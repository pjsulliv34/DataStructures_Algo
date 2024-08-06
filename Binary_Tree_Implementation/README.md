Lab 2
Peter Sullivan
7/23/24

This project enables users to convert from Postfix to Prefix and Infix, and Prefix to Postfix and Infix using the command line. In order for the package to work make sure you are in the location of this readme document. Open up the cmd line and call on the package using pythons module ability. This module takes in four arguments: Inpath, Outpath, input type and output type. Inpath and Outpath are relative to the location you are running the cmd line from. Here are the valid input and output types: 'Prefix','Postfix','Infix'. The final two arguments are optional and default to:

•   Input type : Prefix
•   Output type: Postfix

For this lab we are required to convert from prefix to postfix. My enhancement to enabling additional conversion as mentioned above. To test case from Prefix to Postfix this is an example cmd line request:

python -m lab2 resources/Required_Input.txt output/output.txt Prefix Postfix
python -m lab2 resources/Required_Input.txt output/output.txt 

The default is from prefix to postfix, so there is no need to enter the last two arguments if we are just converting from Prefix to Postfix.

Feel free to swap the paths as desired, and make sure to choose the correct input and output types when running.

Next, I will walk through each step of the program in the order that it runs.

__init__.py

This runs every time the package is imported. This will allow users to use the function process input file function if they desire to use the capabilities of this project.

__main__.py

When we run the cmd line as shown above. This is the first file that the module will run. I first import the Path method from pathlib, argpase and the process input file function from the lab1_functions script.

I then initialize an Argument parser using the argparse package. I then add four arguments that will enable the user to input from the command line in order to run this project. The input type and output type are optional and have defaults if they are not added to the cmd line call. I then use the parse_args method to set up an args object. The two final arguments are optional. They will default to input type prefix and output type postfix. Finally, I create the four variables using the args object, inpath, outpath, input type and outputy type. I also specify that infile and outfile are paths using the path method from the pathlib class.

Finally, I call on the process_input_file function to process our inputs that the user has inputted via the cmd line.

lab2_functions.py

I first imported the Expression Class from expression script. I then create a function called process input file that takes in four arguments, input, output, input type and output type. I then initialize an empty list called processed data. Then using the input file, I initiate a variable called reader using pythons open method. I open the file using the open method and name the variable reader.

I then use a while loop that is set to true. This while loop will only break when something is false or the break clause is called. I then read in the first line using the readline method and the strip method. The strip method removes black space from the right and left of the line. I then use the replace method to remove any blanks spaces inside the input as well changing carrots to the $ as expected. I then use an if clause to check if the line is a blank string. If so the while loop breaks. If not, we then head to the try except block.

In the try block I first create an Expression object using the expressions class which takes in the input from the readline and the input type. I then set up a if clause to check the output type. This tells us which method to call on the expression object. So if we are using a prefix to postfix object. Then the method called would be to post fix. This returns the postfix string. I then append the processed data with a list containing the input string and the output string. If the try fails, we then append the processed data list with the input string with the error using the Exception object for that particular and unknown error.  We loop through each line in the input file.

After the while loop I then use the open function to open the output file in writer mode and initiate the writer variable. I then initiate an index as the integer 1. Next, I loop through each item in the processed data list. For each item in the list, I print out the test case number (index), the input type as well as the input string, the output type and finally the output string. I then increment the index by 1. We loop through each item in the processed data list then close the file.

expressions.py

This class creates an expression object that does most of the work required when converted from one expression to the next.

I first import the Operands class from the operand.py scripts. I then initialized the instance variables string and input type. I also created a quick check on the input type by initiating a list called valid_types. If the type is not in valid types, then the program will spit out an error, asking for correct types. 

Next I created a method called to_post_fix which checks to see the input type. If prefix, we call the pre to post function. If infix, I print out an error. The program does not currently support infix to postfix. This will be a future enhancement. The final clause returns the string since converted from post fix to postfix requires no modification.

The to prefix and to infix methods work in the same way as to postfix.

Next, I initiate a list of operators.

The next method I created is the pre to post method. This method converts from prefix to postfix recursively by recursively processing each character in the prefix string and modifying the postfix list/string on each call. I will only need to go through one of the four conversion methods. They are all very similar, the only difference is that some require looping through the inverse or inversing the string on return.

For pre to postfix, the method takes the self keyword, and two other keyword arguments postfix, and index respectively. If postfix and index are not inputted, they will be defaulted to None for postfix and 0 for index.
Next, I put an if clause in to check if postfix is equal to None, if so, then that means we are in the first call of the method. If it is the first call to the method, then we initialize an empty list called postfix. I then use an if clause to check if the index is >= length of the string as the base case of the recursive function. This means we have processed every character, and we can now return the result. Within the base case, I put a final check to check if the postfix list has more than 1 element. If that is the case, then will return the error. If that is not the case, then we can return the 1 element in the postfix list, using the pop list function. Next is the meat of the recursive function. We first grab the current element in the reversed string using the inputted index. To reverse the string, I use the reverse order method, which I will explain later on. If that element/character is not in the class variable operators, then we can append the postfix list with that character and increment the index by 1. We then call the pre_to_postfix function again with our current postfix list and index. If the character is in the class variable operators, we then move to the else clause. With in the else clause, I first use an if clause to check if the length of the postfix list is less than 2. If so, I return the expected error. If not, I then pop the first two elements from the postfix list. I then create an operand object using the Operands class, and the two items from the postfix list, the current character, and the expected keyword for the operands class. For this method, 'Pre_Post' is expected. For more information on this, see the operand.py explanation below. I then append the postfix list with the result of the operand.combine_operands method. I then increment the index by 1.  Finally, I call the pre_to_post method again with the current postfix list and index. This process will continue until the base case clause is True.

The final method is the reverse_order method which takes that self keyword and a string to recursively process and return the reversed order of the string. I use an if clause as my base case to check if the string length is 0, if so, return the string. If the base case is not satisfied, I then return the final element in the string concatenated with the call of the reverse_order method, with the current string with out its final element. This process will continue until the base case.

opperand.py

The expressions.py script also called on the operands class. This script creates the class Operands. This class creates an Operand object using two operands, an operator, and the input type. The class takes these inputs and combines them based on the input type.

I first initialize the class instance variables. I then created a method called combine operands. This method uses the type to call on the methods below. For example, if the type is Pre_Post ( which means converting from Prefix to Postfix) we then return the result from the combine_post and Prefix method.

The next method is the combine post and prefix method. This method first checks to see if the check for None method is False, If so, we then create a string called combined which is the operators and operands combined in the order that prefix to post fix requires. We then return that string. If there is none type, we return None-Type, which is used by the expressions class to identify an error.

The next two combine methods are very similar to the method above, the only difference is the order that the operands are combined, and the to infix methods add in '('  ')' to the ends of the combined operators and operands.

The final method is the check for none, this just checks to see if the operands or operators are none, if so return true, otherwise false.






