import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests


def run_deg(expr_num, group1_samples, group2_samples):
    """
    Differential expression analysis:
    group2 vs group1

    Returns a dataframe with:
    Probe, logFC, P.Value, adj.P.Val
    """

    results = []

    for probe in expr_num.index:

        group1 = pd.to_numeric(
            expr_num.loc[probe, group1_samples],
            errors="coerce"
        ).dropna()

        group2 = pd.to_numeric(
            expr_num.loc[probe, group2_samples],
            errors="coerce"
        ).dropna()

        # Skip probes with too few observations
        if len(group1) < 2 or len(group2) < 2:
            results.append([probe, np.nan, np.nan])
            continue

        stat, pval = ttest_ind(
            group2,
            group1,
            equal_var=False,
            nan_policy="omit"
        )

        logfc = group2.mean() - group1.mean()

        results.append([probe, logfc, pval])

    deg = pd.DataFrame(
        results,
        columns=["Probe", "logFC", "P.Value"]
    )

    # Initialize adjusted p-values as NaN
    deg["adj.P.Val"] = np.nan

    # Only run FDR on valid p-values
    valid_mask = deg["P.Value"].notna()

    if valid_mask.sum() > 0:
        deg.loc[valid_mask, "adj.P.Val"] = multipletests(
            deg.loc[valid_mask, "P.Value"],
            method="fdr_bh"
        )[1]

    return deg.sort_values("adj.P.Val", na_position="last")
