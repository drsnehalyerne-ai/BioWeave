def find_bridge_genes(
    dysplasia_deg_annot,
    cancer_deg_annot
):

    dysplasia_genes = set(
        dysplasia_deg_annot["Gene symbol"].dropna()
    )

    cancer_genes = set(
        cancer_deg_annot["Gene symbol"].dropna()
    )

    bridge_genes = dysplasia_genes.intersection(
        cancer_genes
    )

    return sorted(list(bridge_genes))
