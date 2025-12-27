# Taking Name and Age as Input from User and Print Eligibility Message
marks = int(input("Enter Your Marks : "))
name = input("Enter Your Name : ")
if 90 <= marks >= 100:
    grade = "A++"
    performance = "Excellent"
elif 80 <= marks >= 89:
    grade = "A"
    performance = "Very Good"
elif 70 <= marks >= 79:
    grade = "B"
    performance = "Good"
elif 50 <= marks >= 69:
    grade = "C"
    performance = "Average"
else:
    grade = "F"
    performance = "You Are Failed"
# Print The Result
print("----- Your Result -----")
print(f"Marks : {marks}")
print(f"Grade =  {grade}")
print(f"Performance =  {performance}")