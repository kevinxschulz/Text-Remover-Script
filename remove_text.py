import os

# Use the current directory as the working directory
directory = os.getcwd()

# Text to be removed from the file names
text_to_remove = input('Enter the text to be removed from the file names: ')

# Iterate through all files in the current directory
for filename in os.listdir(directory):
    new_filename = filename.replace(text_to_remove, '')  # Remove the specific text from the file name
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))  # Rename the file

# Print what just happened
print(f'Text "{text_to_remove}" has been removed from all file names in the current directory.')
