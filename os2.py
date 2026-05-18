import os

def list_files():
    files = os.listdir()
    print("Files:", files)

list_files()