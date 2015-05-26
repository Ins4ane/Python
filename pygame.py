nice = 0
mean = 0

def main():
    start()
    

def start():
    print "Hello and welcome to Nice or Mean!"
    name = raw_input("What's your name?: " )
    print "Welcome, " +name+"!"
    print "In this game, you will be greeted by several different people. You can treat them nicely or you can be mean."
    print "At the end of the game, your fate will be determined depending on how you acted."
    choice = raw_input("Do you want to play? y/n " )
    if choice == "y":
        print "Great, use 'm' for mean and 'n' for nice!"
        begin()
    if choice == "n":
        print "Okay, bye..."

def begin():
    global nice
    global mean
    
    if nice > 4:
        print "Nice job - you win! Everyone loves you, and you live in a palace!"
        choice = raw_input("Do you want to play again? y/n  ")
        if choice == "y":
            print "Ok, let's go!"
            nice = 0
            begin()
        if choice == 'n':
            print "Say no more.....bye!"
            exit()
    if mean > 4:
        print "Too bad - game over! You now live in a van down by the river with no friends!"
		# reset global variables here
	choice = raw_input("Do you want to play again? y/n  ")
        if choice == "y":
            print "Ok lets go!"
            mean = 0
            begin()
        if choice == 'n':
            print "Off you go!"
            exit()
        elif choice != "y"+"n":
            print "Please enter y or n "
            if choice == "y":
                begin()
            if choice == "n":
                print "See you later!"
                exit()
            if choice != "y"+"n":
                choice = raw_input("Do you want to play again? y/n  ")
                
   
                    
    pick = raw_input("Someone approaches you to talk. Will you be nice or mean? n/m? ") # spell approaches correctly
    if pick == "n":
        print "They smile and walk away."
        nice = nice+1
        print "You currently have " + str(nice) + " nice."
        begin()
    if pick == 'm':
            print "They frown, glare and storm off."
            mean = mean+1
            print "You currently have " + str(mean) + " mean."
            begin()
        

start()

# general comments: nice came. Work on spacing between output for readability. Also, your counters are off for interating through the game.
