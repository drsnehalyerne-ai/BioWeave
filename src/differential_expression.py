import pandas as pd
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests


def run_deg(expr_num, group1_samples, group2_samples):

    results = []

    for probe in expr_num.index:

        group1 = expr_num.loc[probe, group1_samples]
        group2 = expr_num.loc[probe, group2_samples]

        stat, pval = ttest_ind(
            group2,
            group1,
            equal_var=False,
            nan_policy="omit"
        )

        logfc = group2.mean() - group1.mean()

        results.append(
            [probe, logfc, pval]
        )

    deg = pd.DataFrame(
        results,
        columns=["Probe", "logFC", "P.Value"]
    )

    deg["adj.P.Val"] = multipletests(
        deg["P.Value"],
        method="fdr_bh"
    )[1]

    return deg.sort_values("adj.P.Val")
