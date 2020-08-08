#command to delete Nth line in the file e.g. delete first line
sed '1d' sed_learn_file.txt

# delete 2nd line
sed '2d' sed_learn_file.txt

#delete last line 
sed '$d' sed_learn_file.txt

#delete range of lines
sed '1,3d' sed_learn_file.txt

#delete distinct line numbers
sed '1d;3d' sed_learn_file.txt

#delete empty lines
sed '/^$/d' sed_learn_file.txt

#delete line if it contains UPPER CASE letters
sed '/[A-Z]*$/d' sed_learn_file.txt


#delete the line if it contains a specific word
sed '/line/d' sed_learn_file.txt

#delete all lines except 
sed '/line/!d' sed_learn_file.txt
