# start

grade: int = int(input("whats your test grade? "))

match grade:
    case grade if 0 <= grade <= 40:
        print("try harder next time!")
    case grade if 41<= grade <= 60:
        print("you're getting there , need some work!")
    case grade if 61 <= grade <= 80:
        print("pretty good!")
    case grade if 81 <= grade <= 95:
        print("AWESOME!")
    case grade if 96 <= grade <= 100:
        print("EXCELLENT! YOU'RE A STAR!!!")
    case _:
        print("illegal grade!")


