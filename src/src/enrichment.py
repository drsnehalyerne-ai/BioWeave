"""
Functional Enrichment Module
"""

import pandas as pd


def prepare_gene_list(
    deg_annot,
    fdr_threshold=0.05,
    logfc_threshold=1.0
):
    """
    Generate gene list for enrichment.
    """

    genes = deg_annot[
        (deg_annot["FDR"] < fdr_threshold)
        &
        (abs(deg_annot["logFC"]) > logfc_threshold)
    ]

    genes = genes["Gene Symbol"]

    genes = genes.dropna()

    genes = genes.astype(str)

    genes = genes.drop_duplicates()

    return genes.tolist()


def export_gene_list(
    genes,
    output_file
):
    """
    Export gene list for STRING,
    g:Profiler, Enrichr.
    """

    pd.Series(
        genes
    ).to_csv(
        output_file,
        index=False,
        header=["Gene"]
    )

    print(
        f"Exported {len(genes)} genes."
    )
