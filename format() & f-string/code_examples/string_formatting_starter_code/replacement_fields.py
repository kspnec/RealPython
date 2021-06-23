# Formatting numbers is easy with the format spec
nums = [3.1, 4.0, 5.7032, 9.2032095, 20.0]

for num in nums:
    # Right-justify, reserve 9 spaces for each element, pad with '%' 
    # Use < for left-justify, ^ for center
    print(f"{num:%>9}") 

for num in nums:
    print(f"{num:6.4}") # Reserve 6 spaces for each element, truncate to 4 decimal places

big_nums = [123568234, 2938520398509235, 12948382049, 20395820398502938]
for num in big_nums:
    print(f"{num:_}") # Print big nums with underscores to divide 3-digit groups (alt. comma)

integers = [1, 2, 3, 4]
for i in integers:
    print(f"{i:b}") # Print integers in binary (o for octal, h for hexidecimal)

# When in doubt, go to the documentation! 
# No one remembers all of these possible formats at all times :)