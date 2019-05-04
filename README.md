# bloom-filter

## Overview

This Python script deletes duplicate files from a directory using a bloom filter approach.  
The script calculates the hash for each file in the directory and checks it against a list.  
If the hash value already exists in the list (duplicate file), the file being examined is 
deleted.  If the hash value does not yet exist, it is added to the list and traversal 
continues.

## Usage

This initial version of the script is fairly simple and uses Python's hashlib.md5() function
to produce the hex digest for each file.

Run the script by passing in the absolute path for the directory you want to examine.  
The output will show the results of the operation.

```
c:\Users\MyName\Scripts>python bloom-filter.py c:\Users\MyName\Images\DuplicateImageTest

Changed directory to c:\Users\MyName\Images\DuplicateImageTest
Now checking for and deleting duplicate files...
Done.

        50      Items originally in directory
        23      Duplicate items deleted from directory
        27      Items remaining in directory
```

Note: This script traverses the directory in reverse order in an attempt to preserve originals 
with base filenames, rather than copies with appended numbers or annotations (duplicate files 
ending in "(1)" or "- Copy", for example, usually appear before their original counterparts in 
a directory listing).

## Output

The script outputs a text file in the same directory where the delete operation takes place, 
containing a list of all items that were deleted.  The text file is timestamped with the 
date and time the script was ran.