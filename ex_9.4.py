fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
counts = dict()

line = fh.read()
line = line.rstrip()
for line in fh:
    if not line.startswith("From ") : continue
    word = line.split()
    aaa = word[1]
    counts[aaa] = counts.get(aaa,0)+1

bigcount = None
bigword = None
for aaa,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = aaa
        bigcount = count

print bigword, bigcount

"""9.4 Write a program to read through the mbox-short.txt and figure out
ho has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word 
of those lines as the person who sent the mail. The program creates 
a Python dictionary that maps the sender's mail address to a count
of the number of times they appear in the file. After the dictionary
 is produced, the program reads through the dictionary using
 a maximum loop to find the most prolific committer."""
