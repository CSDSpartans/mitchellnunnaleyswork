#   This reads and prints the whole document.
#           It does not prt a blank line after each line of the file

name_of_mydocument = 'tuesdayafternoon.txt'
file_input = open(name_of_mydocument, 'r')     #open file for reading

line = file_input.readline()
print(line,end = '' )
line = file_input.readline()
print(line, end = '')
line = file_input.readline()

line_counter = 0
stanza_counter = 0
total_lines_in_file = 2

while line != '':                      # while not end of file
    total_lines_in_file += 1
    if line == '\n':
      stanza_counter += 1
      
      print ()
    else:
      if (line_counter) < 10:
        line_counter += 1
        print(line_counter, ")   " , line, end = '')           # don't print another new line
      else:
        line_counter += 1
        print(line_counter, ")  " , line, end = '')           # don't print another new line
      
    line = file_input.readline()
    
print ()
print ()
print("The song \"Tuesday Afternoon\" first appeared on the album \x1B[3mDays of Future Passed\x1b[23m in 1967.")
print ("The members of The Moody Blues are Graeme Edge, Justin Hayward and John Lodge.")
file_input.close()
