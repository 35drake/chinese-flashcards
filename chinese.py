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

# The row represents the item (quantity: len(lines))
# The col represents the type (character, pinyin, or meaning)
for row in range(len(lines)):
	for col in range(3):
		print(row)
		print(col)
		print(FC[row][col])


# Tasks remaining: display and test user on cards randomly (choose the col shown at random too)
# Also, display the chinese toned vowels correctly somehow (ie display data 'ma4' as 'mà')
# Note: āáǎà






# Pause program until user presses a key
input()

# Reset to standard unicode encoding
check_output("chcp 65001", shell=True)

