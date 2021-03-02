# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
#  Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt", mode="r") as file:  # read all the names in the file
    names = file.readlines()

new_names = []
for n in names:
    new_names.append(n.strip())  # removes the new line character from each name

with open("./Input/Letters/starting_letter.txt", mode="r") as file:  # read the content of the starting letter
    content = file.read()

for name in new_names:  # for every name in the list new_names
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:  # open a file under that name
        new_content = content.replace("[name]", name)  # replace the string [name] with the actual name in the letter
        file.write(new_content)  # write the content with the name
