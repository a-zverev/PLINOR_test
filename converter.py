import argparse
import os
import pandas as pd


def format_snps_data(input_file:str, starting_line:int):
    '''
    Convert the data from file - aggregate all allele variants for SNPs/animals
    '''
    return pd.read_csv(input_file, skiprows=lambda x: x<starting_line, sep="\t").\
    assign(Allele = lambda x: x["Allele1 - AB"] + x["Allele2 - AB"]).\
    filter(["Sample ID", "SNP Name", "Allele"]).\
    groupby(["SNP Name", "Sample ID"], as_index = False).\
    aggregate({'Allele': lambda x: '/'.join(x)}).\
    pivot(index="Sample ID", columns="SNP Name", values="Allele")


if __name__ == "__main__":
    
    def file_exist_check(x):
        if not os.path.exists(x):
            raise argparse.ArgumentTypeError(f"{x} does not exist")
        return x

    # parse all arguments
    parser = argparse.ArgumentParser(
                    prog='Converter',
                    description='Test Converter - convert the data from raw format to \
the table and save in .json format. \nColumns: unique SNPs, \nRows: animals IDs, \
\nValues: allele variants', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', '--input-file', required=True, \
                    type=file_exist_check, help="input raw file with SNPs data")
    parser.add_argument('-o', '--output-file', default='converter_out.json',\
                    help="output file for the table. Default: converter_out.json")
    args = parser.parse_args()
    
    # find out, where are the data starts (usually from 9, but who knows)
    def find_word_line_number(filename, target):
        line_number = 0
        with open(filename, 'r') as file:
            for line in file:
                line_number += 1
                if target in line:
                    return line_number

    # convert and write the data
    start_line_number = find_word_line_number(args.input_file, "[Data]")
    format_snps_data(args.input_file, start_line_number).to_json(args.output_file)