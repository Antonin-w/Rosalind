from counting_Nucleotides import DNA_stats
from gene_bank_entries import how_many_entries
from data_formats import shortest_fasta
from fastq_to_fasta import convert_fastq_to_fasta
from read_quality_distribution import number_reads_below_threshold
from read_filtration_by_quality import number_reads_filtered
from protein_translation import which_genetic_code

# a = "GCTTCGGTAAGACTAACTTGCAACTTACATCACTCTGCAGCATGTACGTTGAATTTAAACTCCGTTCACCCTAGCCCCATGCTAGTCCTGTGCAATGGGTCTTACATATGCTGCGAAAGGTATGCATGTTATATGAATGCAGCAATCACAGAACATGTAACTGGTGACGAATGCTCACATCTTATCGCATGCCGCAATAGATGCTTACGATAAGTCCCCTGGGTGTTTTGGAATGATGTTGACAAAGAGCCCGATCGGCTCATGTCAGGGTCGACATCACACACGGAATATGCCAAGCATCGAATGCCATGATAGTACATCAGACTTCCTAATACCTAGCGCGCGAGTAAAGGAGGCGTACAACATAACCATCCCAGACAACCAGATGAGTTCTTGGGCATTTCGAGACCCCTTCTCCGTGAGACCCCCGCAGATGCTCTGTGGAGGGCCGTCACTTCCAGAGATGATGTGAATTGCTCTTTCGAGGCGACGAAAAATCATACATCGGGGCTCATGTCCGGGGAGGGCGCGCGTGACGTACATCCGTGGTGCTATGAAGATTTAATTTCAACCGTGGAAAAATTCATCCTTTAGTTAAATGCTACTGCCCCAGCACCAGGACTCTTCTGCAGTATTTACTATGGTCAAGTGCTTCGGGCTGGCGAAAACTGGTACGCACGTCTGAGACTCTCCGCCGAAAGGTTGCTTGCGATGCCCCGGCGTCCGTTGAACCCCGGCGTCGCTTTCTATTATAAAGTCGACGTCTACGGAGCGCGTAGCCATAGAGAATGAGAACCTCTTACACCTCTCCAATCTAGCGGTTTACTCGCCCTCGTGTTCGATCACATAAGCGTGTCACAC"
# print(DNA_stats(a))

# print(how_many_entries("Vespertilio", '2004/02/12',  '2012/06/22'))

# shortest_fasta("JN573266 JQ762396 NM_001135551 JX280897 NM_001081821 NM_001168970 NM_001015511 JX469985")

# convert_fastq_to_fasta("test_files/fastq1.fastq", "test_files/fasta.fasta")

# print(number_reads_below_threshold(20, "test_files/fastq1.fastq"))

# print(number_reads_filtered(27,75, "test_files/fastq1.fastq"))

print(which_genetic_code("ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA", "MAMAPRTEINSTRING"))
