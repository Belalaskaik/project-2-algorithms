Project 2 Algorithm 1
This program takes input arrays of cities and finds the common cities between them. It then outputs the order in which the cities appear in the original string for each input array, along with the list of cities in alphabetical order.

Requirements
This program requires Python 3.

Usage
1.To run the program, follow these steps:

Place the input arrays in a text file, one array per line, in the following format:
array 1a = [city1city2city3...]
array 1b = [city4, city5, city6, ...]
array 2a = [city7city8city9...]
array 2b = [city10, city11, city12, ...]

2.Save the file as input.txt in the same directory as the Python script.

3.Run the script by typing the following command in the terminal:
    python project2_algorithm1.py

4. The program will output the order and list of common cities for each input array to the terminal.
Example:
Suppose we have the following input arrays in in2a.txt:
array 1a = [sanoaklandrialtofullertonmarcolongbreacoronamodestoclovissimithousand]
array 1b = [brea, modesto, clovis, corona]

array 2a = [marcopolmonafremontrialtofullertonmarcolongfresnochinoclovissimisalinas]
array 2b = [fullerton, chino, fremont, fresno]

array 3a = [torranceoaklandrialtomarcooxnardchinofresnoirvineclovissimiorange]
array 3b = [oxnard, irvine, orange, marco]

Running the program using the above steps will produce the following output:
Output Order 1: [34, 44, 51, 38] 
Output Array 1: ['brea', 'corona', 'modesto', 'clovis']

Output Order 2: [25, 49, 12, 43] 
Output Array 2: ['fremont', 'fullerton', 'fresno', 'chino']

Output Order 3: [26, 43, 59, 21] 
Output Array 3: ['marco', 'oxnard', 'irvine', 'orange']


This indicates that for the first input array, the cities appear in the order brea, corona, modesto, clovis in the original string, and the common cities are brea, corona, modesto, and clovis. 
For the second input array, the cities appear in the order fremont, fullerton, fresno, chino, and the common cities are fremont, fullerton, fresno, and chino. 
For the third input array, the cities appear in the order marco, oxnard, irvine, orange, and the common cities are marco, oxnard, irvine, and orange.