import re
import time
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
import random
def head():
    print("\t\t\t\tWelcome to Madlibs Generator\n\t\t\t\t  Your fun day starts here!")

clear()
head()
consent=int(input("Do you want to: \n1. Play\n2. Quit\n\nPress 1/2: "))
if consent == 2:
    quit()
elif consent == 1:
    with open('story1.txt','r') as f:
        story=f.read()

blanks=re.findall(r"\{(.*?)\}",story)
response={}

for word in blanks:
    response[word]=input(f"Enter a {word}: ")

final_story = story.format(**response)

clear()
head()
print(final_story)


