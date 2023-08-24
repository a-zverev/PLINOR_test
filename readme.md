Here is a simple converter from Illumina SNPs report to a wide table.

I am not familiar with the structure of the report, so, my first aim have to be a discussion with a team leader about the format. I found a description of the format on the Illumina [site](https://knowledge.illumina.com/microarray/general/microarray-general-reference_material-list/000001489) in this [topic](https://www.researchgate.net/post/How_do_I_read_the_genotype_from_the_Illumina_array_final_report_text_file).

As far as I understand, for animal/SNP we are interested in allele combination (AA, AB or BB), rather than the exact nucleotides (TC, TG ect..). But I still have some concerns, and normally I will ask my superviser to be absolutely clear about my task.

This converter re-format the Illumina report to a JSON table. **SNP Names** are column names, **animal IDs** are row names, values are combinations of alleles (from `Allele1 - AB` and `Allele2 - AB` columns) 