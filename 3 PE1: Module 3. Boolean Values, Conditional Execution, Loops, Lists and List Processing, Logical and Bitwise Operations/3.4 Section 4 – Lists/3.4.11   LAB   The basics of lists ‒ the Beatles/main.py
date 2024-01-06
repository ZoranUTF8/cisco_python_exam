#
# Scenario
# The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
#
# The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
#
#
# Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
#
# step 1: create an empty list named beatles;
beatles = []
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
for a in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(a)
print(beatles)
# step 4: use the del instruction to remove "Stu Sutcliffe" and Pete Best from the list;
indexOf1 = beatles.index("Stu Sutcliffe")

del beatles[indexOf1]

indexOf2 = beatles.index("Pete Best")
del beatles[indexOf2]
print(beatles)
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.
beatles.insert(0, "Ringo Starr")
print(beatles)
# By the way, are you a Beatles fan? (The Beatles is one of Greg's favorite bands. But wait...who's Greg...?)
