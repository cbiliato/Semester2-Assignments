#!/usr/bin/env python
# coding: utf-8

# # Computing 8 Assignment
# 
# 

# ---
# ## Background
# 
# Object oriented programming languages are often used when designing and developing complex systems such as video games. Objects are used to represent various aspects of the game such as players, enemies, items, maps, etc. **Role-playing** video games are a common genre of video games where users control the actions of a player or character. These games often involve some form of combat in addition to the player having attributes such as health, levels, damage, etc. In this assignment, you will be implementing a **Player** class for a video game. Our player class will keep track of the following features:
# 
# -	The player’s name
# -	The player’s health
# -	The player’s current level
# -	The player’s current “score”
# -	The score required to reach the next level
# -	The player’s set of attacks
# 
# In addition to the **Player** class, you will be implementing a function that will use the **Player** class. Please thoroughly read the requirements section to understand how to implement the methods and function!

# ---
# ## NOTE THAT YOU WILL BE MARKED ON MULTIPLE ITEMS IN THIS LAB IN ADDITION TO THE FUNCTIONALITY OF YOUR CODE
#  - Variable Names
#  - Commenting
#  - General Legibility
#  - Test plan
#  - Exception handling
# 

# ---
# ## Program Requirements (12 Marks)
# ---
# ### Requirements - Player Class
# 
# The requirements for the **Player** class are given below. Please ensure that your methods have the EXACT naming as specified! Failure to do so will result in lost marks. 
# 
# ***Note: you must include a try and except statement in at least one function in your code.***
# 
# 1.	Create an **\_\_init\_\_**(*name*) method that takes the following arguments:
# 
#     -	***name***: A *string* representing the name of the player. The variable is assigned to an instance variable. If *name* is an empty string, the instance variable is set to the string **"Default"**.
#     
#     The method also initializes the following instance variables:
#     
#          **a.**	An *int* representing the player’s health. The player’s health is initially set to **100**.  
#          **b.**	An *int* representing the player’s level. The player’s initial level is **0**.  
#          **c.**	An *int* representing the player’s current score. The player’s initial score is **0**.  
#          **d.**	An *int* representing the score required to reach the next level. The initial value is **50**.  
#          **e.**	A *list of lists* representing the current set of attacks. Each sub-list has a length of **2**. The first element is a *string* that represents the name of the attack and the second element is an *int* representing the strength of the attack. A player has **3** different attacks. The player’s initial attacks are provided below:
# 
# 
# <center>[["Fast attack",5],["Slow attack",15],["Default Special Attack",20]]</center>
# 
# 2.	Create the following **accessor** methods:
# 
#     **a.**	**get_name**: Returns the player’s name.  
#     **b.**	**get_health**: Returns the player’s health.  
#     **c.**	**get_level**: Returns the player’s level.  
#     **d.**	**get_score**: Returns the player’s current score  
#     **e.**	**get_next_lvl_score**: Returns the score required to reach the next level.   
#     **f.**	**get_attacks**: Returns the player’s attack set.  
# 
# 
# 3.	Create the **mutator** method **raise_health**(*val*).  
# 
#     -	***val***: An *int*.  
#     -	**Method description**: The method does not return anything, but increases the player’s health by ***val***. If the ***val*** is negative, the method does nothing. The player's health cannot exceed 100 so if the sum of their current health and ***val*** exceeds 100, then set health to 100. 
# 
# 
# 4.	Create the **mutator** method **replace_attack**(*i*, *name*, *strength*).
#     -	***i***: An *int* representing an index (either 0, 1, or 2).
#     -	***name***: A *string* representing the name of an attack.
#     -	***strength***: An *int* representing the strength of the attack associated with ***name***.
#     -	**Method description**: The method replaces the list at index **i** in the attack list instance variable with a *list* of length 2 where the first element is ***name*** and the second element is ***strength***.
# 
# 
# 5.	Create the **mutator** method **take_damage**(*quantity*). 
#     -   ***quantity***: An *int*.
#     -   **Method description**: The method deducts ***quantity*** from the instance variable that stores the players health. The player’s health is set to 0 if ***quantity*** is greater than or equal to the player’s current health.
# 
# 
# 6.	Create the **mutator** method **perform_attack**(*i*, *player_2*).
#     -   ***i***: An *int* representing an index. Assume that the value must be either 0,1, or 2.
#     -   ***player_2***: A *Player* object.
#     -   **Method description**: The method simulates a user attack on ***player_2*** using the attack at index ***i*** from the attack instance variable list of lists. The method performs the following actions:
# 
#         - *player_2*’s health is calculated and stored in a variable.
#         - The object calling the method uses the attack associated with index *i* from the current set of attacks to inflict damage on *player_2* (i.e *player_2* will take damage equal to attack i’s strength).
#         - The difference between *player_2*’s current health and *player_2*’s health before the attack is calculated and stored in the variable *damage_given*.
#         - The value of *damage_given* is added to the player’s current score if the sum of *damage_given* and current score will result in a value less than the instance variable containing the score required to reach the next level.
#         - If the sum of *damage_given* and player score results in a value equal to or higher than the score required to reach the next level, then the following actions are performed
#             - a. The player’s level is increased by **1**. 
#             - b. The player’s current score is set to **0**.
#             - c. The score required to reach the next level is increased by **20**.
#             - d. Each of the player's attack strengths are increased by **5**.

# ---
# ### Requirements - Battle Simulation
# 
# In addition to the **Player** class, you are required to implement a function to simulate a battle. The function definition is given below:
# 
# 1.	Create the function **simulate_battle**(*player_1*, *player_2*, *player_1_moves*, *player_2_moves*).
#     - ***player_1***: A *Player* object.
#     - ***player_2***: A *Player* object.
#     - ***player_1_moves***: A *list* of integers where each element is between 0 and 2 (inclusive).
#     - ***player_2_moves***: A *list* of integers where each element is between 0 and 2 (inclusive).
#     - ***Method Description***: The function performs the following algorithm:
#         - For each element i in *player_1_moves*, *player_1* attacks *player_2* using the *perform_attack* method with attack i. If *player_2*'s health becomes 0 at any point, *player_1* wins the battle.
#         - Then, for each element i in *player_2_moves*, *player_2* attacks *player_1* using the *perform_attack* method with attack i. If *player_1*'s health becomes 0 at any point, *player_2* wins the battle.
#         
#         Note: *All* Player 1 attacks should occur first before *all* Player 2 attacks 
#     - ***Return***: A *string* representing the name of the player object that won the battle. If there is no winner, an empty string is provided.

# ---
# ## Implementation
# Please define the Player class in the cell below.

# In[18]:


# YOUR CODE HERE
#Main class Player
class Player:
    #Constructor for the class Player
    def __init__(self, name = ""):
        self.name = name
        self.health = 100
        self.level = 0
        self.next_lvl_score = 50
        self.score = 0
        self.attacks = [["Fast Attack", 5],["Slow Attack", 15],["Default Special Attack", 20]]
        
    #Accesor functions for the defined variables    
    def get_name(self): #Method to give value of name
        return self.name
    
    def get_health(self): #Method to give value of health
        return self.health
    
    def get_level(self): #Method to give value of level
        return self.level
    
    def get_score(self): #Method to give value of score
        return self.score
    
    def get_next_lvl_score(self): #Method to give value of next level score
        return self.next_lvl_score
    
    def get_attacks(self): #Method to give value of attacks
        return self.attacks
    
    #Mutator methods
    def raise_health(self,val):
        try:
            if val <= 0: #If statement saying if value less than or equal to zero, do below
                self.health += val
                self.health = min(self.health, 100)
        except:
            print("Health isn't going to be increased!")
            
    def replace_attack(self, i, name, strength): #Function to replace attack
        self.attacks[i] = [name, strength]
        
    def take_damage(self, quantity): #Function to take damage
        self.health -= quantity
        self.health = max(self.health, 0)
             
    def perform_attack(self, i, player_2): #Function to perform the attack
        previous = player_2.get_health() #Previous health
        player_2.take_damage(self.attacks[i][1]) #calling function to take damage
        damage_given = previous - player_2.get_health() #Difference between current and previous damage
        
        if  damage_given + self.score <= self.get_next_lvl_score(): #Check if score can take up level
            self.score += damage_given
        else: #If it can't do as follows
            self.level += 1
            self.score = 0
            self.next_lvl_score += 20
            for j in range(3):
                self.attacks[j][1] += 5


# Please define the battle simulation function in the cell below.

# In[19]:


# YOUR CODE HERE
def simulate_battle(player_1, player_2, player_1_moves, player_2_moves):
    for element in player_1_moves: #Attacks for player 1
        player_1.perform_attack(element, player_2)
            
        if player_2.get_health() <= 0:
            return(player_1.get_name(), "is a winner!")
            
    for element in player_2_moves: #Attacks for player 2
        player_2.perform_attack(element, player_1)
            
        if player_1.get_health() <= 0:
            return(player_2.get_name(), "is a winner!")
    
    return "" #If nobody wins


# ---
# ## Sample Output
# Use the following cell to test out your code!

# In[20]:


print("----TESTING PLAYER CREATION----")
colin = Player("Colin")
bosco = Player("Bosco")
colin_name = colin.get_name()
bosco_name = bosco.get_name()
print("Two players created with names:",colin_name,"and",bosco_name)

print("\n")
print("----TESTING ATTACK MODIFICATION----")
print(colin_name+"'s Attacks:",colin.get_attacks())
i = 2
new_attack = "1P13 Exam"
strength = 50
print("Changing",colin_name,"attack",i,"to",new_attack)
colin.replace_attack(i,new_attack,strength)
print(colin_name+"'s Attacks:",colin.get_attacks())

print("\n")
print("----TESTING PLAYER ATTACK----")
print(bosco_name+"'s current score:",bosco.get_score())
print(bosco_name+"'s score required to reach next level:",bosco.get_next_lvl_score())
print(colin_name+"'s health:",colin.get_health())
i=1
print(bosco_name,"will perform an attack on",colin_name,"with move",bosco.attacks[i])
print("...")
bosco.perform_attack(i,colin)
print(bosco_name+"'s current score:",bosco.get_score())
print(bosco_name+"'s score required to reach next level:",bosco.get_next_lvl_score())
print(colin_name+"'s health:",colin.get_health())

print("\n")
print("----TESTING BATTLE----")
b_moves = [0,1,2]
c_moves = [0,2,1,2]
print(bosco_name+"'s moves:",b_moves)
print(colin_name+"'s moves:",c_moves)
print(bosco_name,"will be the first to attack...")
winner = simulate_battle(bosco,colin,b_moves,c_moves)
print("Battle has finished, winner is",winner)
print(bosco_name+"'s health:",bosco.get_health())
print(colin_name+"'s health:",colin.get_health())


# The expected output from the previous cell is given below:
# 
# <code>
# ----TESTING PLAYER CREATION----
# Two players created with names: Colin and Bosco
# </code>
# <code>
# ----TESTING ATTACK MODIFICATION----
# Colin's Attacks: [['Fast attack', 5], ['Slow Attack', 15], ['Default Special Attack', 20]]
# Changing Colin attack 2 to 1P13 Exam
# Colin's Attacks: [['Fast attack', 5], ['Slow Attack', 15], ['1P13 Exam', 50]]
# </code>
# <code>
# ----TESTING PLAYER ATTACK----
# Bosco's current score: 0
# Bosco's score required to reach next level: 50
# Colin's health: 100
# Bosco will perform an attack on Colin with move ['Slow Attack', 15]
# ...
# Bosco's current score: 15
# Bosco's score required to reach next level: 50
# Colin's health: 85
# </code>
# <code>
# ----TESTING BATTLE----
# Bosco's moves: [0, 1, 2]
# Colin's moves: [0, 2, 1, 2]
# Bosco will be the first to attack...
# Battle has finished, winner is Colin
# Bosco's health: 0
# Colin's health: 45
# </code>

# ----------
# ## Code Legibility (6 Marks)
# Your code will be marked on variable names, commenting and exception handling.<br>
# The mark breakdown is as follows:<br>
# > 2 marks for using appropriate variable names that indicate what is being stored in that variable<br>
# 2 marks for leaving comments on major parts of your code such as where you read the file or calculate a summation<br>
# 2 marks for exception handling. Your functions should produce the required outputs even when receiving unexpected inputs

# # ---
# ## Test Plan (6 Marks)
# Develop a test plan for your program. Your test plan should have at least **three** test cases: one normal case, one boundary case, and one abnormal case. You can test any function/method but you must test **at least two different** functions/methods. Please use the following format for your test cases:
# 
# **Function:**   
# **Input:**  
# **Output:**  
# **Expected Output:**  
# **Pass/Fail:**  
# 
# An example test case is shown below:  
# ```
# Function: replace_attack(self, i, name, strength)
# Input: p = Player("")
#        p.replace_attack(0,"weak",2)
#        print(p.get_attacks() == [["weak",2],["Slow Attack",15],["Default Special Attack",20]])
#        
# Output: True
# Expected Output: True
# Pass/Fail: Pass
# ```
# 
# Implement your testing plan in the cell below! 

# In[17]:


'''
NORMAL CASE
Function: take_damage(self, quantity)
Input: p = Player("Carter")
       p.take_damage(10)
       print(p.get_health())
Output: 90
Expected Output: 90
Pass/Fail: Pass

BOUNDARY CASE
Function: take_damage(self, quantity)
Input: p = Player("Carter")
       p.take_damage(200)
       print(p.get_health())
Output: 0
Expected Output: 0
Pass/Fail: Pass

ABNORMAL CASE
Function: replace_attack(self, i, name, strength)
Input: p = Player("Carter")
       p.replace_attack(0, "Laserbeams", "ten")
       print(p.get_attacks()[0])
Output: Please enter the strength of your attack in the form of a number ie. 10 not ten
        ['Fast attack', 5]
Expected Output: Please enter the strength of your attack in the form of a number ie. 10 not ten
        ['Fast attack', 5]
Pass/Fail: Pass

'''


# ---
# ## Reflective Questions
# 
# 1. In the Program Requirements, the ***raise_health()*** mutator was specified to have 1 argument, but when you defined it, the mutator was defined to accept 2 parameters. What is the purpose of the first parameter? What happens if we omit this parameter?
# 
# 
# 2. Suppose we had a method ***rename_player(self,name)*** that renames your player object with *name*. Would this method be an accessor or mutator?
# 
# 
# 3. Is it possible to test that ***raise_health()*** works correctly using a single python statement (i.e. using a single line of code)?
# 
# Please answer all questions in the cell below!

# ```
# DOUBLE CLICK TO EDIT THIS CELL. DO NOT DELETE QUOTATION MARKS
# ```

# ```
# 1. Self is the first parameter, partnered with the val arguement. If we omit self, it the method will not refer to the class Player.
# 
# 2. Rename Player is a mutator method, it has more parameters than just 'self' as well as the fact that is it modifying the players name, which a mutator method could potentially do.
# 
# 3. The way I have done it, I believe it is impossible, but I am sure it can be done, potentially using a while true, or a for loop.
# ```

# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 8 dropbox on avenue with the naming convention: macID_CL8.py
# 
# **Make sure the final version of your lab runs without errors, otherwise, you will likely recieve zero.**
# 
# This assignment is due the day after your Lab A section at 11:59 PM EST
# 
# Late labs will not be accepted
