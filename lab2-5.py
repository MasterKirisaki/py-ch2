mid = int(input("Midterm"))
final = int(input("Final"))
homework = int(input("Homework"))
total = (mid*40/100)+(final*50/100)+(homework*10/100)
print("Total: ", total, "score")
x = total

if x >= 90 and x <= 100:
    print("Grad A")
elif x >= 85 and x < 90:
    print("Grad B+")
elif x >= 80 and x < 85:
    print("Grad B")
elif x >= 75 and x < 80:
    print("Grad c+")
elif x >= 70 and x < 75:
    print("Grad c")
elif x >= 65 and x < 70:
    print("Grad D+")
elif x >= 60 and x < 55:
    print("Grad D")
elif x >= 55 and x < 50:
    print("Grad F")

