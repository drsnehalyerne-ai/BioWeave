import pandas as pd


def annotate_deg(deg, annot):

    deg_annot = deg.merge(
        annot[
            ["ID", "Gene symbol", "Gene title"]
        ],
        left_on="Probe",
        right_on="ID",
        how="left"
    )

    return deg_annot
