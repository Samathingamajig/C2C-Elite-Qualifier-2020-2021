# This python file generates the '__init__.py' file in the 'topics' folder
# This is based off of Saulpila's answer on StackOverflow
# https://stackoverflow.com/a/41727931
if __name__ == "__main__":
  folder_name = "topics"
  from os.path import splitext, join, dirname
  from glob import glob  
  # Get all *.py filenames in the "topics" folder.
  files = [splitext(f)[0] for f in glob(join(dirname(__file__), folder_name, '*.py'))]
  with open(join(folder_name, "__init__.py"), "w") as init_file:
    init_file.write(f"# This file is autogenerated by ../generate_{folder_name}_init.py\n")
    for filename in files:
      if "__init__" not in filename: # Make sure it's not the __init__ file
        while "\\" in filename or "/" in filename: # Remove the slashes from the file name (Need to do both types of slashes because I'm developting this on Windows but this will run on a Linux machine)
          filename = filename[(filename.index("\\") or filename.index("/")) + 1:]
        init_file.write(f"from .{filename} import {filename}\n")