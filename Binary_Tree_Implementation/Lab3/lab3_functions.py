# Import Huffman Class
from Lab3.huffman import Huffman

# This method will process frequency table, encoded data, and clear text data.
# After processing the data, the processed data will be writen to the specified outpath.
def process_main(freq_type,encoded,clear_text,outpath):

    # Read in Data
    freq_table = process_files(freq_type,'freq')
    encoded = process_files(encoded,'encoded')
    clear_text = process_files(clear_text,'clear')
   
    # Initialize an Empty list
    tree_list = []

    # Loop through frequency table creating a TreeNode for each number/letter combination
    for value in freq_table:
        tree_list.append(Huffman(value[1],value[0]))
        
    # Initialize an Empty Tree Node
    huffman_ob = Huffman(None,None)

    # Set up Priority Queue for Tree Node list
    reverse_sorted = huffman_ob.sort_priority(tree_list)
    
    # Build Huffman tree utilizing Huffman method
    huffman_tree = huffman_ob.build_Huffman_tree(reverse_sorted)
  
    # Create a list object that represents the pre order traversal of the huffman tree
    pre_order_traversal = huffman_ob.preOrderTraversal(huffman_tree)
  
    # Grab the huffman codes from Huffman tree
    huffman_code = huffman_ob.get_huffman_codes(huffman_tree,huffman_list=[])
   
    # Open the Outpath file in writer mode
    with open(f'{outpath}','w') as writer:

        writer.write('PreOrder Traversal of Huffman Tree\n')
        
        # Loop through each line in the Pre Order Traversal of the Huffman tree
        for line in pre_order_traversal:
            writer.write(f'{line}\n')


        # Decoding Section
        writer.write(f'\nDecoding Messages----------\n')

        # Loop through encoded messages in Encoded file
        for encoded_message in encoded:

            # Decode the ecoded message using the Huffman code
            try:
                decoded = huffman_ob.decode_huffman(encoded_message,huffman_code)
                writer.write(f"Encodings  \n input: {encoded_message}\n output: {decoded}\n")
            except Exception as e:
                print(e)


        # Encoding Section
        writer.write(f'\nEncoding Messages----------\n')
        for clear in clear_text:
            
            try:
                encoded = huffman_ob.encode_huffman(clear,huffman_code )
                writer.write(f"Decodings  \n input: {clear}\n output: {encoded}\n")
            except Exception as e:
                print(e)
    
    
   
    
# Function to read in file based on file type
def process_files(input,type):

    # Initialize empty list
    processed_data = []

    # Open up the input file in reader mode
    with open(input,'r') as reader:

        # While loop that will stay open until the break close below
        while True:

            # Read in the first line and strip white space from the right and left
            line = reader.readline().strip()
        
            # Replace any white space in between operators and characters with emtpy string
            line = line.replace(' ', '')

            # Clause to check if the line is empty, if so break the while loop
            if line == '':
                break
                
            # Try clause to process the line in the input file
            if type =='freq':
                try:
                    split = line.split('-')
                    processed_data.append([split[0],int(split[1])])
                except Exception as e:
                    print(e)
            elif type in ('encoded','clear'):
                try:
                    processed_data.append(line)
                except Exception as e:
                    print(e)
            else:
                print('Unknown File')

        return processed_data
           
