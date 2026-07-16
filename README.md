In this directory we have several jupyter notebooks and files

1. (peptide_hitcalling.ipynb)

Input: 
"./preprocessing/earliest_tp_rpk_avg_value_for_cohort_techreps_071626.csv"
"./preprocessing/master_sample_metadata_060626.csv"
"./preprocessing/hbdb_pass_100k_techreps_averaged_071626.csv"
"lassa_library_sequences_species_standardized_070726.csv"

Output:
"long_df_z_score_SL_over_US.csv"
"indices_peps_sig_pos_d_z_071626.csv"

This notebook 
- log10(RPK + 1) transforms for each peptide in each individual (both SL and US cohorts)
- calculates the z score for SL over US
- saves results in a long df which has metadata appended : "long_df_z_score_SL_over_US.csv"

This notebook also
- performs MWU to identify statistically significant peptides by comparing the z scores for each peptide
of SL cohort to z scores for each peptide in each US healthy by Leave-one-out analysis.
- the statistical calculation is only performed when a peptide has > 2 individuals in each group
- the output is a FDR adjusted p value for each peptide, the delta z (which is the subtraction of the 
median z value for that peptide for US from the median z value for that peptide for SL : positive
delta z means significant for SL ), and the fraction enriched, which calculates the percentage of 
the SL cohort which has a z score > 3 for this peptide.

Info:

All Lassa-exposed longitudinal vs HBDB - tested: 88,295  FDR < 0.05: 53,300
  Exposed-enriched (delta_z > 0): 36754
  HBDB-enriched    (delta_z < 0): 16546
