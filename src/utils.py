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
        from io import StringIO

end = None

for i, line in enumerate(lines):

    if line.startswith("!series_matrix_table_end"):
        end = i
        break

if end is None:
    end = len(lines)

expr = pd.read_csv(
    StringIO("".join(lines[start:end])),
    sep="\t"
)

return expr
