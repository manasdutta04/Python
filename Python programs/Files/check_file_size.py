# example 1:

import os

file_stat = os.stat('my_file.txt')
print(file_stat.st_size)


# example 2:

# from pathlib import Path

# file = Path('my_file.txt')
# print(file.stat().st_size)