
"""
BioWeave

End-to-End GSE30784 Pipeline

Author: Snehal Yerne
Project: BioWeave
"""

import os
import pandas as pd

from data_loader import (
    read_geo_series_matrix,
    load_gpl_annotation
)

from differential_expression import (
    run_deg
)

from annotation import (
    annotate_deg
)

from bridge_genes import (
    find_bridge_genes
)

# -----------------------------------
# DATA PATHS
# -----------------------------------

DATA_DIR = "/content/drive/MyDrive/BioWeave/data"

GSE_FILE = f"{DATA_DIR}/GSE30784_series_matrix.txt.gz"
GPL_FILE = f"{DATA_DIR}/GPL570.annot.gz"


def main():

    print("BioWeave GSE30784 Pipeline")

    # -------------------------
    # Load data
    # -------------------------

    print("Loading expression matrix...")

    expr = read_geo_series_matrix(
        GSE_FILE
    )

    print("Loading annotation...")

    annot = load_gpl_annotation(
        GPL_FILE
    )

    print("Expression shape:", expr.shape)
    print("Annotation shape:", annot.shape)

    # -------------------------
    # Build sample groups
    # -------------------------

    sample_names = list(expr.columns[1:])

    print("Building sample groups...")

    # Temporary grouping
    control = sample_names[:45]
    dysplasia = sample_names[45:62]
    cancer = sample_names[62:]

    print("Control:", len(control))
    print("Dysplasia:", len(dysplasia))
    print("Cancer:", len(cancer))

    # -------------------------
    # Prepare expression matrix
    # -------------------------

    expr_num = expr.set_index("ID_REF")
    expr_num = expr_num.astype(float)

    # -------------------------
    # DEG Analysis
    # -------------------------

    print("Running Control vs Dysplasia DEG...")

    dys_deg = run_deg(
        expr_num,
        control,
        dysplasia
    )

    dys_deg = dys_deg[
        (dys_deg["adj.P.Val"] < 0.05)
        &
        (abs(dys_deg["logFC"]) > 1)
    ]

    print("Significant DEGs:", len(dys_deg))

    # -------------------------
    # Annotation
    # -------------------------

    print("Annotating genes...")

    dys_deg_annot = annotate_deg(
        dys_deg,
        annot
    )

    # -------------------------
    # Bridge Genes
    # -------------------------

    print("Finding bridge genes...")

    bridge = find_bridge_genes(
        dys_deg_annot,
        dys_deg_annot
    )

    print("Bridge genes:", len(bridge))

    # -------------------------
    # Export
    # -------------------------

    os.makedirs(
        "results",
        exist_ok=True
    )

    dys_deg_annot.to_csv(
        "results/control_vs_dysplasia_deg.csv",
        index=False
    )

    pd.DataFrame(
        bridge,
        columns=["Gene Symbol"]
    ).to_csv(
        "results/bridge_genes.csv",
        index=False
    )

    print("Pipeline completed successfully")


if __name__ == "__main__":
    main()
    main()
```
