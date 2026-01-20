# Runbook — AI Self-Healing CI/CD Platform

## Common Operations

### Restart Services

```bash
kubectl rollout restart deployment log-collector
kubectl rollout restart deployment failure-analyzer
kubectl rollout restart deployment fix-generator
