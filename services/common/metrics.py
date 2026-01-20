from prometheus_client import Counter, Histogram

ci_failures = Counter("ci_failures_total", "Total CI failures")
auto_fixed = Counter("ci_auto_fixed_total", "Auto-fixed failures")
fix_time = Histogram("ci_fix_seconds", "Time to fix")
