# Import Files
from pathlib import Path
import argparse
from Lab3.lab3_functions import process_main

# Set up Parser to receive 4 different inputs via command line
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("freq_table", type=str, help="Huffman Frequency file")
arg_parser.add_argument("encoded", type=str, help="Encoded string")
arg_parser.add_argument("clear_text", type = str, help = "Clear text to be encoded")
arg_parser.add_argument('out_path',type = str, help = "outpath of filename")
arg_parser.add_argument("traversal_type", type = str, help = "picks the type of Tree printed", default= 'Pre', nargs= '?')
args = arg_parser.parse_args()


freq_table = Path(args.freq_table)
encoded = Path(args.encoded)
clear_text = Path(args.clear_text)
out_path = Path(args.out_path)
traversal_type = args.traversal_type




# Call On the main function from lab1_functions that proccesses the input file and prints to desired output to a single .txt
process_main(freq_table,encoded,clear_text,out_path,traversal_type)

