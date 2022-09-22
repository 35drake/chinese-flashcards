# >This is my Chinese flashcard learning program. You put the character, pinyin, and meaning of each flashcard in the "data.txt" file. See "README.txt" for details.<

# This library used to shuffle lists
import random

# This debug function displays all flashcards (FC var doesn't need to be passed)
def show_all():
	print('\n')
	for row in range(len(FC)):
		print(row,FC[row][0],FC[row][1],FC[row][2])

# This module allows Windows to pause for a key press that doesn't have to be ENTER
import msvcrt as m
def pause():
	m.getch()
	print()
	
# This reference list (48) interprets pinyin tones
tones = ['ā',"a1",'á',"a2",'ǎ',"a3",'à',"a4",
'ē',"e1",'é',"e2",'ě',"e3",'è',"e4",
'ī',"i1",'í',"i2",'ǐ',"i3",'ì',"i4",
'ō',"o1",'ó',"o2",'ǒ',"o3",'ò',"o4",
'ū',"u1",'ú',"u2",'ǔ',"u3",'ù',"u4",
'ǖ',"v1",'ǘ',"v2",'ǚ',"v3",'ǜ',"v4"]

# Display Chinese text in the Windows terminal:
from subprocess import check_output
check_output("chcp 936", shell=True)

# Store flashcard data in 'lines' list:
with open('data.txt',encoding="utf8") as f:
    lines = f.readlines()

# Initialize and fill the 'flashcards' matrix
# FC's row represents the item (quantity: len(lines))
# FC's col represents the type (character, pinyin, or meaning)
FC = []
for line in lines:
	FC = FC + [line.split(",")]
	# The "lines" list shouldn't be used anymore, use "FC"

# Add a '\n' character to the end of the last flashcard (this ensures its asterisk won't be displayed if it has one)
if not(FC[-1][2][-1] == '\n'):
	FC[-1][2] = FC[-1][2] + '\n'

# Fix the tones of each flashcard and mark them as special if they have '*'
specials=[]
for row in range(len(FC)):
	for count in range(24):
		
		# Correct pinyin tones
		FC[row][1]=FC[row][1].replace(tones[2*count+1],tones[2*count])

		# Omit asterisk and add card to special list
		if FC[row][2][-2] == '*':
			FC[row][2] = FC[row][2][:-2] + FC[row][2][-1] #spot [-1] is just a '\n'
			specials = specials+[row]

# Give user menu
choice = input("\n\nPick which mode:\n\n1:Show character first\n2:Show pinyin first\n3:Show character OR pinyin first\n4:Display meaning first\n5:Display all cards\n6:Quit\nTYPE 's' BEFORE THE NUMBER TO ONLY USE STARRED FLASHCARDS.\n\nChoice: ")
print('\n')

# Delete all non-special flashcards if the user activates special (starred) only mode.
specials_only = False
if choice[0] == 's':
	specials_only = True
	choice = choice[1:]
	
	# Put all special flashcards into temporary list, then use that to overwrite the FC list
	FC_temp = []
	for each_index in specials:
		FC_temp = FC_temp + [FC[each_index]]
	FC = FC_temp
	
# Perform program depending on choice
choice = eval(choice)
if choice < 5:
	
	# Create a randomized list of indices for the flashcards
	numbers_list=[]
	for count in range(len(FC)):
		numbers_list=numbers_list+[count]
	random.shuffle(numbers_list)
	
	# Show the character first
	if choice == 1:
		for count in range(len(FC)):
			print(FC[numbers_list[count]][0])
			pause()
			print(FC[numbers_list[count]][1])
			print(FC[numbers_list[count]][2])	
			pause()

	# Show the pinyin first
	if choice == 2:
		for count in range(len(FC)):
			print(FC[numbers_list[count]][1])
			pause()
			print(FC[numbers_list[count]][0])
			print(FC[numbers_list[count]][2])	
			pause()

	# Show either the character or pinyin first (chosen randomly each time)
	if choice == 3:
		for count in range(len(FC)):
			category_shown = random.choice([0,1])
			print(FC[numbers_list[count]][category_shown])
			pause()
			print(FC[numbers_list[count]][not(category_shown)])
			print(FC[numbers_list[count]][2])	
			pause()	

	if choice == 4:
		for count in range(len(FC)):
			print(FC[numbers_list[count]][2])
			pause()
			print(FC[numbers_list[count]][0])
			print(FC[numbers_list[count]][1])	
			pause()

# Show all cards at once
if choice == 5:
	show_all()

# Pause program until user presses a key (and print input for debug, if any)
a=input("\nDone.")
print(a)

# Reset to standard unicode encoding
check_output("chcp 65001", shell=True)