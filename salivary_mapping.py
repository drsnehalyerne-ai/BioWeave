import pandas as pd

def run_salivary_translational_mapping(v2_bridge_genes_df):
    print("Initializing BioWeave v3: Translational Salivary Mapping Engine...")
    VERIFIED_SALIVARY_PROTEOME = {
        "MMP1", "MMP2", "MMP3", "MMP9", "TIMP1", "TIMP2", "IL6", "IL8", "IL1B", 
        "TNF", "VEGFA", "TGFB1", "IFNG", "CCL2", "S100A7", "S100A8", "S100A9", 
        "S100A12", "EGFR", "CD44", "CYFRA21-1", "KRT6A", "KRT14", "KRT19", "CEA", 
        "MUC1", "TP53", "CCND1", "BIRC5", "PCNA", "MKI67", "FN1", "CDH1", "STAT3", 
        "AKT1", "PIK3CA", "SRC", "MAPK1", "CST3", "LCN2", "LTF", "SPO1", "AMY1A", 
        "HMGN2", "MSLN"
    }
    
    v3_salivary_mapped = v2_bridge_genes_df[v2_bridge_genes_df['gene_symbol'].isin(VERIFIED_SALIVARY_PROTEOME)].copy()
    
    def prioritize_biomarker(row):
        if abs(row.get('logFC_dysplasia_vs_control', 0)) > 1.5 and abs(row.get('logFC_oscc_vs_dysplasia', 0)) > 1.0:
            return "Tier-1: Linear Progression Tracer (Ideal Early Detection)"
        elif abs(row.get('logFC_dysplasia_vs_control', 0)) > 1.5:
            return "Tier-2: Early Dysplastic Diagnostic Switch"
        elif abs(row.get('logFC_oscc_vs_dysplasia', 0)) > 1.5:
            return "Tier-3: Late-Stage Malignancy Transition Marker"
        return "Tier-4: Auxiliary Diagnostic Indicator"

    if not v3_salivary_mapped.empty:
        v3_salivary_mapped['clinical_priority'] = v3_salivary_mapped.apply(prioritize_biomarker, axis=1)
    
    print(f"Successfully isolated {len(v3_salivary_mapped)} translationally viable salivary biomarkers!")
    return v3_salivary_mapped
