__author__ = 'francoism'
# Mood computer
# Deomonstrate the if-elif-else structure
# francois m

import random

print "i sense your energy. your tRue emotions are coming across my screen."
print "you are..."

mood = random.randrange(3)

if mood == 0:
    # happy
    print \
        """
        -----------
       |         |
       | O     O |
       |    <    |
       |         |
       | .    . |
       |  `...`  |
       -----------
    """

elif mood == 1:
    #neutral
    print \
    """
        -----------
       |         |
       | O     O |
       |    <    |
       |         |
       | ------- |
       |         |
       -----------
       """
elif mood == 2:
    #sad
    print \
        """

        -----------
       |         |
       | O     O |
       |    <    |
       |         |
       |  .'.   |
       | '   '   |
       -----------
       """

else:

    print "illegal mood values! (you must be in a very bad mood)"

print "...today."

raw_input("\n\npress enter to quit.")