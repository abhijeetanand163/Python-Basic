# My text file location in my PC is "E:\Sample data\SampleTextFile_100kb.txt"
with open("E:\Sample data\SampleTextFile_100kb.txt", 'r') as File1:
	file_stuff = File1.readline(4)
	# readline(4) implies I am reading first four character of the text file
	print(file_stuff)

	file_stuff = File1.readline(6)
	# readline(6) is after readline(4), it implies I will read next 6 lines of the text after pervious ones.
	print(file_stuff)

