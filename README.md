# MEMED PULSE

**Attention Intelligence for the Creator Economy** — an independent, Vercel-ready applied-ML prototype that estimates relative content attention, explains the signal mix, retrieves similar demo content, and scores optimization variants.

## Product

The application includes an analyzer, dashboard, explorer, campaign lab, creator recommendations, model transparency, and settings. Every displayed score runs through `lib/engine.ts`; no LLM invents performance scores.

## ML pipeline

- **Dataset:** 300 correlated synthetic/curated demonstration records. It is not platform data or a claim of real-world performance.
- **Features:** caption token/punctuation/emotional/cultural proxies, semantic novelty, alignment proxy, audience fit, and brand suitability.
- **Embeddings:** deterministic 48-dimensional normalized hashed word vectors, cached by deterministic calculation at demo scale.
- **Similarity:** cosine similarity ranked against the seed corpus.
- **Prediction:** Vercel-safe deterministic weighted scoring surrogate. `ml/training/train.py` provides an optional reproducible sklearn `GradientBoostingRegressor` workflow.
- **Explainability:** exact weighted feature contributions; explicitly not SHAP.
- **Recommendation:** `0.35 × category affinity + 0.30 × semantic relevance + 0.20 × predicted performance + 0.15 × novelty`.

## Evaluation

The prototype dashboard reports synthetic holdout values: model MAE **5.8**, RMSE **7.2**, R² **0.78**; mean baseline MAE **12.6**, RMSE **15.7**, R² **0.00**. Run the offline Python pipeline to generate fresh metrics from the synthetic generator.

## Local development

```bash
npm install
npm run dev
```

Run `python ml/data/generate_dataset.py` from `ml/data`, then `python ml/training/train.py` for the optional offline training path (requires pandas, scikit-learn, joblib).

## API

`POST /api/analyze`, `/predict`, `/similarity`, `/explain`, `/recommend`, `/optimize`, `/campaign`, `/upload`; `GET /api/content`, `/api/content/:id`, `/api/model/metrics`, `/api/creator/:id`.

## Environment and deployment

Copy `.env.example` to `.env.local` only if adding optional LLM copy generation. No variable is required for demo mode. Push to GitHub, import the repository in Vercel, and use the default Node build command (`npm run build`). This self-contained demo needs no database or Python service in Vercel. See [architecture](docs/architecture.md) and [model card](docs/model_card.md).

## Limitations / future work

This is a transparent prototype using synthetic data and text-first deterministic features. Production use needs consented, representative historical data, validated visual models, proper train/test reporting, monitoring, privacy controls, and a separately deployed inference service for the serialized model.
