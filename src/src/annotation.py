"""
GPL570 Annotation Module
"""

import pandas as pd
import gzip
from io import StringIO


def load_gpl570_annotation(filepath):
    """
    Load GPL570 annotation file.
    """

    with gzip.open(filepath, "rt", errors="ignore") as f:
        lines = f.readlines()

    start = None

    for i, line in enumerate(lines):

        if line.startswith("ID\t"):
            start = i
            break

    if start is None:
        raise ValueError(
            "Could not find GPL570 table."
        )

    annot = pd.read_csv(
        StringIO("".join(lines[start:])),
        sep="\t",
        low_memory=False
    )

    return annot


def annotate_deg(deg, annot):
    """
    Add gene symbols and gene names.
    """

    merged = deg.merge(
        annot[
            [
                "ID",
                "Gene Symbol",
                "Gene Title"
            ]
        ],
        left_on="Probe",
        right_on="ID",
        how="left"
    )

    return merged
