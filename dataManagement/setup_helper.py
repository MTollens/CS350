# this file is run to ensure that there are no problems with the install
import os, sys, warnings, subprocess, threading, shutil

try:
    import wx
    import wx.adv
    import mysql.connector
    import json
    import platform
    import regex
except Exception as e:
    print("encountered import error:")
    print(e)
    print("make sure you have the required modules on your PATH, or in the appropriate virtualenv")
    quit()

if __name__ == "__main__":
    print("this file is not meant to be run on its own\nrun main.py")
else:
    # create the images directory if it doesnt exist,
    if not os.path.exists("images"):
        os.mkdir("images")