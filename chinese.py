# This reference list interprets pinyin tones
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

# The row represents the item (quantity: len(lines))
# The col represents the type (character, pinyin, or meaning)
for row in range(len(lines)):
	for col in range(3):
		print(row)
		print(col)
		print(FC[row][col])




# Drake, now you have to tl interpret the pinyin tones

# Tasks remaining: display and test user on cards randomly (choose the col shown at random too)












# Pause program until user presses a key
input()

# Reset to standard unicode encoding
check_output("chcp 65001", shell=True)

