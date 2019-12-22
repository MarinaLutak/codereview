"""
Перевірити наявність шляху до папки. Дано шлях, якщо він існує програма виведе OK, якщо ны - ERROR
"""

import re

def is_path(text):
    return bool(re.match('r^{C}?{D}?\:\/(\w)+$', text)

def is_file_path(prompt):
    var= input(prompt)
    while not is_path(var):
        var= input(prompt)
    return str(var)

def file_search(folder, file_path):
    file_path=file_path.split(\)
    if file_path[-1] is folder:
        return bool


if file_search()= True:
    print("OK")
else:
    print('ERROR')


folder= list(input('File: '))
file_path= is_file_path('File_Path: ')