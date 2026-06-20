"""
BioWeave Input / Output Utilities
"""

import gzip
import pandas as pd
from io import StringIO


def read_geo_series_matrix(filepath):
    """
    Load GEO Series Matrix file into DataFrame
    """

    with gzip.open(filepath, "rt", errors="ignore") as f:
        lines = f.readlines()

    start = None

    for i, line in enumerate(lines):

        if line.startswith('"ID_REF"'):
            start = i
            break

    expr = pd.read_csv(
        StringIO("".join(lines[start:])),
        sep="\t"
    )

    return expr


def load_gpl_annotation(filepath):
    """
    Load GEO GPL annotation file
    """

    with gzip.open(filepath, "rt", errors="ignore") as f:
        lines = f.readlines()

    start = None

    for i, line in enumerate(lines):

        if line.startswith("ID\t"):
            start = i
            break

    annot = pd.read_csv(
        StringIO("".join(lines[start:])),
        sep="\t",
        low_memory=False
    )

    return annot
