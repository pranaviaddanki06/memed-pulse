# ML components

`data/generate_dataset.py` creates a correlated synthetic dataset. `training/train.py` provides an optional offline sklearn GradientBoosting training flow. The deployed Next.js demo uses a serializable-in-spirit deterministic scoring surrogate, so Vercel does not need Python or model binaries. Its cosine retrieval uses normalized 48-dimensional hashed text vectors.
