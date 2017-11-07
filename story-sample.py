# let the user know what's going on
print ("A Trip To The Beach!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
name1 = raw_input("Enter your name: ")
name2 = raw_input("Enter your friend's name: ")
adjective1 = raw_input("Enter an adjective: ")
food = raw_input("Your favorite food: ")
liquid = raw_input("Your favorite drink: ")
adjective2 = raw_input("Enter another adjective: ")
animal = raw_input("Your favorite animal: ")
adjective3 = raw_input("Enter one more adjective: ")
verb = raw_input("Enter a verb: ")
pluralnoun = raw_input("Name a pair of things you would buy at the beach: ")
food2 = raw_input("Your favorite fish food: ")
verb2 = raw_input("Enter a verb: ")
noun = raw_input("Enter a noun: ")

# this is the story. it is made up of strings and variables.
story = "One day, " + name1 + " and " + name2 + " decided to take a trip to the beach. " + name1 + " packed a bag full of " + adjective1 + " " + food + " " \
" and a big jug of " + liquid + ". " + name2 + " brought a towel that had a picture of a " + adjective2 + " " + animal + " on it." \
"The beach was crowded but there were a few " + adjective3 + " spots left. " + name1 + " and " + name2 + " wanted to learn how to " + verb + " " \
"so they rented a pair of " + pluralnoun + " and hopped into the water. " \
 " Soon it was time for more snack so " + name1 + " went to a stand to buy fish " + food2 + ". " \
"The sun was " + verb2 + " and eventually the tide came too close so " + name1 + " and " + name2 + " packed their" \
" " + noun + " and went home. "

# finally we print the story
print (story)