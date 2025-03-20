# Oral Cavity Model Paper

[![CCDS Badge](https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter)](https://cookiecutter-data-science.drivendata.org)

Modelling the tumor progression based on lymphatic spread patterns of newly diagnosed oral cavity squamous cell carcinoma patient records.

## Project Organization

```txt
├── LICENSE               <- Open-source license if one is chosen
├── README.md             <- The top-level README for developers using this project.
├── data
│   ├── external          <- Data from third party sources.
│   └── processed         <- The final, canonical data sets for modeling.
│
├── models                <- Trained and serialized models, model predictions, or model summaries
│
├── pyproject.toml        <- Project configuration file with package metadata for 
│                            ocmscripts and configuration for tools like black
│
├── reports               <- Generated analysis as HTML, PDF, LaTeX, etc.
│   ├── figures           <- Generated graphics and figures to be used in reporting
│   └── manuscript.qmd    <- The main manuscript of the publication
│
└── ocmscripts            <- Source code for use in this project.
    │
    ├── __init__.py           <- Makes ocmscripts a Python module
    │
    ├── config.py             <- Store useful variables and configuration
    │
    ├── dataset.py            <- Scripts to download or generate data
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py        <- Code to run model inference with trained models          
    │   └── train.py          <- Code to train models
    │
    └── plots.py              <- Code to create visualizations
```

--------
