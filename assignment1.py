#!/usr/bin/env python
# coding: utf-8

# # Computing 6 Assignment
# 
# 

# ---
# ## Background
# 
# In this assignment you will be implementing a portion of a Geographic Information System (GIS). A GIS is a computer system used to organize, categorize, and analyze geographical data in order to produce accurate depiction of the real world. The system uses multiple layers of information to achieve this task. The data layers are split into a grid and represented as a matrix with **m** rows and **n** columns where each entry in the matrix contains the type of land at that point on the map. An entry **A<sub>ij</sub>** is the *i*th row and *j*th column in our map matrix. We assume that **A<sub>00</sub>** is the first element in our matrix. The graphic below will assist in visualizing the process:
# 
# ![Comp6.png](attachment:Comp6.png)
# \begin{align}
#   \texttt{Figure 1}
# \end{align}
# 
# 
# As seen in the previous example, our GIS utilizes **6** different data layers. We call these layers the **map types** as they classify regions of different land on our map. Thus, each entry in our map matrix can be **one** of the 6 map types.
# 
# -	Transportation (T)
# -	Agricultural (A)
# -	Residential (R)
# -	Commercial (C)
# -	Water (W)
# -	Undeveloped land (U)
# 
# Our GIS will store the map information as a list of lists. If we have a list named **map**, then map[i][j] will store the map type at row i, column j. Each entry will contain a string that corresponds to 1 of the 6 possible map types listed above. The list representation of the map in **Figure 1** is shown below:
# 
# 
# ```
# [['A','A','A','A','U','U','U','U'],    
#  ['A','A','A','A','U','R','R','R'],    
#  ['W','W','W','W','T','T','T','T'],    
#  ['W','W','W','W','T','R','R','R'],
#  ['C','C','U','U','T','R','U','U'],    
#  ['T','T','T','T','T','T','U','U'],    
#  ['U','U','U','U','T','R','U','U']]
# ```
# 
# One usage of the system is to be able to easily identify whether or not a piece of land (entry in the map matrix) is deemed **commercially buildable**. A piece of land at **A<sub>ij</sub>** is deemed commercially buildable if the following conditions hold:
# -	The entry at **A<sub>ij</sub>** has map type **U**
# -	The entry **A<sub>ij</sub>** is not on the edges of the map (the first and last rows and columns).
# -	The entry **A<sub>ij</sub>** is not adjacent with an entry of map type **R** or map type **A**. Note that adjacent entries are entries to the top, bottom, left, and right of the current cell.
# 
# Based on the criteria and the map representation of **Figure 1**, it can be seen that **A<sub>4,2</sub>** is commercially buildable and **A<sub>1,4</sub>** is not commercially buildable. 
# 
# Please read the requirements below to implement the GIS system!
# 

# ---
# ## Additional Information
# When using a 2D list, we can access elements around a specific index. Given the element at location i,j we can find the adjacent element within the same row by changing the row index. If we want to access the element to the *left* of our selected element, we can subtract 1 from the j index. To access the element to the right, we can add 1 to the j index. To access the element in the previous row (above the element), we can subtract 1 from the i index. To access the element in the next row (below the element), we can add 1 to the i index.

# In[ ]:


x = [[1,2,3],
     [4,5,6], 
     [7,8,9]]
i=1
j=1
print(x[i][j])
print(x[i-1][j]) # above
print(x[i][j+1]) # right


# Be careful when accessing adjacent elements - if you try to access an element that doesn't exist, you might receive unexpected output, or an error!

# In[ ]:


print(x[i-2][j]) # 2 above - actually wraps around and gives us the element in row -1 (which is the last row)
print(x[i][j+2]) # 2 right - tries to access value in column 3 (which doesn't exist)


# ---
# ## NOTE THAT YOU WILL BE MARKED ON MULTIPLE ITEMS IN THIS LAB IN ADDITION TO THE FUNCTIONALITY OF YOUR CODE
#  - Variable Names
#  - Commenting
#  - General Legibility
#  - Reflective Questions

# ---
# ## Program Requirements (12 Marks)
# 
# Your GIS system will be comprised of a set of functions used to analyze the information of any given map. In addition, you will be creating a function used to determine whether or not a piece of land is commercially buildable. The requirements of the system are given below. Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks.
# 
# 1. Define a function **countType**(*map_data*, *map_type*):
#   - ***map_data***: A *list of lists* representing the data for a given map.
#   - ***map_type***: A *string* representing a map type ('T','A','R','C','W', or 'U')
#   - **Return:** An *integer* representing the number of times *map_type* occurs in *map_data*.
#   
#   
# 2.	Define a function **classifyMap**(*map_data*):
#   -	***map_data***: A *list of lists* representing the data for a given map.
#   -	**Return**: A map classification according to the following rules:
#           -	The *string* **Suburban** if the number of 'R' cells is greater than 50% of all cells.
#           - The *string* **Farmland** if the number of 'A' cells is greater than 50% of all cells.
#           - The *string* **Conservation** if the number of 'U' cells plus the number of 'W' cells is greater than 50% of all cells.
#           - The *string* **City** if the number of 'C' cells is greater than 50% of all cells and the number of 'U' cells plus the number of 'A' cells is between 10% and 20% of all cells (inclusive).
#           - The *string* **Mixed** if none of the above criteria are met.  
#           _(Hint, use your countType function coupled with the fact that the total cells in map\_data is given by m*n)_
#           
# 
# 3.	Define a function **isolateType**(*map_data*, *map_type*):
#   -	***map_data***: A *list of lists* representing the data for a given map.
#   -	***map_type***: A *string* representing a map type (‘T’, ‘A’, ‘R’, ‘C’, ‘W’, or ‘U’)
#   -	**Return**: A new *list of lists* that represent *map_data* as a matrix but all entries that **are not** equal to *map_type* are replaced with a string containing only a space (" ").  
#   
# 
# 4.	Define a function **commerciallyBuildable**(*map_data*, *i*, *j*):
#   -	***map_data***: A *list of lists* representing the data for a given map.
#   -	***i***: An *integer* representing a given row in *map_data*.
#   -	***j***: An *integer* representing a given column in *map_data*.
#   -	**Return**: **True** if *map_data[i][j]* is commercially buildable, otherwise **False**. (Refer to the background section to determine what is deemed commercially buildable)

# ---
# ## Implementation
# Please define all functions in the cell below

# In[1]:


# YOUR CODE HERE
def countType(map_data, map_type): #function for determining coutner values
    count = 0 #start coutner at zero
    for i in map_data: #loop for value i in list
        for j in i: # value j in value i
            if j == map_type: #if j is a string
                count += 1 #add 1 to current counter
    return count #return coutner value

def classifyMap(map_data): #function to determine map type
    rows = len(map_data) #rows are length of map_data list
    cols = len(map_data[0]) #columns are number of values in row
    total_count = rows * cols 
    half_count = (total_count)/2     
    classification = " "
    if countType(map_data, "R") > half_count: #if statement to determine the inital map classification
        classification = "Suburban"
    elif (countType(map_data, "A") > half_count):
        classification = "Farmland"
    elif (countType(map_data, "U") + countType(map_data, "W")) > half_count:
        classification = "Conservation"
    elif (countType(map_data, "C") > half_count) and ((countType(map_data, "U") + countType(map_data, "A")) 
        >= (total_count/10)) and ((countType(map_data, "U") + countType(map_data, "A")) <= (total_count/5)):
        classification = "City"
    else:
        classification = "Mixed" #if none, mixed
    return classification #return findings
    
def isolateType(map_data, map_type): #function to isolate the letters chosen
    new_list = map_data.copy() #copy of the map_data to be altered in a new list
    for i in range(0, len(new_list)): 
        for j in range(0, len(new_list[i])): 
            if new_list[i][j] != map_type: #if new list does not equal map_type string
                new_list[i][j] = " " #fills in area with nothing
    return new_list #returns the new makeup of the list

def commerciallyBuildable(map_data, i, j): #function to determine if commercially buildable
    rows = len(map_data) #len of map_data is row
    cols = len(map_data[0]) #len of map_data is length row is the column
    region = map_data[i][j] #find the region in question
    if (region == 'U') and (i != 0 and i != rows) and (j != 0 and j != cols): #determine the result and return
        if(map_data[i-1][j] != 'A' and map_data[i+1][j] != 'A' and map_data[i][j-1] != 'A' and map_data[i][j+1] != 'A'): #determines adjacency and outer edge
            if(map_data[i-1][j] != 'R' and map_data[i+1][j] != 'R' and map_data[i][j-1] != 'R' and map_data[i][j+1] != 'R'):
                return True
    else:
        return False


# ---
# ## Sample Output
# Unlike the other computing labs that required you to run main() to validate your code, these functions can act as stand-alone functions. You have been provided with some test cases, but you are encouraged to create more to thoroughly test your code.

# In[2]:


MAP = [['A','A','A','A','U','U','U','U'],
       ['A','A','A','A','U','R','R','R'],
       ['W','W','W','W','T','T','T','T'],
       ['W','W','W','W','T','R','R','R'],
       ['C','C','U','U','T','R','U','U'],
       ['T','T','T','T','T','T','U','U'],
       ['U','U','U','U','T','R','U','U']]

MAP2 = [['C','C','C','C','R','T','C'],
        ['T','T','T','T','T','C','C'],
        ['C','C','W','C','R','T','C'],
        ['C','C','C','W','U','T','C'],
        ['C','C','C','U','U','T','C'],
        ['C','C','C','C','C','U','C'],
        ['C','C','C','T','U','U','C'],
        ['C','T','C','T','U','A','C']]


# countType() and classifyMap() functions
print("The number of U spaces in MAP =",countType(MAP, 'U'))
print("The number of T spaces in MAP2 =",countType(MAP2, 'T'))
print("MAP Type =",classifyMap(MAP))
print("MAP2 Type =",classifyMap(MAP2))

# isolateType() function
print("-----------------")
print("Isolated MAP: U")
MA = isolateType(MAP,'U')
for row in MA:
   print(row)
print("-----------------")
print("Isolated MAP2: T")
MB = isolateType(MAP2,'T')
for row in MB:
   print(row)
print("-----------------")

# commerciallyBuildable() function
print("Is MAP commercially buildable at (4,2):",commerciallyBuildable(MAP,4,2))
print("Is MAP2 commercially buildable at (2,2):",commerciallyBuildable(MAP2,2,2))


# The expected output for the provided test cases is given below:
# ```
# The number of U spaces in MAP = 17  
# The number of T spaces in MAP2 = 12 
# MAP Type = Mixed 
# MAP2 Type = City  
# -----------------
# Isolated MAP: U
# [' ', ' ', ' ', ' ', 'U', 'U', 'U', 'U']
# [' ', ' ', ' ', ' ', 'U', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', 'U', 'U', ' ', ' ', 'U', 'U']
# [' ', ' ', ' ', ' ', ' ', ' ', 'U', 'U']
# ['U', 'U', 'U', 'U', ' ', ' ', 'U', 'U']
# -----------------
# Isolated MAP2: T
# [' ', ' ', ' ', ' ', ' ', 'T', ' ']
# ['T', 'T', 'T', 'T', 'T', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', 'T', ' ']
# [' ', ' ', ' ', ' ', ' ', 'T', ' ']
# [' ', ' ', ' ', ' ', ' ', 'T', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', ' ', 'T', ' ', ' ', ' ']
# [' ', 'T', ' ', 'T', ' ', ' ', ' ']
# -----------------
# Is MAP commercially buildable at (4,2): True  
# Is MAP2 commercially buildable at (2,2): False
# ```

# ----------
# ## Code Legibility (6 Marks)
# Your code will be marked on commenting and code legibility.<br>
# The mark breakdown is as follows:<br>
# > 2 marks for using appropriate variable names that indicate what is being stored in that variable<br>
# 2 marks for leaving comments on major parts of your code such as where you read the file or calculate a summation<br>
# 2 marks for general legibility. The TA's should be able to understand your code without spending hours reading it. For example do not put your code in one very long line as this is hard for someone else reading your code to understand

# ---
# ## Test Plan
# Develop a test plan for your program. Your test plan should have at least three test cases: one normal case, one boundary case, and one abnormal case. You can test any function but you must test **at least two different** functions. Please use the following format for your test cases:
# 
# **Function:**   
# **Input:**  
# **Output:**  
# **Excepted Output:**  
# **Pass/Fail:**  
# 
# An example test case is shown below:  
# ```
# Function: countType(map_data,map_type)
# Input: map_data = [['U','T','U','A'],
#                     ['R','T','W','A'],
#                     ['U','T','A','W']]  
#        map_type = 'U'
# Output: 3
# Excpected Output: 3
# Pass/Fail: Pass
# ```
# 
# Implement your testing plan in the cell below! 

# ```
# DOUBLE CLICK TO EDIT THIS CELL. DO NOT DELETE QUOTATION MARKS
# ```

# ---
# ## Reflective Questions (6 Marks)
# 
# 1. Which functions did you use a nested structure (nested loops, nested conditionals, etc) to implement the requirements? Would it have been possible to implement them without using a nested structure? Which functions did you *not* use a nested structure? Would it have been possible to implement them *with* a nested structure?  
# 
# 
# 2. Suppose we wanted to create an additional map classification called 'Urban City' which is indicated by the number of 'R' cells plus the number of 'C' cells being between 60% and 80%. Can we do this? How might this affect our classifyMap() function?
# 
# 
# 3. How many test cases would you need to confirm that your classifyMap() function correctly identifies a "Farmland" map? Explain what your test cases would be.

# ```
# 1. I used nested loops in the first function. The second function I did not use any nested structures, but I potentially could have for the elif statements to state my conditionals. The third function has a nested loop statement. The fourth function has a nested if statement. These functions are able to be done without the nested statements, but would use either more code or would be less efficient code.
# 2. This is possible, but you would need to add a variable that is between 60 and 80. It would be the same as any other classification just with different parameters that classify what type of map it is. This will just add another section to our nested if statement under the classifyMap() function.
# 3. Three test cases.
# ```

# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 6 dropbox on avenue with the naming convention: macID_CL6.py
# 
# **Make sure the final version of your lab runs without errors, otherwise, you will likely recieve zero.**
# 
# This assignment is due the day after your Lab A section at 11:59 PM EST
# 
# Late labs will not be accepted
