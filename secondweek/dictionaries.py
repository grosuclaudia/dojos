battleship_guesses = {
    (3, 4): False,
    (2, 6): True,
    (2, 5): True,
}

surnames = {} # this is an empty dictionary
surnames["John"] = "Smith"
surnames["John"] = "Doe"
print(surnames) # we overwrote the older surname

marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }
marbles["blue"] = 30 # this will work
print(marbles)