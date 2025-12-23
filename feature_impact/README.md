# Feature Impact Analysis: SmartFeed_v2 Case Study

A portfolio case study demonstrating **statistical rigor in product analytics** through causal inference techniques.

## 🎯 Project Overview

This project tells the story of how **propensity score matching uncovered a false positive signal** in feature analysis. Initial metrics showed a 144% engagement lift, but deeper statistical analysis revealed the feature provided no retention benefit and posed risks to core users.

**Key Insight:** Distinguishing metric gaming from real product improvements requires more sophisticated analysis than simple statistical tests.

## 📊 Live Case Study Website

**View the interactive case study:** Open `index.html` in your browser

The website includes:
- Professional case study narrative
- 5 interactive Plotly visualizations
- Problem → Methods → Findings → Recommendation flow
- Segment-level analysis and key takeaways
- Technical appendix explaining propensity score matching

## 🔍 The Analysis

### Product Context

SmartFeed is a content discovery surface that delivers short-form summaries of real-world events to users seeking quick, low-friction information consumption. SmartFeed_v2 introduces personalized ranking by reordering content cards based on predicted user relevance scores.

### Key Finding

| Approach | Metric | Result | Truth |
|----------|--------|--------|-------|
| **Naive (T-test)** | Engagement | +144% lift | False positive |
| **Improved (PSM)** | Retention | +0.17% lift | Negligible impact |

### Why This Matters

The naive analysis showed impressive engagement gains but missed the core truth: **the feature provided no retention benefit**. This is classic metric gaming—optimizing for engagement without corresponding improvements in user retention (the north star metric).

Propensity score matching revealed that the initial finding was driven by **selection bias**: more engaged users naturally gravitated toward personalization features, confounding the treatment effect with user characteristics.

## 📁 Project Contents


### Analysis Notebooks
- `naive_bayes.ipynb` - Simple T-test baseline
- `v2.ipynb` - Propensity score matching implementation

### Documentation
- `index.html` - Polished case study website
- `LLM_ANALYSIS.md` - Full technical analysis report

### Original Project Definition
- `data_design/` - Simulated data (50k users, 4.2M events)
- `data_design/simulate_events.py` - Data generation script

## 💡 Key Learning: Propensity Score Matching

**Problem:** Users self-select into SmartFeed_v2 based on engagement level. Unmatched comparison confounds selection bias with treatment effect.

**Solution:** Propensity score matching (PSM)
1. Model propensity to be assigned to SmartFeed_v2
2. Match treated users with similar control users
3. Compare outcomes in matched cohort
4. Result: Balanced groups, valid causal inference

**Impact:** After matching, retention shows no meaningful improvement (85.49% vs 85.32%), revealing the +144% engagement lift was driven by user selection, not feature quality.

## 📈 Key Findings

### False Positive Signal
- **Naive finding:** 144% engagement lift (p < 0.001)
- **Root cause:** Selection bias + metric gaming
- **True causal effect:** Negligible retention improvement (+0.17 pp)

### Segment-Level Risks
- **New users:** 100% retention (sample composition artifact)
- **Returning users:** 85.5% retention (neutral effect)
- **Power users:** 84.98% retention (core segment at risk)

### Recommendation
**🔴 Rollback SmartFeed_v2** - Feature doesn't meet success criteria:
- No meaningful retention gain
- Power user segment at risk
- Content diversity guardrail likely violated
- New user experience may be harmed

## 🚀 Quick Start

### View the Case Study
```bash
# Open in browser
open index.html
```

### Explore the Analysis
```bash
# Run the notebooks
jupyter notebook naive_bayes.ipynb
jupyter notebook v2.ipynb
jupyter notebook chatbot.ipynb
```

### Download Reports
- Download `visualizations_portfolio/findings_summary.csv` for results
- View `LLM_ANALYSIS.md` for full technical details

## 🎓 Portfolio Value

This project demonstrates:

✅ **Statistical Thinking** - Identifying and correcting for selection bias  
✅ **Causal Inference** - Applying propensity score matching to product analytics  
✅ **Business Impact** - Prevented shipping a feature that would harm users  
✅ **Data Storytelling** - Communicating complex findings to stakeholders  
✅ **Full-Stack Skills** - Python, Jupyter, Plotly, HTML/CSS  
✅ **Cross-Functional** - Product, engineering, and analytics collaboration  

## 📚 Technical Stack

- **Languages:** Python, SQL, HTML/CSS
- **Data Analysis:** pandas, numpy, scikit-learn, scipy
- **Visualization:** Plotly, Matplotlib, Seaborn
- **Notebooks:** Jupyter
- **Methods:** Propensity Score Matching, Logistic Regression, T-tests, Causal Inference

## 🔗 Deployment Options

Deploy as a live portfolio website:

**GitHub Pages:** Push to repo, enable Pages in settings  
**Vercel:** `vercel deploy --prod`  
**Netlify:** `netlify deploy --prod`  

## 📄 Data Summary

- **Users:** 50,000 simulated users
- **Events:** 4.2M simulated product events  
- **Segments:** New, Returning, Power
- **Time Horizon:** User lifecycle events, 7-day retention window
- **Status:** Simulated data for educational purposes

## 🤔 Questions This Raises

1. **When should you use propensity score matching vs A/B testing?**
   - PSM: Observational data, faster analysis
   - A/B testing: Most reliable, but slower and more expensive

2. **How do you know if your matching was successful?**
   - Check covariate balance between treated and matched control
   - Compare propensity score distributions
   - Sensitivity analysis on unobserved confounding

3. **What guardrails prevent this kind of metric gaming?**
   - Define north star metric (retention, not engagement)
   - Implement content diversity metrics
   - Monitor segment-level effects
   - Track cohort retention over time

## 📖 References

- Rosenbaum & Rubin (1983) - Propensity Score Matching
- Angrist & Pischke (2009) - Mostly Harmless Econometrics  
- Pearl (2009) - The Book of Why
- Product analytics best practices from Meta, Netflix, Airbnb

---

**Portfolio Project** | Created: December 2025 | Status: Complete