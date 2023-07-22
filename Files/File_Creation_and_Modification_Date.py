# example 1:

import os.path, time

file = pathlib.Path('abc.py')
print("Last modification time: %s" % time.ctime(os.path.getmtime(file)))
print("Last metadata change time or path creation time: %s" % time.ctime(os.path.getctime(file)))


# example 2:

# import datetime
# import pathlib

# fname = pathlib.Path('abc.py')
# print("Last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
# print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_ctime))