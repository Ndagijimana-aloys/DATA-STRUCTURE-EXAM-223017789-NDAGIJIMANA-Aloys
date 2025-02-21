Example 1: Basic "Hello, World!" Program
Every C++ program must have a main() function, which serves as the starting point for execution. The #include <iostream> directive allows input and output operations, such as displaying text on the screen. The using namespace std; statement simplifies coding by eliminating the need to prefix standard functions with std::. The cout statement prints "Hello, World!" to the console, and return 0; indicates that the program executed successfully.
________________________________________
Example 2: Understanding Variables in C++
A variable is a named storage location in memory that holds a value. In C++, variables must be declared with a specific data type, which determines the kind of values they can store.
For example:
•	int (integer) stores whole numbers like 10, 25, or -5.
•	A variable name (such as age) uniquely identifies the storage location.
•	The assigned value (e.g., 25) is stored in the variable and can be used throughout the program.
________________________________________
Example 3: Common Data Types in C++
C++ supports multiple data types for different kinds of values:
•	int: Stores whole numbers (e.g., 30).
•	float: Stores decimal numbers with single precision (e.g., 3.14).
•	double: Stores decimal numbers with higher precision (e.g., 3.1415926535).
•	char: Stores a single character (e.g., 'A').
•	bool: Stores boolean values (true or false).
•	string: Stores text (e.g., "Alice"). This requires including the <string> header.
These data types allow a program to handle different types of information efficiently.
________________________________________
Example 4: Variable Declaration and Output Statements
In C++, variables must be declared before use.
•	Assigning values to variables at the time of declaration is called initialization.
•	cout is used to display variable values on the screen.
•	The endl manipulator moves the output to a new line.
For example:
•	Declaring int age = 20; means the variable age stores the value 20.
•	double price = 19.99; stores a decimal number.
•	char grade = 'A'; stores a single character.
•	string name = "Alice"; stores a sequence of characters.
Using cout << "Age: " << age << endl; prints the value stored in age.
________________________________________
Example 5: Taking User Input
C++ programs often need to accept user input at runtime.
•	The cin object is used to take input from the keyboard.
•	It reads data and stores it in variables.
•	The program can then process and display the entered values.
For example:
•	If the user enters "John" when prompted for their name, it gets stored in the variable name.
•	If they enter "25" when prompted for their age, it is stored in age.
•	The program then displays a message such as "Hello, John! You are 25 years old."
This interaction makes programs dynamic and useful.
________________________________________
Example 6: Basic Arithmetic Operations
C++ allows mathematical operations on variables.
•	Addition (+) computes the sum of two numbers.
•	Subtraction (-) calculates the difference between two numbers.
For instance:
•	If a = 10 and b = 3, then a + b results in 13, and a - b results in 7.
•	The calculated values can be displayed using cout.


