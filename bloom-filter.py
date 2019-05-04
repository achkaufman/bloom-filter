import sys
import os
import hashlib

if len(sys.argv) > 1:
    # If a filepath was passed in, cd to that directory
    os.chdir(str(sys.argv[1]))

    # debugging
    print()
    print("Changed directory to " + os.getcwd())

# Get list of all filenames in directory before delete operation
filenameList = os.listdir()
startCount = len(filenameList)

# Debugging - Output list of files originally in directory before delete operation
# print(str(startCount) + " files in directory:")
# for x in range(len(filenameList)):
#     print(filenameList[x])
# print()

# Create list to track hashes of files in current directory
md5list = []

# Create list to track filenames of deleted items
deletedItems = []

# For each file, check to see if its hash is in the hash list
# If it is, delete the file (duplicate)
# If it isn't, add it (new file)
# Note: Traverse the list in reverse to preserve originals,
# since copies with a number appended typically appear first
print("Now checking for and deleting duplicate files...")
for filename in reversed(filenameList):
    h = hashlib.md5()
    with open(filename, 'rb') as file:
        fileBinary = 0
        fileBinary = file.read()
        h.update(fileBinary)
    # If the file's hash already exists in the hash list, delete the file
    if h.hexdigest() in md5list:
        deletedItems.append(filename)
        os.remove(filename)
    # Otherwise, add the file's hash to the list
    else:
        md5list.append(h.hexdigest())
print("Done.")
print()

# Get the number of deleted items
deletedCount = len(deletedItems)

# Debugging - Output list of files that were deleted during operation
# print(str(deletedCount) + " items deleted:")
# for x in range (len(deletedItems)):
#     print(deletedItems[x])
# print()

# Get list of all filenames in current directory
newFilenameList = os.listdir()
endCount = len(newFilenameList)

# Debugging - Output list of files remaining in directory after delete operation
# print(str(endCount) + " files in directory:")
# for x in range(len(newFilenameList)):
#     print(newFilenameList[x])
# print()

# Summary
print("\t" + str(startCount) + "\tItems originally in directory")
print("\t" + str(deletedCount) + "\tDuplicate items deleted from directory")
print("\t" + str(endCount) + "\tItems remaining in directory")