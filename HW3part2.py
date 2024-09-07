# start

grade: int = int(input("whats your test grade? "))

if grade >= 0 and grade < 40:
    print("try harder next time...!")
elif grade > 41 and grade < 60:
    print("you're getting there , need some work!")
elif grade > 61 and grade < 80:
    print("pretty good!")
elif grade > 81 and grade < 95:
    print("AWESOME!")
elif grade > 96 and grade <= 100:
    print("EXCELLENT! YOU'RE A STAR!!!")
else:
    print("grade illegal!")
