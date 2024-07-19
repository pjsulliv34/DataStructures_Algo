# Import Expressions class
from Lab2.expressions import Expressions


# This method will process the input file based on input type and desired output type and then output
# the data into the output file at the desired location
def process_input_file(input,output,input_type,output_type):

    # Initialize and Empty list
    Processed_data = []

    # Open up the input file in reader mode
    with open(input,'r') as reader:

        # While loop that will stay open until the break close below
        while True:

            # Read in the first line and strip white space from the right and left
            line = reader.readline().strip()

            # Replace any white space in between operators and characters with emtpy string
            line = line.replace(' ', '')

            # Replace carrot operator with desired $
            line = line.replace('^','$')

            # Clause to check if the line is empty, if so break the while loop
            if line == '':
                break
                
            # Try clause to process the line in the input file
            try:
                
                # Create an expression object using the Expressions Class
                print(f'line {line}\n')
                expression_object = Expressions(line,input_type)
                
                # If Else clause to check what is the desired output. Desired output will determine which clause to run
                if output_type == 'Postfix':
                    print('running to Postfix')
                    
                    # Create desired output string using expression object method
                    output_expression = expression_object.to_post_fix()

                    # Append Input and output to the processed data list
                    Processed_data.append([line,output_expression])

                elif output_type == 'Prefix':
                    output_expression = expression_object.to_pre_fix()
                    Processed_data.append([line,output_expression])
                else:
                    output_expression = expression_object.to_infix()
                    Processed_data.append([line,output_expression])

            # Except clause to catch any errors that are not planned
            except Exception as e:
                print(e)
                Processed_data.append([line,'Unknown Error'])
                     
    # Open up output file in writing mode
    with open(output, 'w') as writer:

        # Initialize Index at 1
        index = 1

        # Loop through process data list
        for line in Processed_data:

            # Write to the output file using the write method and fstring
            writer.write(f"Testcase {index}\n {input_type}: {line[0]}\n {output_type}: {line[1]}\n")

            # Increment index by 1
            index +=1
