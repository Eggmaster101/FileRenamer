# Imports
# TODO Double check what all of these do.
import os
import tkinter as tk
from tkinter import filedialog

# TODO Double check what's going on here.
root = tk.Tk()
root.withdraw()

# Prompts the user for the directory where the files to rename are.
folder_path = filedialog.askdirectory()

# Asks the user whether or not they want to completely replace a string, or to add a prefix or suffix to the filename.
mode = str(input("Choose a mode: (R)eplace, Append to (F)ront, Append to (B)ack: "))

# Function for renaming files
def user_string_getter(usermode):
    # If the user has chosen to replace a string in the filename:
    if mode == ("R" or "r"):
        # Asks the user for a string within the filename that they would like to replace.
        user_str_og = str(input("String to Replace: "))
        # Asks the user what they want to replace the chosen string with. By inputting nothing for this, this function will act as a string deleter.
        user_str_new = str(input("Replace With What?: "))
        # Applies the function to every file in the folder indiscriminitely, so be very careful that files won't undergo unwanted changes.
        for f in os.listdir(folder_path):
            # Generates the new filename by using the replace method to search for the chosen string within the filename and replace it with the new string (if one is given). Files without the chosen string will remain unaffected.
            # TODO Check what happens if string can't be found in any file? Should probably make it throw up an error message.
            newname = f.replace(user_str_og, user_str_new)
            # TODO Double check what this method is doing.
            os.rename(r"%s/%s" % (folder_path, f),r"%s/%s" % (folder_path, newname))
    # If the user has chosen to add something to the filename:
    elif mode == (("F" or "f") or ("B" or "b")):
        user_str = str(input("String to Add: "))
        if mode == ("F" or "f"):     
            # Applies the function to every file in the folder indiscriminitely, so be very careful that files won't undergo unwanted changes.
            for f in os.listdir(folder_path):
                # Generates the new filename by adding the original filename to the given string
                newname = user_str + f
                # 
                os.rename(r"%s/%s" % (folder_path, f),r"%s/%s" % (folder_path, newname))
        elif mode == ("B" or "b"):     
            # Applies the function to every file in the folder indiscriminitely, so be very careful that files won't undergo unwanted changes.
            for f in os.listdir(folder_path):
                # Generates the new filename by adding the given string to the original filename
                newname = f + user_str
                # 
                os.rename(r"%s/%s" % (folder_path, f),r"%s/%s" % (folder_path, newname))
    return

# Runs the function defined above.
user_string_getter(mode)

# =============================================================================
# if mode == ("R" or "r"):
#     for f in os.listdir(folder_path):
#         newname = user_string_getter(mode)
#         os.rename(r"%s/%s" % (folder_path, f),r"%s/%s" % (folder_path, newname))
# elif mode == ("A" or "a"):
#     for f in os.listdir(folder_path):
#         num = find_num(f)
#         newname = "%s_%s.png" % (prefix, num)
#         os.rename(r"%s/%s" % (folder_path, f),r"%s/%s" % (folder_path, newname))
# =============================================================================

# Visual confirmation that the program has run.
print("Done.")
