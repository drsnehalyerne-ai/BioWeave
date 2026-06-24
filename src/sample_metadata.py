
import gzip


def extract_sample_status(filepath):
    """
    Extract true sample status from GEO series matrix.

    Looks through all !Sample_characteristics_ch1 lines and finds
    the one containing status labels like:
    - status: control
    - status: dysplasia
    - status: cancer
    """

    characteristic_lines = []

    with gzip.open(filepath, "rt", errors="ignore") as f:
        for line in f:
            if line.startswith("!Sample_characteristics_ch1"):
                parts = line.strip().split("\t")[1:]
                cleaned = [
                    x.replace('"', '').strip().lower()
                    for x in parts
                ]
                characteristic_lines.append(cleaned)

    if not characteristic_lines:
        raise ValueError("No !Sample_characteristics_ch1 lines found in GEO series matrix")

    status_line = None
    for row in characteristic_lines:
        joined = " | ".join(row)
        if ("control" in joined) or ("dysplasia" in joined) or ("cancer" in joined):
            status_line = row
            break

    if status_line is None:
        raise ValueError("Could not find a status-containing characteristics line")

    sample_status = {}
    for i, value in enumerate(status_line):
        value = value.replace("status:", "").strip().lower()

        if "control" in value:
            sample_status[i] = "control"
        elif "dysplasia" in value:
            sample_status[i] = "dysplasia"
        elif "cancer" in value:
            sample_status[i] = "cancer"
        else:
            sample_status[i] = "unknown"

    return sample_status


def build_gse30784_groups(sample_names, filepath):
    """
    Build control, dysplasia, and cancer sample groups from GEO metadata.
    """

    status_by_index = extract_sample_status(filepath)

    control = []
    dysplasia = []
    cancer = []

    for i, gsm in enumerate(sample_names):
        status = status_by_index.get(i, "unknown")

        if status == "control":
            control.append(gsm)
        elif status == "dysplasia":
            dysplasia.append(gsm)
        elif status == "cancer":
            cancer.append(gsm)

    return control, dysplasia, cancer

