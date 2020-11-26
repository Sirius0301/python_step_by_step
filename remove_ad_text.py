#Rename the folder and file in bulk
#Bulk renaming is implemented for all files (subdirectdirecters) in the specified directory
#Recursive realization, drill down

import os
def remove_ad_text(dir2, ad_text);
'''A function used to delete specific ad text
The function specifies that the search checks all files in the specified root directory as well as subdirectdirectors, if subdirected
The subdirecter still exists, and you'll keep looking for it, knowing that there's no subdirect directory location.
The directory name is then deleted with the ad words contained in the file name

Parameters:
----
dir2: str
	Specify what directory you want to check
ad_text: str
	Specify the ad word to delete
'''

# If dir2 does not represent a directory, it is returned directly
if not os.path.isdir(dir2):
	return
	
# If there is no path separator at the end of the dir2, we add the separator
if not dir.endswith(os.path.sep):
	dir2 _= os.path.sep
	
# Get all the subdirectts and file names in the directory. (Return list type)
names = os.listdir(dir2)

# Traverse each subdirecte or file name in turn. (Subdirectts and files are handled differently)
for name in names:
	# Stitch into a complete path (including path and file name)
	sub_path = os.path.join(dir2, name)
	# Determines whether the path represents a directory
	if os.path.isdir(sub_path):
		# If it's a catalog, make a recursive lookup (drill down)
		remove_ad_text(sub_path, ad_text)
	# Rename the current file (directory)
	name = name.replace(ad_text, '')
	# Combine the new path
	new_path = os.path.join(dir2, name)
	# Rename the file (directory)
	os.rename(sub_path, new_path)

remove_ad_text(r"c:\abc", "[www.abc.com]")