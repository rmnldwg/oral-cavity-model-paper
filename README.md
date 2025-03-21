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
│   ├── configs           <- YAML files that define models and how to sample their params.
│   ├── histories         <- Bookkeeping of how a MCMC sampling round went.
│   └── samples           <- The burned-in and thinned chain of MCMC samples as HDF5 files.
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

## Pipeline

We use [DVC] as a pipeline management and execution tool. Similar to [Make], it defines a directed acyclic graph (DAG) from inputs and outputs of various computational stages. Taken together, the pipeline ingests the data in the `data/external/` folder as well as any model/sampling configurations files (e.g. in `models/configs/`) to draw parameter samples (stored in `models/samples/`) and create figures and plots (which get saved to `/reports/figures/`).

The pipeline is defined in a human-readable `dvc.yaml` file and a successful run produces a `dvc.lock` lockfile. This lockfile can also be used to cache runs with different parameters or download selected runs that are uploaded to Azure blob storage containers.

[DVC]: https://dvc.org
[Make]: https://www.gnu.org/software/make/

## Python Scripts

The individual computational stages within the pipeline are done mostly using custom [Python] (version 3.10) scripts or custom lyscripts CLIs. In order to have a working environment as close as possible to the one in which all results were produced, we recommend using [uv]. With this repository also comes a cross-plattform lockfile that should allow the easy creation of an isolated and OS-independent virtual [Python] environment.

[Python]: https://docs.python.org/3.10/
[uv]: https://docs.astral.sh/uv/

## Manuscript

The actual paper is written in [Quarto]'s [markdown] flavour and can be found in `reports/manuscript.qmd`. Using [Quarto], this output-agnostic source file can then be compiled into different file formats for reading, e.g. HTML, PDF, Word, etc.

[Quarto]: https://quarto.org/
[markdown]: https://daringfireball.net/projects/markdown/
