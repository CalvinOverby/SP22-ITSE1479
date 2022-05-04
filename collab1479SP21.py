# Menu program for Programming Final Project
# Used with Github to ensure that students know the GitHub process.

semester = "ITSE1479 - Spring 2022";

def main():
    #*****************************************************************
    # jumpTable for all functions
    # 
    # Modify your line to create a jumpTable entry for your 
    #   function.  Replace stub() with the name of your function that 
    #   you added to the end this code section.
    #
    # Notes:
    #    jumpTables hold the name of a function, not the variables
    #       that are passed to it.  See smileyFunction for a way
    #       to pass variables manually, 
    #       OR create your own inputs inside of your function to 
    #           collect user input.
    #   Use the following code at the end of your function to 
    #       pause the program
    #           print()
    #           print("Press ENTER to return to the menu")
    #           input()
    #   DO NOT TRASH THE CALL TO main() at the end.  Thanks.
    #*****************************************************************
    jumpTable = {}
    jumpTable['1'] = smileyFunction       # Smiley - call to function goes here
    jumpTable['2'] = stub                 # Alvarez - call to function goes here
    jumpTable['3'] = stub                 # Appiah - call to function goes here
    jumpTable['4'] = stub                 # Balderas - call to function goes here
    jumpTable['5'] = stub                 # Butler - call to function goes here
    jumpTable['6'] = stub                 # Kennedy - call to function goes here
    jumpTable['7'] = stub                 # Long - call to function goes here
    jumpTable['8'] = stub                 # Nguyen - call to function goes here
    jumpTable['9'] = overbyFunction      # Overby - call to function goes here
    jumpTable['10'] = stub                # Robarge - call to function goes here
    jumpTable['11'] = stub                # Roeper - call to function goes here
    jumpTable['12'] = stub                # Subba - call to function goes here
    jumpTable['13'] = stub                # Thorne - call to function goes here
    jumpTable['14'] = stub                # Thurman - call to function goes here
    jumpTable['15'] = stub                # Valdez - call to function goes here

    chrChoice = ""      # To hold a menu choice

    # Constants for the menu choices
    EXIT = '0';

    while chrChoice != '0':
        # Display the menu and get the user's choice.
        showMenu();
        
        chrChoice = input("Enter your selection (0 to exit): ")
        
        if(chrChoice.isdigit() and int(chrChoice) < (len(jumpTable) + 1)):
            # Validate the menu selection.
            if chrChoice == EXIT:
                print()
                print("Thank for using the", semester, "Menu Program. ")
                print("Have a nice day.")
            else:
                jumpTable[chrChoice]()
        else:
            print("Please enter one of the numeric values from the menu.  Thanks")
            print("Press ENTER to continue.")
            input()    

            

#*****************************************************************
# Definition of function showMenu which displays the menu.       *
#*****************************************************************

def showMenu():
    print("*******************************************************************")
    print("*   Welcome to the ", semester, " Program!")
    print("*      Make a selection from the list below to see student output *")
    print("*                                                                 *")
    print("*      Enter 0 and press Enter to Quit.                           *")
    print("*******************************************************************")

    print("1.  Smiley")
    print("2.  Alvarez")
    print("3.  Appiah")
    print("4.  Balderas")
    print("5.  Butler")
    print("6.  Kennedy")
    print("7.  Long")
    print("8.  Nguyen")
    print("9.  Overby")
    print("10. Robarge")
    print("11. Roeper")
    print("12. Subba")
    print("13. Thorne")
    print("14. Thurman")
    print("15. Valdez")
    print()

# *****************************************************************************************
# Function Definitions Section
# *****************************************************************************************
# Add your function below.  
#  
# FunctionName:  lastnameFunction(your parameters)
# *****************************************************************************************

# *****************************************************************************************
# FUNCTION:         stub (default for menu)
# DESCRIPTION:      stub function created to print a single message: Not Implemented Yet
# OUTPUT EXAMPLE:   User enters any jumpTable entry that has not been created yet
# *****************************************************************************************
def stub():
    print()
    print()

    print("Not implemented at this time.  Check back later.")
    print("Press ENTER to continue.")
    input()


# *****************************************************************************************
# FUNCTION:         overbyFunction
# DESCRIPTION:      Takes a year as an input from the user, and calculates when
#                   Easter will be that year.
# OUTPUT EXAMPLE:   User enters 2022
#                   Program outputs the following:
#                      Easter occurs on the Seventeenth of April in 2022.
# *****************************************************************************************
def overbyFunction():
    MONTHS = ("January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December")

    DAYS = ("First", "Second", "Third", "Forth", "Fifth", "Sixth", "Seventh", 
            "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth", "Thirteenth", 
            "Fourteenth", "Fifteenth", "Sixteenth", "Seventeenth", "Eighteenth",
            "Nineteenth", "Twentieth", "Twenty-first", "Twenty-second", 
            "Twenty-third", "Twenty-fourth", "Twenty-fifth", "Twenty-sixth", 
            "Twenty-seventh", "Twenty-eighth", "Twenty-ninth", "Thirtieth")
    
    #"Splash" menu describing the program at first start.
    print("\n" * 2)
    print("*" * 51)
    print("*{:^49}*".format('FUNCTION DESCRIPTION'))
    print("*" * 51)
    print("* This program takes any year and returns the Day *\n" +
          "* and Month that Easter Sunday will occure.       *")
    print("*%49s*" % " ")
    print("*" * 51)
    
    #The Year value
    year = input("Enter a year: ")
    year = int(year)
    
    #Easter Sunday calculation
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25 
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    #Month
    n = (h - m + r + 90) // 25
    #Day
    p = (h - m + r + n + 19) % 32
    
    #Month and Day number to word convertion
    month = MONTHS[n - 1]
    day = DAYS[p - 1]
    
    print("\nEaster occurs on the {} of {} in {}.".format(day, month, year))
    print("\nPress ENTER to continue.")
    input()



# *****************************************************************************************
# FUNCTION:         smileyFunction
# DESCRIPTION:      calls SmileyFib with a parameter of 11
#                   prints the Fibonacci series as defined by the input value
# OUTPUT EXAMPLE:   User enters 11
#                   Program outputs the following:
#                      Fibonacci Sequence (9 iterations): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# *****************************************************************************************
def smileyFunction():
    smileyFib(11)
    print("Press ENTER to continue.")
    input()    

def smileyFib(numberOfTimes):
    current = 0
    nextOne = 1
    nextTerm = 0

    print()
    print()
    print("Fibonacci Sequence (", str(numberOfTimes)," iterations)")

    for i in range(0, numberOfTimes):
        if (i == 1):                    # Prints the first term
            print(str(current), end= '')

        elif (i == 2):                 # Prints the second term
            print(str(nextOne), end = '')
        else:                          # Prints all subsequent terms
            nextTerm = current + nextOne;
            current = nextOne;
            nextOne = nextTerm;

            print(str(nextTerm), end = '')

        if (i + 1) < numberOfTimes:
            print(", ", end = '')

    print()
    print()

#*****************************************************************
# Please leave me alone,
#   Sincerely,
#       main()
#*****************************************************************
main()
