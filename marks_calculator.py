
name = input("Enter student name: ")

m1 = int(input("Enter Maths marks: "))
m2 = int(input("Enter Science marks: "))
m3 = int(input("Enter English marks: "))

total = m1 + m2 + m3
average = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
