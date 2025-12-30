# Break Statement
i = 0
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
# After Using Break Statement the loop terminates when the condition becomes true
# Continue Statement
i = 0
while i <= 5:
    if(i == 4):
        i += 1
        continue
    print(i)
    i += 1
# Contiue Statement Skips the value when the condition becomes true and continues the loop
# Example of Continue Statement
# Print all odd numbers using continue statement between 1 to 10
print("Odd Numbers")
i = 0
while i <= 10:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1
# Print all odd numbers using continue statement between 1 to 10
print("Even Numbers : ")
i = 0
while i <= 10:
    if(i % 2 != 0):
        i += 1
        continue
    print(i)
    i += 1