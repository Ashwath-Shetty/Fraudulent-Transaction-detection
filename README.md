# Fraudulent-Transaction-detection
## Problem Statement
You are provided a synthetic dataset for a mobile payments application. In this dataset, you are
provided the sender and recipient of a transaction as well as whether transactions are tagged as
fraud or not fraud. Your task is to build a fraud detection API that can be called to predict
whether or not a transaction is fraudulent.
You are expected to build a REST API that predicts whether a given transaction is fraudulent or
not. You are also to assume that the previous API calls are to be stored in order to engineer
features relevant to finding fraud. The API calls will include the time step of the transaction, so
you can assume that a transaction happens sequentially within the same time step.

### A typical top-level directory layout

    .
    ├── build                   # Compiled files (alternatively `dist`)
    ├── docs                    # Documentation files (alternatively `doc`)
    ├── src                     # Source files (alternatively `lib` or `app`)
    ├── test                    # Automated tests (alternatively `spec` or `tests`)
    ├── tools                   # Tools and utilities
    ├── LICENSE
    └── README.md
