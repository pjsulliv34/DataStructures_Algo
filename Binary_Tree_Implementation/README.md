Lab 3
Peter Sullivan
8/6/2024

This project enables users to perform huffman encoding using an inbuilt class called Huffman. By inputting 4 inputs freq_table, encoded, clear_text and an outpath, the program will read in the three input files, freq, encoded data, and clear text data. The fifth argument is defaulted to pre order traversal, but can be inputed if the user wants to print a different traversal type. The program will then build a huffman tree using the frequency data. Utilizing that huffman tree, the program will then create a huffman code by traversing the tree and assigning 1's and 0's. Next the program will use that huffman code to decode the encoded data and encode the clear text data. Writing both to the output file.

For my enhancement, I added in two additional functions post order traversal and in order traversal. These are methods that can be used when importing the package. I also added in added in an additional args argument that takes in the traversal type. The argument is defaulted to prefix and is not neccessary to add, but if added, the user can specify the traversal type desired. Post, Pre and In. The text in the output file will also change based on the traversal type specified.

 If users want to use this package from the command line. They will need to input four different arguments in the command line. 

•   Freq Table Path
•   Encoded Text Path
•   Clear Text Path
•   Output Path
•   Traveral Type

Here are the examples Calls to the program:

python -m Lab3 resources\FreqTable.txt resources\Encoded.txt resources\ClearText.txt output\Output.txt
python -m Lab3 resources\FreqTable.txt resources\Encoded.txt resources\ClearText.txt output\Output2.txt 
python -m Lab3 resources\FreqTable.txt resources\Encoded.txt resources\ClearText.txt output\Output2.txt Post
python -m Lab3 resources\FreqTable.txt resources\Encoded.txt resources\ClearText.txt output\Output2.txt Pre
python -m Lab3 resources\FreqTable.txt resources\Encoded.txt resources\ClearText.txt output\Output2.txt In

Traversal Type will always default to Pre, and is not necessary as an input. 


__init__.py

This runs every time the package is imported. This will allow users to use the function process input file function if they desire to use the capabilities of this project.

__main__.py

When we run the cmd line as shown above. This is the first file that the module will run. I first import the Path method from pathlib, argparse and the process input file function from the lab1_functions script.

I then initialize an Argument parser using the argparse package. I then add four arguments that will enable the user to input from the command line in order to run this project. 

The freq_table specifies that location of the frequency table provided in a .txt file. The encoded and clear text are processed the same way. The out_path is used to specify the location of the text file. For all four arguments, I use the Path Method. I then bring in the Traversal type as an argument, with the default of Pre.

Finally, I call on the process_main function to process our inputs that the user has inputted via the cmd line.

lab3_functions.py

This script first imports the Huffman class from the huffman.py script.

I then created a method called process main which takes in four inputs specified from the cmd line. I then read in the three tables using the process file’s function. I then initialize an empty list. Using the frequency table List, I loop through each element and create a treenode using the Huffman class.

Next, I initialize an empty Tree object. I then use that empty tree objects method called sort Priority to sort the list of tree nodes based on priority desired for this assignment. Next, I build a huffman tree using the huffman method and inputting the sorted tree node list. I then create an object that represents the Preorder Traversal of the Huffman tree. I use an if clause to check the traversal type. The function is defaulted to Pre, but it will run the other types if chosen. If a type is chosen that is not expected we will print an error.

This is a list of nodes. I then grab the huffman codes using the get huffman codes method. 

Next, I open the output file as a .txt. I thenn write the traversal type and then I loop through the order traversal list and write each item to the output file. I then loop through each line in the encoded files and decode the string using the decode huffman method. I then write the message and decode the output.

I put in a try except, to catch any errors on each line of the encoding. This will print the error, not write the error to the output file. This can be modified to write to the file if desired. I then perform the same loop for lines in the clear text, but instead of using the decode huffman, I use the encode huffman method.

The next function is the process files function. This takes in an input and a type. I first initialize an empty list. I then open the input file in reader mode. I then loop through until the while loop breaks. I read through each line item stripping out blank spaces. If the line is blank, the program will then break the loop.

I then use an if clause to check which type of file we are processing. If its a freq type, we then need to split and append the items in a nested list. Otherwise we can append the line item a string to the processed list. I use try except clauses to check for errors while reading in each file.

huffman.py

This program is used to create the class Called Huffman. This class can be used to create tree nodes, or to perform huffman encoding. The class first creates 4 class instance variables. We have an additional instance variable called char that is needed for huffman encoding.

I then create a method called build huffman tree. This method takes in a sorted list of nodes. For best accuracy, it is recommended that the nodes are presorted before pushing to this method. I then use a while loop to check if the length of the sorted nodes list is greater than 1. If so, we pop the first two items in the list. I then combine the values of each node and the characters of each node. I then create a parent node using the Huffman class and inputting the new val, char, and the left and right nodes as children. I then append the new single node back on the list. I then sort the sorted nodes list again before the next iteration. When the sorted list is less then 2, the loop breaks and returns the tree node.

I then create another method called get huffman codes. This method first uses an if clause to check if we are at a leaf node. A leaf node will have no children on the left or right side. If so, then we append the huffman list. If that is not the case, we then use a recursive call to call the get huffman codes method inputting the left or right node depending on which node is not none, the current huffman list and the current prefix. As left children get priority, we always check the left if clause before the right if clause. We then return the nested list containing the huffman codes.

The method I create is called sort priority. This is one of the most important functions. If this is working incorrectly, the program will not decode correctly. I first initialize an empty list called stack and a list containing the alphabet. I then use a while loop to check if the inputted list is empty.
I then pop the item from the list. Initialize an empty stack and two indexes at 0. 
I then use two for loops. The first loops through the alphabet list and increments the current index until we reach the index of the alphabet. The next loop first checks if the stack is empty, and if not then grabs the location of the alphabet for the item on top of the stack.

I then use a while loop to append the temp stack with the current stack top, if the current item is greater than the stack value, or if the values match, and current char length is greater than the current char length or if both the char lengths and the values match, we check to see if the current index in the alphabet is greater than the stack index in the alphabet.

This then appends the stack with the current item. I then empty the temp stack back into the main stack, before iterating through the next node. This then returns the node list in the desired priority as requested in the assignment.

I then created a method called encode huffman. This method takes in a string and a huffman code. We first initialize an empty string called final. I then loop through each character in the string. I then loop through each item in the huffman code comparing the lowercase versions of both. If we get a match, we then add the encoded binary to the final output. We then return the output after going through each character.

The next method is the decode huffman method. This method reads in a binary string and the huffman code. We initialize two empty strings, final and tempchar. I then loop through each bit in the binary string. I then add that bit to the temp char string. I then loop through the codes to check if we have a binary match. If not, I then add another bit to the temp string and keep adding until we get a match. If we get a match, temp is cleared and we keep processing the bits until the code is processed. We return the decoded string.

The final method is the Preorder Traversal method. This method takes in a tree node object. This method first checks to see if the output is none, if so, we initialize an empty list. I then create a base case to check if the node is Node None. If that’s the case we return the output list. If not, we then append the output list with the node value and corresponding characters. I then recursively call the function again with the left and the right children, and passing in the output list. Since this is pre order traversal, we call the left child first before calling the right child.


