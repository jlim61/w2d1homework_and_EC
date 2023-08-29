# Reference from Dylan

# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints
    # Determine a Logical way to solve the problem
        #Write each step out english
        #Write each step out in Python-esse
    # Invoke and Test Your Function

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Given a string of letters, write a function to see if the word  is a palindrome (the same word spelled forward and backwards).

# The given string will contain only letters 

# Examples:
# is_palindrome("RaceCar") \\ => True
# is_palindrome("mom")  \\ => True
# is_palindrome("Shoha") \\ => False

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
input string of letter
output = boolean (Dylan asked if he was safe to assume looking for boolean. That's the format you want to ask during a technical assessment)
constraints: inputs are only letter, only one word (also asked if he was safe to assume it is only one word so he doesn't have to worry about spaces which was confirmed so that is a constraint)
RaceCar


approach:
look at end of each letter and check equality
if they are unequal then it is not a palindrome
if it's equal, look at the next letters and check for equality
next letters moving first letter one to the right
last letter one to the left
continue checking all letter for equality until unequal or I've checked to the middle

pseudo code:
if not letter = 
return false
else = 
continue

"""
# 

def check_palindrome(astring):
    left_point = 0 # set up index because you usually have to do that for a while loop
    right_point = len(astring) - 1 # this sets up the end of the string letter, but length is 3 and index goes 0-2 so you have to make it "-1" to target last letter
    while left_point < right_point: # run code while condition is met, it will continue until condition is no longer met
        # print(left_point, right_point)
        # print(astring[left_point], astring[right_point], astring[left_point] != astring[right_point])
        if astring[left_point].lower() != astring[right_point].lower():
            return False
        else:
            left_point += 1
            right_point -= 1
    return True

print(check_palindrome("RaceCar"), True)
print(check_palindrome("mom"), True)
print(check_palindrome("Shoha"), False)

def check_with_reverse(astring):
    return astring.lower() == astring.lower()[::-1]

print(check_palindrome("RaceCar"), True)
print(check_palindrome("mom"), True)
print(check_palindrome("Shoha"), False)