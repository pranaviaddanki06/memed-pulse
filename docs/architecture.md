# Architecture

```text
User → Next.js UI → API routes → feature extraction → normalized text embedding
     → cosine vector search → deterministic prediction → weighted attribution
     → optimization/recommendation → UI
```

The deployable prototype avoids heavyweight serverless inference. An optional sklearn training workflow lives in `ml/`; replace the TypeScript scoring adapter with a separately deployed Python inference service when using a persisted real model.
