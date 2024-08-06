# Import Expressions class
#from Lab2.expressions import Expressions
from Lab3.tree_node import TreeSearch
from Lab3.huffman import Huffman

# This method will process the input file based on input type and desired output type and then output
# the data into the output file at the desired location


def process_main(freq_type,encoded,clear_text,outpath,test_case):
    freq_table = process_files(freq_type,'freq')
    print(freq_table)
    encoded = process_files(encoded,'encoded')
    print('encoded')
    print(encoded)
    print(len(encoded))
    clear_text = process_files(clear_text,'clear')
    print(clear_text)


    tree_list = []
    for value in freq_table:
        tree_list.append(TreeSearch(value[1],value[0]))
        
    
    huffman_ob = Huffman()
    reverse_sorted = huffman_ob.sort_priority(tree_list)
    print(reverse_sorted)
   
    huffman_tree = huffman_ob.build_Huffman_tree(reverse_sorted)
    print(huffman_tree)

    
    pre_order_traversal = huffman_ob.preOrderTraversal(huffman_tree)
    print(pre_order_traversal)
    
    huffman_code = huffman_ob.get_huffman_codes(huffman_tree,huffman_list=[])
    print(huffman_code)

    

    with open(f'{outpath}.txt','w') as writer:

        print(f'Test Scenario : {test_case}')

        # print('PreOrder Traversal of Huffman Tree')
        writer.write('PreOrder Traversal of Huffman Tree\n')
        print(f'len of pre {len(pre_order_traversal)}')
        for line in pre_order_traversal:
            print(line)
            writer.write(f'{line}\n')

        writer.write(f'\nDecoding Messages----------\n')

        for encoded_message in encoded:
            decoded = huffman_ob.decode_huffman(encoded_message,huffman_code)
            print(decoded)
            writer.write(f"Encodings  \n input: {encoded_message}\n output: {decoded}\n")

        writer.write(f'\nEncoding Messages\n')
        for clear in clear_text:
            print('clear')
            print(clear)
            encoded = huffman_ob.encode_huffman(clear,huffman_code )
            writer.write(f"Decodings  \n input: {clear}\n output: {encoded}\n")
    
    
   
    
    
def process_files(input,type):
    processed_data = []
    # Open up the input file in reader mode
    with open(input,'r') as reader:

        # While loop that will stay open until the break close below
        while True:

            # Read in the first line and strip white space from the right and left
            line = reader.readline().strip()
            print(line)
            

            # Replace any white space in between operators and characters with emtpy string
            line = line.replace(' ', '')

            # Clause to check if the line is empty, if so break the while loop
            if line == '':
                break
                
            # Try clause to process the line in the input file
            if type =='freq':
                try:
                    #print(line)
                    split = line.split('-')
                    processed_data.append([split[0],int(split[1])])
                except Exception as e:
                    print(e)
            elif type == 'encoded':
                processed_data.append(line)
            else:
                processed_data.append(line)

        return processed_data
           
