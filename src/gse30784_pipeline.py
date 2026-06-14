"""
BioWeave

Pipeline:
GSE30784 Normal vs Dysplasia Analysis

Author: Snehal Yerne
Project: BioWeave
"""

import pandas as pd
import numpy as np

from utils import read_geo_series_matrix


def load_expression_matrix(filepath):
    """
    Load GEO series matrix file.
    """

    print("Loading expression matrix...")

    expr = read_geo_series_matrix(filepath)

    print("Expression matrix shape:", expr.shape)

    return expr


def create_metadata():
    """
    Create sample annotation.
    """
    print("Creating metadata...")
    return None


def differential_expression():
    """
    Normal vs Dysplasia DEG analysis.
    """
    print("Running DEG analysis...")
    return None


def annotate_probes():
    """
    Probe-to-gene annotation.
    """
    print("Annotating probes...")
    return None


def enrichment_analysis():
    """
    GO and KEGG enrichment.
    """
    print("Running enrichment...")
    return None


def export_results():
    """
    Export BioWeave outputs.
    """
    print("Exporting results...")
    return None


def main():

    print("BioWeave GSE30784 Pipeline")

    expr = load_expression_matrix(
    "datasets/GSE30784/GSE30784_series_matrix.txt.gz"
)

    create_metadata()

    differential_expression()

    annotate_probes()

    enrichment_analysis()

    export_results()


if __name__ == "__main__":
    main()
