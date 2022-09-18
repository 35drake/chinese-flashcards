# >This is my Chinese flashcard learning program. You put the character, pinyin, and meaning of each flashcard in the "data.txt" file. See "README.txt" for details.<

# This library used to shuffle lists
import random

# This debug function displays all flashcards; you must type literally "show_all(lines)"
def show_all(lines):
	print('\n')
	for row in range(len(lines)):
		print(row,FC[row][0],FC[row][1],FC[row][2])

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


# Initialize the 'flashcards' matrix (character, pinyin, meaning):
FC = []

# Fill the 'flashcards' matrix
for line in lines:
	FC = FC + [line.split(",")]

# FC's row represents the item (quantity: len(lines))
# FC's col represents the type (character, pinyin, or meaning)

# Correct the pinyin tones in each flashcard
for row in range(len(lines)):
	for count in range(24):
		FC[row][1]=FC[row][1].replace(tones[2*count+1],tones[2*count])

# Give user menu
choice = eval(input("\n\nPick which mode:\n\n1:Show character first\n2:Show pinyin first\n3:Show either first\n4:Display all cards\n\nChoice: "))
print('\n')

# Perform program depending on choice
if choice < 4:
	
	# Create a randomized list of indices for the flashcards
	numbers_list=[]
	for count in range(len(lines)):
		numbers_list=numbers_list+[count]
	random.shuffle(numbers_list)
	
	# Show the character first
	if choice == 1:
		for count in range(len(lines)):
			print(FC[numbers_list[count]][0])
			input()
			print(FC[numbers_list[count]][1])
			print(FC[numbers_list[count]][2])	
			input()

	# Show the pinyin first
	if choice == 2:
		for count in range(len(lines)):
			print(FC[numbers_list[count]][1])
			input()
			print(FC[numbers_list[count]][1])
			print(FC[numbers_list[count]][2])	
			input()

	# Show either the character or pinyin first (chosen randomly each time)
	if choice == 3:
		for count in range(len(lines)):
			category_shown = random.choice([0,1])
			print(FC[numbers_list[count]][category_shown])
			input()
			print(FC[numbers_list[count]][not(category_shown)])
			print(FC[numbers_list[count]][2])	
			input()	

# Show all cards at once
if choice == 4:
	show_all(lines)

# Pause program until user presses a key (and print input for debug, if any)
a=input("\nDone.")
print(a)

# Reset to standard unicode encoding
check_output("chcp 65001", shell=True)