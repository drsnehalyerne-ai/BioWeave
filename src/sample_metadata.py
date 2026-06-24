import gzip


def extract_sample_status(filepath):
    """
    Parse GSE30784 series matrix header and extract
    sample status for each GSM accession.

    Returns
    -------
    sample_status : dict
        {sample_name: "control"/"dysplasia"/"cancer"}
    """

    with gzip.open(filepath, "rt", errors="ignore") as f:
        for line in f:
            if line.startswith("!Sample_characteristics_ch1"):
                parts = line.strip().split("\t")

                # first column is the metadata label itself
                raw_status = parts[1:]

                sample_status = {}
                for i, status in enumerate(raw_status):
                    status = status.replace('"', '').strip().lower()
                    # status looks like: status: cancer
                    status = status.replace("status:", "").strip()
                    sample_status[i] = status

                return sample_status

    raise ValueError("Could not find !Sample_characteristics_ch1 in series matrix")


def build_gse30784_groups(sample_names, filepath):
    """
    Build control, dysplasia, and cancer sample lists
    using true GEO metadata rather than positional slicing.

    Parameters
    ----------
    sample_names : list
        GSM sample names in the expression matrix
    filepath : str
        Path to GSE30784_series_matrix.txt.gz

    Returns
    -------
    control, dysplasia, cancer : lists of GSM names
    """

    status_by_index = extract_sample_status(filepath)

    control = []
    dysplasia = []
    cancer = []

    for i, gsm in enumerate(sample_names):
        status = status_by_index[i]

        if status == "control":
            control.append(gsm)
        elif status == "dysplasia":
            dysplasia.append(gsm)
        elif status == "cancer":
            cancer.append(gsm)

    return control, dysplasia, cancer
