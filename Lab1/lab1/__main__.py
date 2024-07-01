# Import Files
from pathlib import Path
import argparse
from lab1.lab1_functions import process_input_file

# Set up Parser to receive 4 different inputs via command line
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
arg_parser.add_argument("input_type", type = str, help = "Input type")
arg_parser.add_argument("output_type", type = str, help = "Output type")
args = arg_parser.parse_args()


in_path = Path(args.in_file)
out_path = Path(args.out_file)
input_type = args.input_type
output_type = args.output_type


# Call On the main file from lab1_functions that proccesses the input file and prints to desired output
process_input_file(in_path,out_path,input_type,output_type)

