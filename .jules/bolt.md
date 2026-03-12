## 2025-05-15 - [Rate Limiter Cleanup Optimization]
**Learning:** Redundant deep cleanup of request deques in a background task is an anti-pattern when the same cleanup is already performed lazily at the call-site (is_allowed). Global cleanup should focus on evicting stale high-level objects (windows) using a 'last_access' timestamp.
**Action:** Use lazy cleanup for fine-grained data and O(N) timestamp checks for global state pruning.
