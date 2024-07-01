Lab 1
Peter Sullivan
7/2/24

This project enables users to convert from from Postfix to Prefix and Infix and Prefix to Postfix and Infix using the command line. In order for thes package to work make sure you are in the location of this readme document. Open up the cmd line and call on the package using pythons modular ability. This module takes in four arguments: Inpath, Outpath, input type and output type. Inpath and Outpath are realitve to the location you are running the cmd line from. Here are the valid input and output types: 'Prefix','Postfix','Infix'.

For this lab we are required to convert from prefix to postfix. My enhancement to enabling additional conversion as mentioned above. To test case from Prefix to Postfix this is an example cmd line request:

python -m lab1 resources/Required_Input.txt output/output.txt Prefix Postfix

Feel free to swap the paths as desired, and make sure to choose the correct input and output types when running.

Next I will walk through each step of the program in the order that it runs.


__init__.py

This runs every time the package imported. This will allow users to use the function proccess input file function if they desire to use the cabalities of this project.


__main__.py

When we run the cmd line as shown above. This is the first file that the module will run. I first import the Path method from pathlib, argpase and the proccess input file function from the lab1_functions script.

I then initalize an Argument parser using the argparse package. I then add four arguments that will enable the user to input from the command line in order to run this project. I then use the parse_args method to set up a args object. Finally I create the four variables using the args object, inpath, outpath, input type and outputy type. I also specify that infile and outfile are paths using the path method from the pathlib class.

Finally, I call on the process_input_file function to process our inputs that the user has inputted via the cmd line.


lab1_functions.py

I first import the Expression Class from expression script. I then create a function called process input file that takes in four arguments, input, output, input type and output type. I then initalize an empty list called processed data. Then using the input file, I initiate an varable called reader using pythons open method. I open the file in reader method.

I then use a while loop that is set to true. This while loop will only break when something is false or the break clause is called. I then read in the first line using the readline method and the strip method. The strip method removes black space from the right and left of the line. I then use the replace method to remove any blanks spaces inside the input as well changing carrots to the $ as expected. I then use an if clause to  check if the line is a blank string. If so the while loop breaks. If not, we then head to the try except block.

In the try block I first create a Expression object using the expressions class which takes in the input from the readline and the inputed type. I then set up a if clause to check the output type. This tells us which method to call on the expresion object. So if we are using a prefix to postfix object. Then the method called would be to post fix. This returns the postfix string. I then append the processed data with a list containing the input string and the output string. If the try fails, we then append the proccessed data list with the input string and an error as unknown, as this error was not planned for. We loop through each line in the input file.

After the while loop I then use the open function to open the output file in writer mode and iniate the writer variable. I then iniate an index as the integer 1. Next I loop through each item in the processed data list. For each item in the list, I print out the test case number (index), the inputtype as well as the input string, the output type and finally the output string. I then increment the index by 1. We loop through each item in the proccessed data list then close the file.


expressions.py

This class creates an expression object that does most of the work required when converted from one expression to the next.

I first imported the StackArray class from stack.py and the Operands class from the operand.py scripts. I then iniatillized the instance variables string and input type. I also created a quick check on the input type by initiating a list called valid_types. If the type is not in valid types, then the program will spit out an error, asking for correct types. 

Next I created a method called to_post_fix which checks to see the input type. If prefix, we call the pre to post function. If infix, I print out an error. The program does not currently support infix to postfix. This will be a future enhancement. The final clause returns the string since converted from post fix to postfix requires no modification.

The to prefix and to infix methods work in the same way as to postfix.

Next, I iniatiate an list of operators.

The next method I created is the pre to post method. This method converts from prefix to postfix. I will only need to go through one of the four conversion methods. They are all very similar, the only difference is that some require looping through the inverse or inversing the string on return.

For pre to postfix, I first initialize and empty stack object using the stackarray class. I then loop through each character in the inputed string but in reverse using the reverse order method. I then check if the character is in the operators list, if not, I push the character onto the stack. If the character is in the operators list, I then pop the two top items. I then create a operand object using the Operands class, using the two popped items, the operator, and a string that tells that operand how to handle the combine operation. I then have a if clause to check if the combine operands method returns none type. If it does, this means that we have the inccorect number of operands. That message will be returned as the final output in our output file.
If not, then we push the result of calling the method combine_operands(). Before returning the string that has been converted, I implement a if clause to check to see if the stack length is >1. This means that we did not have enough operators in the input string. This would also be returned to the output file if that is the case. Other wise we pop the stack which should contain the converted string.

The final method is the reverse_order method which takes a string. This method first iniatilizes an empty stack using the stack array classs. Then loops through each character string and pushes onto the stack. I then intiazlize an empty string. I then use a while loop to check if the stack is empty, if not we pop the stack and add that to the empty string. Finally we return the reveresed string.


stack.py

For this script, I create a class called StackArray. This class was called multiple times in the expressions.py script. This class is meant to mimic a stack object using pythons built in list. I first initiatie the class instance variables. For this one, we take no input, and it creates an empty list called stack.

I then created multiple methods to mimic a stacks methods. The first method is the empty method. This method checks to see if the length of the list ==0 using the len function. If so return True, otherwise return false.

The next method is the peek method. This method first checks to see if the stack is empty. We can't peek an elment on an empty stack or list. If the stack is empty, we print the stack is empty. Otherwise, I return the value of the last element in the list(top of the stack) using the indices and the len function.

The next method is the pop method. We first check to see that the stack empty, if not i create a variable called item which references the last item in the list (top of stack). I then use indices to slice the stack and exclude the last item from the stack. I then return the final item that was popped off the stack.

The next method is the stack length method. This method using the len function to return the length.

the final method is the push method. This method takes in a item and uses pythons built in function append to push the item to the top of the stack or the end of list.


opperand.py

The expressions.py script also called on the operands class. This script creates the class Operands. This class creates an Operand object using two operands, a operator, and the input type. Which is bassically just combining operands and operators into a string.

I first inialize the class instance variables. I then create a method called combine operands. This method using the type to call on the methods below. For example, if the type is Pre_Post ( which means converting from Prefix to Postfix) we then return the result from the combine_post and Prefix method.

The next method is the combine post and prefix method. This method first checks to see if the check for None method is False, If so, we then create a string called combined which is the operators and operands combined in the order that prefix to post fix requires. We then return that string. If there is none type, we return None-Type, which is used by the expressions class to identify an error.

The next two combine methods are very similar to the method above, the only difference is the order that the operands are combined, and the to infix methods add in '('  ')' to the ends of the combined operators and operands.

The final method is the check for none, this just checks to see if the operands or operators are none, if so return true, otherwise false.






