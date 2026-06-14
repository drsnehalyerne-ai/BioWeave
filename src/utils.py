"""
BioWeave Utility Functions
"""

import pandas as pd
import gzip


def read_geo_series_matrix(filepath):
    """
    Read GEO Series Matrix file.
    """

    with gzip.open(filepath, "rt", errors="ignore") as f:
        lines = f.readlines()

    start = None

    for i, line in enumerate(lines):
        if line.startswith('"ID_REF"'):
            start = i
            break

    if start is None:
        raise ValueError("Expression matrix not found.")

    from io import StringIO

    expr = pd.read_csv(
        StringIO("".join(lines[start:])),
        sep="\t"
    )

    return expr
