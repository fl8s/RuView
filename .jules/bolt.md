## 2025-03-14 - [Subprocess overhead in high-frequency sensing]
**Learning:** Calling `subprocess.run` (e.g., `iw station dump`) at 10Hz creates a significant performance bottleneck due to context switching and process creation overhead (~2ms per call). Replacing these with direct `/proc` or `/sys` file reads reduces the overhead by ~95% (~0.1ms per call).
**Action:** Prefer direct kernel filesystem reads (`/proc`, `/sys`) over CLI tools for high-frequency data collection loops.
