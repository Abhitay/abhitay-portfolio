**Files in this folder**
- **events.csv:** simulated event-level data (session starts, card views, session ends).
- **users.csv:** per-user metadata (signup date, engagement propensity, segment, assigned feature flag).
- **simulate_events.py:** script that generates both `users.csv` and `events.csv`.

**High-level generation process**
- Create N users with a `signup_date` sampled around a START_DATE.
- Assign each user an `engagement_score` (beta distribution) and derive a `segment` (`new`, `returning`, `power`).
- Assign feature exposure (`SmartFeed_v2` or `control`) with segment-dependent probabilities (power users are more likely to see the treatment — deliberate selection bias).
- Simulate multiple active days per user, producing session-level and event-level rows. Inject a novelty boost (higher views in first week for treated users) and a higher early-churn probability for some new users when exposed.

**Schema (column descriptions)**
- `users.csv`:
	- `user_id` (string): UUID unique per user.
	- `signup_date` (datetime): initial signup date used as baseline for events.
	- `engagement_score` (float): latent propensity used to segment users.
	- `segment` (categorical): derived from `engagement_score`; values: `new`, `returning`, `power`.
	- `feature_flag` (categorical): either `SmartFeed_v2` or `control`.

- `events.csv`:
	- `user_id` (string): foreign key to `users.csv`.
	- `event_time` (datetime): event timestamp.
	- `event_name` (string): e.g., `session_start`, `card_view`, `session_end`.
	- `session_id` (string): UUID for sessions; groups events into sessions.
	- `feature_flag` (categorical): copied from users at time of simulation.
	- `content_id` (string|null): content identifier for `card_view` events.

**Design choices and signals**
- *Selection bias*: `power` users have a higher probability of being exposed to `SmartFeed_v2`. This creates a confounder between exposure and baseline engagement.
- *Novelty effect*: treated users see a temporary engagement uplift during the first ~7 days (modelled as a multiplicative boost to view counts).
- *Heterogeneous effects*: different segments respond differently to the feature — some benefit, some churn.
- *Retention risk*: new users exposed to the feature have a small probability to churn early; this creates a trade-off between short-term engagement and longer-term retention.

**Reproducibility & parameters**
- The script sets random seeds for `numpy` and `random` for reproducible output by default.
- Key parameters are defined at the top of `simulate_events.py` (for the current script): `N_USERS`, `START_DATE`, and `N_DAYS`. Edit these constants to change dataset size or time horizon.