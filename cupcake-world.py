# an object describing our player
player = { 
    "name": "p1", 
    "score": 0,
    "items" : ["milk"],
    "friends" : [],
    "location" : "start"
}

cupcake = {
    "cupcake1" : "birthday",
    "cupcake2" : "love",
    "cupcake3" : "cherry"
}

import random # random numbers
import sys # system stuff for exiting

def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print "You roll a: " + str(result) + " out of " + str(maxNum)

    if result <= difficulty: 
        print "trying again...."
        
        raw_input("press enter >")
        rollDice(minNum, maxNum, difficulty)

    return result

def printGraphic(name):
 if (name == "title"):
	print '                              _                             _        '
	print '                             | |                           | |    |  '
	print '  __           _   __   __,  | |   _             __   ,_   | |  __|  '
	print ' /    |   |  |/ \_/    /  |  |/_) |/    |  |  |_/  \_/  |  |/  /  |  '
	print ' \___/ \_/|_/|__/ \___/\_/|_/| \_/|__/   \/ \/  \__/    |_/|__/\_/|_/'
	print '            /|                                                       '
	print '            \|                                                       '


 if (name == "birthday"):
	print '                  ++`                   '
	print '                 +.`/.       .`         '
	print '  -+`     -`    `+  `+      `++`        '
	print '  +`:-    +/-   `+. `+      /.`+`       '
	print ' `+ `-:  ./`-/` .:+//:+    -/  `+    `:+'
	print ' `+` .+  /.  `+`o`    o`   `+-.::  .::`+'
	print '  ./oyo+/`+/:+-`+----:s   `+-://. :-` `+'
	print '   +`.+-s/:...+`y.````o   -/   -: /-`./-'
	print '   .+:+-.y/   -/+  `.-o   ::   :-o+oo/- '
	print '    /-./-oy   `os::::-o   /-   +o:--.o- '
	print '    `+:/:/h`   y/`   `o   +.   y/---++  '
	print '     `y:.:o:   s/---:/+   o`  .o::-:o`  '
	print '      .o::/o   o+.````o`  o`  o:--:o`   '
	print '       -o++y`  +-.----/:::s  :+:::s.    '
	print '      `-ooos-  /:..``    `o--s:::s-     '
	print '    .::.`...+..:-         `.o/-:oo`     '
	print '  `::`      `...`           /:::+./:`   '
	print ' `/.                         `..`  -+.  '
	print '`+.                                 `+- '
	print ':-                                   `/-'
	print '/                                     `o'
	print '+      ``````        .-:::`   -: `:-``.s'
	print 'o     `/-..-:-`` ``./-.  ::   `o   .-/+.'
	print 'o.    /.``  `.---:--``   ::    o` ` `+` '
	print '.o`  `+``/  -.   +   +   `+-..:/  /`/.  '
	print ' `:/:/:  +` ./   +   +    /.../  -/-:   '
	print '   -/`+` --  +   o   o   `+  `+ `o.+    '
	print '    /../  +` /.  o   o   :-  :: ::+`    '
	print '    `o`:: -: `+  +`  o   +`  o``o/.     '
	print '     .+`+. +` o` :-  o`  o  `+ :+:      '
	print '      -+`+ ./ -: ./  +`  +  :` .+       '
	print '       -/`  -` + `-  +`  :    `o`       '
	print '        -/.    .     :      ``+.        '
	print '         `-::-----------::::::`         '



 if (name == "cherry"):                                
	print '             +//++.                     '
	print '                  /s`                   '
	print '                 `+sh+s/                '
	print '             `oyoN-`. :ds``             '
	print '            .m/  m:   `hhoosy+          '
	print '      `+sssshh .h+hyoyh+yo++ oy         '
	print '     +h-     y/``  d`-h//:+h .dyyy/     '
	print '    +h  .+o- `+so//-   -::.  /+o/`yo    '
	print '    do  h`-h/    ``      --.oo .d`:d    '
	print '    /m+.`.+h-  /y+/++  +/.`/ss+--/d:    '
	print '     `/Ny/:`  -m/`os/  h::/+.  .y+      '
	print '       -hdssoss`+y+++++s:oso++ss:       '
	print '        `N::. +  +  +  +` + `sy         '
	print '         sh`/ +  +  +  +  + `m`         '
	print '         `N-+ :. +  /  +  + oo          '
	print '          oy/ .- :. +  + .:`m`          ' 
	print '          `mo .: .: +  + :.so           '
	print '           /h++/``/ + `o-soy`           '
	print '              .:/++++++/-.  			   '	


 if (name == "love"):
	print '              .::/-`    -//:/+-          '
	print '            o-   ./+.`+-     y           '
	print '           `o       +s`     `y           '
	print '        o-             `s.               '
	print '             /+`          -s.            '   
	print '        .:/:+o:.--`````.-+o//:.`         ' 
	print '    ``-+:``  `...-:-...```.-``://`       '
	print '   //:/-...````````...-::.-     -s.      '
	print '  +: `    `````........-..   ``  -++:`   '
	print ' -+     `    `````....`  `     `.:` -o-  '
	print './o-.``  `......```    `   ```....   `.y '
	print 's`  .`....``````  `........`..`   ```.:y '
	print 'o:`      .``.`............-......`....-y '
 	print '-+/....-...-...-....-....-....-..../o-`. '
	print '   :/   .`  .`  .`   .    .    .  `+:    '
	print '    -+`  .   .  `.   .    .   .  `o-     '
	print '     -o` ``  .   .   .   .`  `.  o-      '
	print '      -o  .  `.  .   .   .   .  //       '
	print '       :+ `.  .  .   .   .  `. `y        '
	print '        +- .  .  .   .   .  .  /:        '
	print '        `s``. `` .   .   .  .  y`        '
	print '         -+ .  . ``  .  ``  . `y         '
	print '          +//` . ``  .  .``-+//:         '
	print '            `-:/://::/:://-.             '

 if (name == "bowl"):

	print '                                            `:/+o/  '
	print '                                         `--   `d+  '
	print '                                        -.    `++   '
	print '                                      -:`   `//`    '
	print '               ``.--::::::--.`     :/.   -/:        '
	print '       -/////+oo++///::::://+oso+y+.   :+-          '
	print '   `:////-----.`               `oo.   :ss+:         '
	print ' `+/.:-.                     .+/`   /s-.::/oo       '
	print 'o`.+                      :+:    /s-     o:/h       '
	print '`s -/                   -//`    :y:       //.N`     '
	print '`m+ :/.              -++-     .y+       .+/-sd      '
	print 'h-o+.-:::-.`     .++-       /h.  `.::::://-s-       '
	print ':o  -++++////:--:+.........:s:::/++++//-  `h        '
 	print ' h`      `.-:/++++++++++++++ooo+/-.       o-        '
	print ' -o                                      .y         '
	print '  s-                                     y.         '
	print '  `y.                                   o:          '
	print '   `y-                                 s/           '
	print '     o+`                             :y-            '
	print '      `//-                        `+o:              '
	print '        `----.`             `-//+/`                 '
	print '             ::.----...`..--:++                     '
	print '               .---::-------:`                      '


 if (name == "love"):

	print '                          .+++/                   '
	print '                         :y`  .h  ``              '
	print '                        y-    oo+/:+o.           '
	print '                `////` +o-.       :h           '
	print '	                -/`  `s:-../y`-y-``         ' 
	print '              `-.:           -/-:+++:             '
	print '            -s/..-           `-`./h`              '
	print '            h`                    o-              '
	print '            ++                   .s               '
	print '           o:                    .+y.             '
	print '           ::-.                    /+             '
	print '             s:s:/.//./: .- `-  .`-/`             '
	print '             o-/.:d `m``d--yo.yoo/+               '
	print '              h`/ y  h  h  h `y`o/-               '
	print '              .h-:y  h `s -+ o`+o/                '
	print '               o+o+- h /: s`/:oy:                 '
	print '                h/ss d y`.o.ood.                  '
	print '                `ydd`h`y y`s+N-                   '
	print '                  -oss+so+/o/`                    '

 if (name == "wish"):

	print '                                                .os.                                 '               
	print '                                               .s-:s`                                '              
	print '                                              `s:  /o                                '             
	print '                                             `s/    /+                               '             
	print '                                             os`    `y/                              '               
	print '                                            /y` `oo` `y.                             '               
	print '                                           -s- `o/++  .o                             '               
	print '                                          `y:  oo  ++  ..                            '               
	print '                                          :y` /s`  `y-  ``                           '               
	print '                                          /s`.y-    `-` .                            '               
	print '                                          .o-+o`     ```:                            '               
	print '                                           .//s-`  `.:-.                             '               
	print '                                             `:/++o/:.                               '               
	print '                                                :ss-                                 '               
	print '                                                -oy-                                 '               
	print '                                              ``.+y-                                 '               
	print '                                           /o+ososh+++/o:                            '               
	print '                                           /s    ``-/oss/                            '               
	print '                                           +y`-/oyhs/-`/+                            '               
	print '                                           os/+/:.     //                            '               
	print '                                           o/    `-/oys//                            '               
	print '                                           o+-/shhs/-  ++                            '               
	print '                                           ++--.`    `.++                            '               
	print '                                           o+   `-/syy+/+                            '               
	print '                                           +s:oyhs+-`  o/                            '               
	print '                                           /y.```   `-:s:                            '               
	print '                                           +o` `-/syso:o/                            '               
	print '                                           +s/oss+:``  o:                            '               
	print '                                           +o```   .-/+o-                            '               
	print '                                           /+`.-/syso/.+/                            '               
	print '                                           /:/+++:.`   :/                            '               
	print '                                           //`    `-:+o+:                            '              
	print '                                           /:.-/osso:.`y/                            '               
	print '                                           /--/:-.`  ``s-                            '               
	print '                                           /:   `.-/osoh-                            '               
	print '                                           /-./oyys/-` o-                            '               
	print '                                           ::---.`  `..+:                            '               
	print '                                           .:  `.-/oss++-                            '               
	print '                                           -::+sys+-`  .`                            '               
	print '                                           .:`.`   ``-:..                            '               
	print '                                           .: ``-/osyo:`.                            '               
	print '                                           `:/oss+:`    `                            '               
	print '                                           `/.........` `                            '               
	print '                                            `                   						'

 if (name == "applesauce"):

	print '                         ``                                 '
	print '                        +/+-             .`-.....-.         '
	print '                         -.:.       ``-/--:..` `:.          '
	print '                          --/     -:/-`---`    -+.          '
	print '                           /.:  .+:` ```      :+`           '
	print '                           `/+ /:.:/`       `//`            '
	print '            ...--.----...   /:+-:+:........:o.              '
	print '         `--``       -..-/o/++y+/-```     ``.--.            '
	print '        --`       `//-`-/+/o.```               .:.          '
	print '       :.       ./+.``::.`./                     :-         '
	print '      :.       .+:   ``  .s.                      --        '
	print '     .-       .s-`.`   `-/`                        /.       '
	print '     /        o/--``.:::.                           /       '
	print '    `:        o---//:``              ```            :`      '
	print '    :`        //++oshy+.          ./++shh+`         .:      '
	print '    /         //`   -mMm.        +:`   -NMd.        `/      '
	print '    :`        d-     syhs        m.     ysho        `/      '
	print '    ..        sd/.``/y.-+        hd/-``+s.:/        .:      '
	print '     :        `omN+--/h/         `smN/--+y:         :`      '
	print '     :`         `-:--.`  `     `   `-:-..          `/       '
	print '      /                  ....-..                   /`       '
	print '      `/                                          --        '
	print '       .:`                                       :-         '
	print '        `/`                                    `:.          '
	print '          --                                  .:`           '
	print '           `:.                              `:.             '
	print '             .--                          `:-               '
	print '               `--.                    `--.                 '
	print '                  `---`             `---                    '
	print '                      .------------..                       '
                                                            
 if (name == "bigheart"):

	print '       `:oydNNNNNmho:`        `/ohmNNNNNdyo:`      '
	print '    :yNms/-`   `.:odMh/    /hMdo:.`   `-/smNy:    '
	print '  .dMs.             .oNm::mNo.             .sMd.  '
	print ' /Nd.                 `hMMh`                 .dN/ '
	print '-Mm`                    yy                    `mM-'
	print 'hM-                                            -Mh'
	print 'MN                                              NM'
	print 'NN`                                            `NN'
	print 'yM:                                            /My'
	print '-Mm`                                          `mN.'
	print ' +Mh`                                        `dM: '
	print '  /Md.                                      :mN:  '
	print '   -dNo`                                  .yMy`   '
	print '     +NN+`                              .sMd-     '
	print '      `+mNo`                          -yMh:       '
	print '         /dNs.                      :hMy-         '
	print '           :hMh:                 `+mNs.           '
	print '             .sNd/             `oNm+`             '
	print '               `oNm+         `sNm/                '
	print '                 `+Nm+     `oNm/                  '
	print '                   `oNm:  :mN+                    '
	print '                     `yMyyMs`                     '
	print '                       :NN:                       '

 if (name == "smallheart"):

	print '    `  `-:/-.` `  `.:/:-`    ` '
	print '   `/yddddddds--sdddddddy:` ` '
	print '  `ymhhhhhhhhhmmhhhhhhhhhmy`  '
	print '  /mhhhhhhhhhhhhhhhhhhhhhhN:  '
	print '  /mhhhhhhhhhhhhhhhhhhhhhhN:` '
	print '  `ddhhhhhhhhhhhhhhhhhhhhdy`  '
	print '   .ydhhhhhhhhhhhhhhhhhhds`   '
	print '    `:ydhhhhhhhhhhhhhdds-     '
	print '      `-sddhhhhhhhhdho.`      '
	print '   `  `  .+ddhhhhdh/.       ` '
	print '           `+dddd/`           '
	print '  `  `    `  `so`       `  `  '
	print '               `              '



def applesauce ():
    print "Let's start with 1 stick of butter, 4 tbsp applesauce, 2 cups all-purpose flour, 1 tsp. baking powder AND APPLES!!!!"
    print "Mix it all together"
    raw_input("press enter >")

    printGraphic("bowl")
    print "Mix well, set oven to 350 degrees"
    raw_input("press enter >")
    
    print "Pour into cupcake pan"
    print "Wait 30 minutes"
    raw_input("press enter >")
    print "Check if baked through with a toothpick"
    raw_input("press enter >")
    print "Take out of pan and arrange on platter"
    raw_input("press enter >")
    print "YOU ARE SWEET AS APPLESAUCE :) "
    printGraphic("applesauce")


    if ("applesauce" in player["items"]):
        print "options: [ eat now, save for later ]"
    else:
        print "options: [ eat now, save for later]"

    pcmd = raw_input(">")

    # option 1: eat now
    if (pcmd == "eat now"):
        print "enjoy!"
        printGraphic("smallheart")

    
    # option 2: save for later
    elif (pcmd == "save for later"):
        print "Hope you had fun!"
        print "Let's roll a dice to see what happens next!"
        raw_input("press enter to roll >")

        difficulty = 5
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20

        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty): 
            printGraphic("applesauce")
            printGraphic("applesauce")
            printGraphic("applesauce")
            player["score"] += 50
            print "It's you're lucky day! You get another 3 applesauce cupcakes."
            print "enjoy!"

        else:
            print " Try another cupcake. "
            allergies () # try again
        



def love ():
    print "Let's start with 1 stick of butter, 4 egg whites, 2 cups all-purpose flour, almond milk and A WHOLE LOTTA LOVE <3 "
    print "Mix it all together"
    raw_input("press enter >")

    printGraphic("bowl")
    print "Mix well, set oven to 350 degrees"
    raw_input("press enter >")
    
    print "Pour into cupcake pan"
    print "Wait 30 minutes"
    raw_input("press enter >")
    print "Check if baked through with a toothpick"
    raw_input("press enter >")
    print "Take out of pan and arrange on platter"
    raw_input("press enter >")

    printGraphic("love")
    print "SURPRISE!!! YOU GET TWO KINDS OF LOVE CUPCAKES!!! <3 <3 "

    if ("love" in player["items"]):
        print "options: [ eat now, save for later ]"
    else:
        print "options: [ eat now, save for later]"

    pcmd = raw_input(">")

    # option 1:eat now
    if (pcmd == "eat now"):
        print "enjoy!"
        printGraphic("bigheart")


    
    # option 2: save for later
    elif (pcmd == "save for later"):
        print "Hope you had fun!"
        print "Let's roll a dice to see what happens next!"
        raw_input("press enter to roll >")

        difficulty = 5
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20

        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty):
            printGraphic("love")
            player["score"] += 50
            print "It's you're lucky day! You get another two love cupcakes!!!!!"
            print "enjoy!"

        else:
            print " Try another cupcake. "
            allergies () # try again
        
def cherry ():
    print "Let's start with 1 stick of butter, 4 egg whites, 2 cups of banana flour, 1 tsp. baking powder AND LOTS OF CHERRIES!!!"
    print "Mix it all together"
    raw_input("press enter >")

    printGraphic("bowl")
    print "Mix well, set oven to 350 degrees"
    raw_input("press enter >")
    
    print "Pour into cupcake pan"
    print "Wait 30 minutes"
    raw_input("press enter >")
    print "Check if baked through with a toothpick"
    raw_input("press enter >")
    print "Take out of pan and arrange on platter"
    raw_input("press enter >")

    printGraphic("cherry")

    if ("cherry" in player["items"]):
        print "options: [ eat now, save for later ]"
    else:
        print "options: [ eat now, save for later]"

    pcmd = raw_input(">")

    # option 1: eat now
    if (pcmd == "eat now"):
        print "enjoy!"
        printGraphic("smallheart")

    
    # option 2: save for later
    elif (pcmd == "save for later"):
        print "Hope you had fun!"
        print "Let's roll a dice to see what happens next!"
        raw_input("press enter to roll >")

        difficulty = 5
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20

        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty):
            printGraphic("cherry")
            player["score"] += 50
            print "It's you're lucky day! You get another cherry cupcake."
            print "enjoy!"

        else:
            print " Try another cupcake. "
            allergies () # try again
        

def birthday ():
    print "Let's start with 1 stick of butter, 4 egg whites, 2 cups all-purpose flour, 1 tsp. baking powder AND SURPRISE SECRET INGREDIENT..."
    print "Mix it all together"
    raw_input("press enter >")

    printGraphic("bowl")
    print "Mix well, set oven to 350 degrees"
    raw_input("press enter >")
    
    print "Pour into cupcake pan"
    print "Wait 30 minutes"
    raw_input("press enter >")
    print "Check if baked through with a toothpick"
    raw_input("press enter >")
    print "Take out of pan and arrange on platter"
    raw_input("press enter >")

    printGraphic("birthday")
    print "SECRET INGREDIENT REVEAL: ITS YOUR BIRTHDAY!!!"
    raw_input("press enter >")
    print "Make a wish."
    raw_input("press enter >")
    printGraphic("wish")
    print "Your wish has been granted! YOU WON!!!"



    if ("birthday" in player["items"]):
        print "options: [ eat now, save for later ]"
    else:
        print "options: [ eat now, save for later]"

    pcmd = raw_input(">")

    # option 1: eat now
    if (pcmd == "eat now"):
        print "enjoy!"
        printGraphic("smallheart")


    
    # option 2: save for later
    elif (pcmd == "save for later"):
        print "Hope you had fun!"
        print "Let's roll a dice to see what happens next!"
        raw_input("press enter to roll >")

        difficulty = 5
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20

        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty):
            print "It's you're lucky day! You get another birthday cupcake."
            printGraphic("birthday")
            player["score"] += 50
            print "enjoy!"

        else:
            print " Try another cupcake. "
            allergies () # try again
        



def allergies ():
    print "Before we begin, are you allergic to any of the following?"
    
    if (("cherry" in player["items"]) and not ("birthday" in player["friends"])):
        print "Your options: [ wheat, milk, eggs ]"

    elif ("cherry" in player["items"]):
        print "Your options: [ wheat, milk, eggs ]"

    else:
        print "Your options: [ wheat, milk , eggs, none ]"

    pcmd = raw_input(">") # user input



    # player options
    if (pcmd == "wheat"):
        print "Hmmm, then fruit cupcakes are the way to go"

        raw_input("press enter >")
        cherry ()

    # path option
    elif (pcmd == "milk"):
        print "Uh oh. We will make sure to use almond milk instead "
        raw_input("press enter >")
        love ()

    # path2 option
    elif (pcmd == "eggs"):
        print "Some applesauce just might do the trick!"
        raw_input("press enter >")
        applesauce()

    # path3 option
    elif (pcmd == "none"):
        print "Awesome! The possibilities are endless! "
        raw_input("press enter >")
        birthday ()


def introStory():
    # let's introduce them to our world
    print "Good to see you again!"
    player["name"] = raw_input("Please enter your name >")

    # intro story, quick and dirty
    print "Welcome to Cupcake World " + player["name"] + "!"
    print "It is a fun day to make cupcakes!"
    print "You are probably hungry, so let's get baking!"
    print "Hands washed and supplies ready to go? :) "

    pcmd = raw_input("please choose yes or no >")

    # the player can choose yes or no
    if (pcmd == "yes"):
        print "Awesome!"
        raw_input("press enter >")
        allergies ()
    else:
        print "No? ... That doesn't work here."
        pcmd = raw_input("press enter >")
        introStory() # repeat over and over until the player chooses yes!


# main! most programs start with this.
def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens