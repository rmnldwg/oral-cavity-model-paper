# Oral Cavity Model Paper

[![CCDS Badge](https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter)](https://cookiecutter-data-science.drivendata.org)

Modelling the tumor progression based on lymphatic spread patterns of newly diagnosed oral cavity squamous cell carcinoma patient records.

## Project Organization

```txt
├── LICENSE               <- Open-source MIT license.
├── README.md             <- Detailed information about the setup and experiments in this project.
├── data
│   ├── external          <- Data from rmnldwg/lydata repo.
│   └── processed         <- The final, canonical data set for modeling.
│
├── models                <- Drawn samples and computed posteriors or risks.
│
├── pyproject.toml        <- Project configuration file with package metadata for
│                            ocmscripts and configuration for tools like ruff.
│
├── uv.lock               <- A cross-platform lockfile of the virtual Python environment created and
|                            updated whenever a command is run via `uv run`.
|
├── dvc.yaml              <- Defines the data, sampling, and inference pipeline.
|
├── dvc.lock              <- A locked record of the state of the defined pipeline using MD5 file hashes.
│
├── reports               <- Generated analysis as HTML, PDF, LaTeX, etc.
│   ├── figures           <- Generated graphics and figures to be used in reporting.
│   └── manuscript.qmd    <- The main manuscript of the publication.
│
└── ocmscripts            <- Source code for use in this project.
    │
    ├── __init__.py           <- Makes ocmscripts a Python module.
    │
    ├── config.py             <- Store useful variables and configuration.
    │
    ├── dataset.py            <- Scripts to concatenate and filter.
    │
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py        <- Code to run model inference with drawn samples.
    │   └── train.py          <- Code to draw MCMC samples.
    │
    └── plots.py              <- Code to create visualizations.
```

--------
