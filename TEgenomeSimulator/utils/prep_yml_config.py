import os
import sys
import argparse
import re
import pandas as pd
from Bio import SeqIO
from pathlib import Path

# parse argument
parser = argparse.ArgumentParser()
parser.add_argument("-p","--prefix", type=str,
                    help="project prefix of the simulation")
parser.add_argument("-c","--chridx", type=str,
                    help="path to the chromosome index file")
parser.add_argument("-g","--genome", type=str,
                    help="path to the genome fasta file")
parser.add_argument("-r","--repeat", type=str,
                    help="path to the repeat fasta file")
parser.add_argument("-t","--table", type=str,
                    help="path to the repeat table file")
parser.add_argument("-s","--seed", type=str, default="1",
                    help="seed value for simulation. default = 1")
parser.add_argument("-o", "--outdir", type=str,
                    help="output firectory")

args = parser.parse_args()
prefix = args.prefix
chr_index = args.chridx
genome_fa = args.genome
te_fa = args.repeat
te_table = args.table
seed = args.seed
outdir = args.outdir

print("\n")
print("#############################################")
print("### Prepare TEgenomeSimulator config file ###")
print("#############################################")
print(f"Using genome fasta file {args.genome}")
print(f"Using repeat fasta file {args.repeat}")
print(f"Output directory set as {args.outdir}")

# Generate chromosome dictionary
if chr_index:
    # Randome Genome Mode using chromosome index table
    df = pd.read_csv(str(chr_index), sep=',', names=['chr_id', 'length', 'gc'])
    #rand_genome_lib_w_len = df.set_index('chr_id')[['length', 'gc']].to_dict()
    rand_genome_lib_w_len = df.set_index('chr_id').to_dict('index')

elif genome_fa:
    # Custome Genome Mode using genome fasta file
    genome_lib = SeqIO.to_dict(SeqIO.parse(genome_fa ,"fasta"))
    cust_genome_lib_w_len = {}

    for seq_id, seq_record in genome_lib.items():
        length = len(seq_record.seq)  # Get the length of the sequence
        cust_genome_lib_w_len[seq_id] = {
            'sequence': seq_record,
            'length': length
            }

# Create the config file
final_out = outdir + '/TEgenomeSimulator_' + prefix + '_result'
yml_name = 'TEgenomeSimulator_' + prefix + '.yml'
#os.chdir(Path(outdir, "TEgenomeSimulator_" + file_prefix + "_result"))
#table_out = open(Path(final_out, "TElib_sim_list.table"), "w")
config_out = open(Path(final_out, yml_name), 'w')
if chr_index:
    # Generate config file for Randome Genome Mode
    config_out.write(''.join(['prefix: "', str(prefix), '"\n', 
                              'rep_fasta: "', str(te_fa), '"\n',
                              'rep_list: "', str(te_table), '"\n',
                              'seed: ', str(int(seed)), '\n',
                              'chrs:\n'
                              ]))
    i = 0
    for chr_id, data in rand_genome_lib_w_len.items():
        chr_len = data['length']
        gc_ctn = data['gc']
        config_out.write(''.join(['  ', str(chr_id), ':\n',
                                 '    prefix: "', str(chr_id), '"\n',
                                 '    seq_length: ', str(chr_len), '\n',
                                 '    gc_content: ', str(gc_ctn), '\n'
                                 ]))
        i += 1
    config_out.close()
elif genome_fa:
    # Generate config file for Randome Genome Mode
    config_out.write(''.join(['prefix: "', str(prefix), '"\n',
                             'genome_fasta: "', str(genome_fa), '"\n',
                             'rep_fasta: "', str(te_fa), '"\n',
                             'rep_list: "', str(te_table), '"\n',
                             'seed: ', str(int(seed)), '\n',
                             'chrs:\n'
                             ]))
    i = 0
    for chr_id, data in cust_genome_lib_w_len.items():
        chr_len = data['length']
        config_out.write(''.join(['  ', str(chr_id), ':\n',
                                  '    prefix: "', str(chr_id), '"\n',
                                  '    seq_length: ', str(chr_len), '\n'
                                 ]))
        i += 1
    config_out.close()

print(f"Generated the config file for simulation. File saved as {outdir}/TEgenomeSimulator_{prefix}.yml")
print("\n")