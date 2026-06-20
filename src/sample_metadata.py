def build_gse30784_groups(sample_names, sample_status):

    control_samples = []
    dysplasia_samples = []
    cancer_samples = []

    for gsm, status in zip(sample_names, sample_status):

        if "control" in status.lower():
            control_samples.append(gsm)

        elif "dysplasia" in status.lower():
            dysplasia_samples.append(gsm)

        elif "cancer" in status.lower():
            cancer_samples.append(gsm)

    return (
        control_samples,
        dysplasia_samples,
        cancer_samples
    )
