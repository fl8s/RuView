## 2025-05-14 - [Optimize Linux RSSI collector by replacing iw subprocess with procfs reads]
**Learning:** Spawning a subprocess (like 'iw') in a high-frequency loop (10Hz) introduces significant overhead (~2.3ms/call). Reading directly from '/proc/net/dev' and '/proc/net/wireless' is ~400x faster (~0.006ms/call) and provides equivalent telemetry.
**Action:** Prefer direct procfs/sysfs reads over spawning external binaries for telemetry collection on Linux.
