"""
Differential Expression Module
"""

import pandas as pd
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests


def normal_vs_dysplasia(expr,
                        normal_samples,
                        dysplasia_samples):
    """
    Perform Normal vs Dysplasia DEG analysis.
    """

    results = []

    for _, row in expr.iterrows():

        probe = row["ID_REF"]

        normal = pd.to_numeric(
            row[normal_samples],
            errors="coerce"
        )

        dysplasia = pd.to_numeric(
            row[dysplasia_samples],
            errors="coerce"
        )

        logfc = dysplasia.mean() - normal.mean()

        stat, pval = ttest_ind(
            dysplasia,
            normal,
            nan_policy="omit"
        )

        results.append(
            [probe, logfc, pval]
        )

    deg = pd.DataFrame(
        results,
        columns=[
            "Probe",
            "logFC",
            "pvalue"
        ]
    )

    deg["FDR"] = multipletests(
        deg["pvalue"],
        method="fdr_bh"
    )[1]

    return deg
