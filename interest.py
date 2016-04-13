# Prompt the user for an Initial Balance (and save to a variable)
# use the float() function to convert the input into a number.
initialBalance = float(input("What is the Initial Balance? "))

# Prompt the user for an Annual Interest % (and save to a variable)
# use the float() function to convert the input into a number
annualInterestPercent = float(input("What is the Annual Interest percentage? "))

# change the percentage number into a decimal (e.g. 6 turns into .06, 5 turns into .05, etc).
# remember to save your new value to a variable!
annualInterestDecimal = (annualInterestPercent / 100)

# Prompt the user for a Number of years (and save to a variable)
# use the int() function to convert the input into an integer
yearsBanked = int(input("How many years will it be banked? "))

# Calculate the total value following the formula.
# You can use multiple steps and variables if necessary.
# Note that n = 12
totalValue = (initialBalance * (1 + (annualInterestDecimal/12))**(12*yearsBanked))

# Calculate the interest earned based on the above value and the initial balance
interestEarned = (totalValue - initialBalance)

# Output the interest earned
print ("Interest earned in "+str(yearsBanked)+" years: $"+str(interestEarned))

# Output the total value
print ("Total value after "+str(yearsBanked)+" years: $"+str(totalValue))
