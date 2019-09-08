from pathlib import Path
import shutil
firstInput = input()
step1Lst = ['D', 'R']
searchCharLst = ['A', 'N ', 'E ', 'T ', '< ', '> ']
step3Lst = ['F', 'D', 'T']
allFiles = []
interestingFiles = []
path1 = firstInput[2:]
firstLines = []
finalFirstLines = []
#Functions start here


def is_binary(file_name: str) -> bool:
    '''determines if file is readable'''
    try:
        with open(file_name, 'tr') as check_file:  #Tries to open file in text mode
            check_file.read()
            return False
    except:  #If it is false, then it is a text file (non-binary)
        return True

def listPaths(onepath: str) -> list:
    '''makes list of paths of files in directory and prints it'''
    p = Path(onepath)
    j = list(p.iterdir())
    try:
        for i in j:
            if Path(i).name == '.DS_Store':
                j.remove(i)
            else:
                pass
    finally:
        j.sort()
        for path in j:
            if Path.is_file(path) == True:
                allFiles.append(path)
                print(path)

def listSubPaths(twopath: str) -> list:
    '''prints list of paths as well as subdirectories'''
    p = Path(twopath)
    j = list(p.iterdir())
    files_list = []
    dir_list = []
    try:
        for i in j:
            if Path(i).name == '.DS_Store':
                j.remove(i)
            else:
                continue
    finally:
        for path in j:
            if Path.is_dir(path) == True:
                dir_list.append(path)
            else:
                files_list.append(path)
        files_list.sort()
        dir_list.sort()
        for file in files_list:
            allFiles.append(file)
            print(file)
        for directory in dir_list:
            if Path.is_dir(directory) == True:
                listSubPaths(directory)
            else:
                allFiles.append(directory)
                print(directory)


def allFilesInteresting(allFiles:list) -> list:
    '''Makes all paths "interesting"'''
    for path in allFiles:
        interestingFiles.append(path)

def interestingNameFiles(allFiles: list, interestName: str) -> list:
    '''Makes files with a certain name "interesting"'''
    for path in allFiles:
        temp = Path(path).name
        if temp == interestName:
            interestingFiles.append(path)

def interestExt(allFiles: list, interestExt: str) -> list:
    '''Makes files with given extension "interesting"'''
    for path in allFiles:
        temp = Path(path).suffix
        if temp == interestExt:
            interestingFiles.append(path)

def bytecountLessThan(allFiles: list, bytesize: int) -> list:
    '''Makes files with a byte size less than input 'interesting"'''
    for path in allFiles:
        if int(bytesize) > Path.stat(path).st_size:
            interestingFiles.append(path)

def bytecountGreaterThan(allFiles: list, bytesize: int) -> list:
    '''Makes files with a byte size greater than input "interesting"'''
    for path in allFiles:
        if int(bytesize) < Path.stat(path).st_size:
            interestingFiles.append(path)

def findText(allFiles: list, certaintext: str) -> list:
    '''Makes text files with a certain text in it "interesting"'''
    for path in allFiles:
        if Path.is_file(path) == True and is_binary(path) == False:
            f = open(path, 'r')
            text = f.read()
            if certaintext in text:
                interestingFiles.append(path)
            f.close()

def printFirstLine(interestingFiles: list) -> list:
    '''#Makes list and Prints first line of all interesting files who have desired text.'''
    for file in interestingFiles:
        try:
            if is_binary(file) == False:
                f = open(file, 'r')
                text = f.readline()
                if text != '\n':
                    firstLines.append(text)
                f.close()
            else:
                text = 'NOT TEXT\n'
                firstLines.append(text)
        except:
            continue

def duplicateFiles(interestingFiles: list) -> list:
    '''# duplicates all files that are "interesting"'''
    for file in interestingFiles[:]:
        temp = shutil.copy(file, str(file) + '.dup')
        interestingFiles.append(temp)
    print(interestingFiles)

def touchFiles(interestingFiles: list) -> None:
    '''updates time stamp of all interesting files to current time'''
    for file in interestingFiles:
        file.touch()
                

# First step of input
while firstInput[0] not in step1Lst:
    print('ERROR')
    firstInput = None
    firstInput = input()
    path1 = firstInput[2:]

if firstInput[0] == 'D' and len(firstInput) > 2:
    listPaths(path1)
elif firstInput[0] == 'R' and len(firstInput) > 2:
    listSubPaths(path1)

#Step 2: Narrowing Search to Interesting Files
searchChar = input()

while searchChar[0:2] not in searchCharLst:
    print('ERROR')
    searchChar = None
    searchChar = input()

if searchChar[0] == 'A':
    allFilesInteresting(allFiles)
    for file in interestingFiles:
        print(file)
elif searchChar[0] == 'N':
    interestName = searchChar[2:]
    interestingNameFiles(allFiles, interestName)
    for file in interestingFiles:
        print(file)
elif searchChar[0] == '<':
    bytesize = searchChar[2:]
    bytecountLessThan(allFiles, bytesize)
    for file in interestingFiles:
        print(file)
elif searchChar[0] =='>':
    bytesize = searchChar[2:]
    bytecountGreaterThan(allFiles, bytesize)
    for file in interestingFiles:
        print(file)
elif searchChar[0] == 'T':
    certaintext = searchChar[2:]
    findText(allFiles, certaintext)
    for file in interestingFiles:
        print(file)
elif searchChar[0] == 'E':
    interestE = searchChar[2:]
    interestE = '.' + interestE
    interestExt(allFiles, interestE)
    for file in interestingFiles:
        print(file)

#Third Input takes action on interesting files
        
thirdInput = input()
while thirdInput not in step3Lst:
    print('ERROR')
    thirdInput = None
    thirdInput = input()

if thirdInput[0] == 'F':
    printFirstLine(interestingFiles)
    for text in firstLines:
        finalFirstLines.append(text[0:-1])
    for newText in finalFirstLines:
        print(newText)
elif thirdInput[0] == 'D':
    duplicateFiles(interestingFiles)
elif thirdInput[0] == 'T':
    touchFiles(interestingFiles)
    




