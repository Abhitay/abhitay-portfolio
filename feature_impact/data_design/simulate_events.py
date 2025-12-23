import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import uuid
import random

np.random.seed(42)
random.seed(42)

# -----------------------------
# Config
# -----------------------------
N_USERS = 50000
START_DATE = datetime(2024, 9, 1)
N_DAYS = 30

# -----------------------------
# User generation
# -----------------------------
users = pd.DataFrame({
    "user_id": [str(uuid.uuid4()) for _ in range(N_USERS)],
    "signup_date": [
        START_DATE + timedelta(days=np.random.randint(0, 10))
        for _ in range(N_USERS)
    ]
})

# Engagement propensity (latent)
users["engagement_score"] = np.random.beta(2, 5, size=N_USERS)

# Segment users
users["segment"] = pd.cut(
    users["engagement_score"],
    bins=[0, 0.3, 0.7, 1.0],
    labels=["new", "returning", "power"]
)

# -----------------------------
# Feature exposure (biased)
# -----------------------------
def assign_exposure(segment):
    if segment == "power":
        return np.random.choice(["SmartFeed_v2", "control"], p=[0.8, 0.2])
    if segment == "returning":
        return np.random.choice(["SmartFeed_v2", "control"], p=[0.5, 0.5])
    return np.random.choice(["SmartFeed_v2", "control"], p=[0.3, 0.7])

users["feature_flag"] = users["segment"].apply(assign_exposure)

# -----------------------------
# Event simulation
# -----------------------------
events = []

for _, row in users.iterrows():
    user_id = row["user_id"]
    segment = row["segment"]
    feature = row["feature_flag"]

    active_days = np.random.randint(3, N_DAYS)
    churn_early = (
        segment == "new"
        and feature == "SmartFeed_v2"
        and np.random.rand() < 0.15
    )

    for day in range(active_days):
        if churn_early and day > 5:
            break

        session_id = str(uuid.uuid4())
        session_time = row["signup_date"] + timedelta(days=day)

        events.append([
            user_id, session_time, "session_start",
            session_id, feature, None
        ])

        # novelty effect
        novelty_boost = 1.5 if (feature == "SmartFeed_v2" and day < 7) else 1.0

        base_views = {
            "new": 2,
            "returning": 4,
            "power": 8
        }[segment]

        n_views = int(
            np.random.poisson(base_views * novelty_boost)
        )

        for _ in range(max(1, n_views)):
            content_id = f"card_{np.random.randint(1, 500)}"
            events.append([
                user_id,
                session_time + timedelta(minutes=np.random.randint(1, 30)),
                "card_view",
                session_id,
                feature,
                content_id
            ])

        events.append([
            user_id,
            session_time + timedelta(minutes=35),
            "session_end",
            session_id,
            feature,
            None
        ])

# -----------------------------
# Create dataframe
# -----------------------------
events_df = pd.DataFrame(
    events,
    columns=[
        "user_id",
        "event_time",
        "event_name",
        "session_id",
        "feature_flag",
        "content_id"
    ]
)

events_df.to_csv("events.csv", index=False)
users.to_csv("users.csv", index=False)

print("Generated:")
print(events_df.shape)
