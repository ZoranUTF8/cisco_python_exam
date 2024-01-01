# TODO Question 1: Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:

# for num in range(1,11):
#     if num % 2 != 0:
#         print(num)

# TODO Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
# count = 0
#
# while count < 11:
#     if count % 2 != 0:
#         print(count)
#
#     count += 1

# TODO Question 3: Create a program with a for loop and a break statement. The program should iterate over characters in an email
# TODO address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:

# def get_address(email_address):
#     name = ""
#
#     for let in email_address:
#         if let == "@":
#             break
#
#         print(let, end="")
#
#
# get_address("zoran_janjic23@gmail.com")

# TODO Question 4: Create a program with a for loop and a continue statement. The program should iterate over a string of digits,
# TODO replace each 0 with x, and print the modified string to the screen. Use the skeleton below:

# def replace_0_with_x(stringofdigits):
#     for let in str(stringofdigits):
#         if let == "0":
#             print("x", end="")
#             continue
#         print(let,end="")
#
#
# replace_0_with_x("0165031806510")


# TODO Question 5: What is the output of the following code?

# n = 3
#
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)


# 4
# 3
# 2
# 0

#  TODO Question 6: What is the output of the following code?
#
# n = range(4)
#
# for num in n:
#     print(num - 1)
# else:
#     print(num)

# -1
# 0
# 1
# 2
# 3


#  TODO Question 7: What is the output of the following code?
# for i in range(0, 6, 3):
#     print(i)

# 0,3


flag_register = 0x1234
print(flag_register)
