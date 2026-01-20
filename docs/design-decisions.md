
---

# 📁 docs/design-decisions.md

```md
# Design Decisions

## Why Microservices?

Allows independent scaling and fault isolation between:
- Logging
- Analysis
- Fix generation
- Execution

---

## Why Vector DB?

Enables semantic similarity matching instead of fragile regex-based detection.

---

## Why Human-in-the-Loop?

To prevent:
- Accidental destructive fixes
- Hallucinated LLM outputs
- Compliance violations

---

## Why GitOps?

Ensures:
- Immutable deployments
- Auditable change history
- Rollback safety

---

## Why Policy Engine?

To block:
- terraform destroy
- secret rotations
- rm -rf
- database drops

---

## Why OpenTelemetry?

To unify:
- Logs
- Metrics
- Traces

Across pipelines and AI services.

---

## Trade-offs

- Slight latency added to pipelines  
- LLM costs  
- Increased complexity  

Accepted to improve reliability and MTTR.
