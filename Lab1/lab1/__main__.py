# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m proj0'. This file is NOT run during
# imports. This whole file is basically the java equivalent of:
# public static void main(string args[]), or c's int main();

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse
from lab1.lab1_functions import process_input_file

# Argument parser is an amazing tool. It's worth mastering
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
arg_parser.add_argument("input_type", type = str, help = "Input type")
arg_parser.add_argument("output_type", type = str, help = "Output type")
args = arg_parser.parse_args()

# pathlib.Path is also a fantastic built in tool and has a lot of great
# features. Please look it up! I promise it's worth it.
in_path = Path(args.in_file)
out_path = Path(args.out_file)
input_type = args.input_type
output_type = args.output_type

process_input_file(in_path,out_path,input_type,output_type)
print(args)
