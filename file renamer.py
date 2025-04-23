import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory()

mode = str(input("Choose a mode: (R)eplace, Append to (F)ront, Append to (B)ack: "))

def user_string_getter(usermode):
    if mode == ("R" or "r"):
        user_str_og = str(input("String to Replace: "))
        user_str_new = str(input("Replace With What?: "))
        for f in os.listdir(folder_path):
            newname = f.replace(user_str_og, user_str_new)
            os.rename(r"%s/%s" % (folder_path, f),r"%s/%s" % (folder_path, newname))
    elif mode == (("F" or "f") or ("B" or "b")):
        user_str = str(input("String to Add: "))
        if mode == ("F" or "f"):     
            for f in os.listdir(folder_path):
                newname = user_str + f
                os.rename(r"%s/%s" % (folder_path, f),r"%s/%s" % (folder_path, newname))
        elif mode == ("B" or "b"):     
            for f in os.listdir(folder_path):
                newname = f + user_str
                os.rename(r"%s/%s" % (folder_path, f),r"%s/%s" % (folder_path, newname))
    return

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

print("Done.")
