# lasv_phipseq_2026

We have several files and scripts in this preprocessing folder. 

1. (All_source_plates_mapped_rpk_column_names_standardized_unique_identifiers_for_duplicates_with_hbdb_plate_samples_dropped_less_100k_readcounts_071426.csv)

This file stores the raw RPK values of all PhIP-Seq runs on this cohort. Samples which did not surpass readcounts of 100k were removed. Column names were standardized and identifiers added for technical replicates. 

2. 
(Analysis_QC_and_averaging_of_techreps_071626.ipynb)

Input: All_source_plates_mapped_rpk_column_names_standardized_unique_identifiers_for_duplicates_with_hbdb_plate_samples_dropped_less_100k_readcounts_071426.csv

Output:
(rpk_df_technical_replicates_samples_passing_readcounts_100k_all_averaged_071626.csv)
(hbdb_pass_100k_techreps_averaged_071626.csv)

This notebook performs quality control on the PhIP-Seq runs itself, such as:
do technical replicates correlate well with themselves? 
how about GFAP wells? 

This notebook also takes the average peptide value for technical replicates. 

This notebook also subsets the dataframe to US healthies for downstream analysis. 

3. 
(Subset_to_earliest_tp.ipynb)

Input:
(rpk_df_technical_replicates_samples_passing_readcounts_100k_all_averaged_071626.csv)

Output:
(earliest_tp_rpk_avg_value_for_cohort_techreps_071626.csv)

This notebook subsets the cohort samples to their earliest timepoint of collection. 
