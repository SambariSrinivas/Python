TestFile = open("C:\\Users\\srini\\Learning\\Python\\Basics\\testfile.txt")
print('index in file is at {}'.format(TestFile.tell()))
TestFileContent = TestFile.read()
print('Now the index in file is at {}'.format(TestFile.tell()))
print(TestFileContent)


def closefile():
    print('Does the TestFile closed :  {}'.format(TestFile.closed))
    if not TestFile.closed:
        print("Closing the File")
        TestFile.close()
        print('Does the TestFile closed : {}'.format(TestFile.closed))
    else:
        print("File already closed")


print('First three bytes of the file are : {}'.format(TestFile.read(3)))
closefile()

with open('C:\\Users\\srini\\Learning\\Python\\Basics\\testfile2.txt') as testfile2:
    file2contents = testfile2.read()
    print("testfile2 content is : ")
    print(file2contents)
   # testfile2.write("This is another line that i am adding using write method")
    file2contents = testfile2.read()
    print(file2contents)

print("TestFile2 is Closed : {}".format(testfile2.closed))


open('C:\\Users\\srini\\Learning\\Python\\Basics\\testfile3.txt', 'w').write("This is thrid file")
open('C:\\Users\\srini\\Learning\\Python\\Basics\\testfile.txt', 'a').write("\n Adding a line using append mode")
closefile()
