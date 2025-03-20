from pathlib import Path
import warnings

from loguru import logger
from lydata import C
from lydata.utils import infer_and_combine_levels
import typer

from ocmscripts.config import PROCESSED_DATA_DIR

warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd  # noqa: E402

app = typer.Typer()


def compile_icd_codes(start: int = 2, end: int = 6) -> list[str]:
    """Compile a list of ICD codes from the given range."""
    icd_codes = []
    for i in range(start, end + 1):
        base = f"C{i:02d}"
        icd_codes += [base] + [f"{base}.{j}" for j in range(10)]
    return icd_codes


@app.command()
def main(
    input_paths: list[Path],
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
):
    """Combine multiple datasets and filter for oral cavity subsites."""
    datasets = []
    for input_path in input_paths:
        dataset = pd.read_csv(input_path, header=[0,1,2])
        dataset = infer_and_combine_levels(dataset)
        datasets.append(dataset)
        logger.info(f"Loaded dataset from {input_path = }")

    joined_dataset = pd.concat(datasets, axis="index", ignore_index=True)
    logger.info(f"Concatenated {joined_dataset.shape = }")

    is_oral_cavity = C("subsite").isin(compile_icd_codes(2, 6))
    filtered_dataset = joined_dataset.ly.query(query=is_oral_cavity)
    logger.info(f"Remaining {filtered_dataset.shape = }")

    filtered_dataset.to_csv(output_path, index=False)
    logger.success(f"Saved dataset to {output_path = }")


if __name__ == "__main__":
    app()
