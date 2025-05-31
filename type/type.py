from random import randint
import time

def main():
    print(" 1. General \n 2. Dominant ")
    choice = int(input("\n Enter your choice: "))
    match choice:
        case 1 : schar()
        case 2 : dom()


def schar():
    count = int(input("Enter the no of Characters: "))
    i = 0
    start = time.time()
    while i < count:
        r = chr(randint(97,122))
        while True:
            c = input(f"{r}: ")
            if c == r:
                break
        i += 1
    end = time.time()
    timer(start,end,count)

def timer(start,end,count):
    duration = end - start
    print(f"Time: {duration:.2f}")
    if duration < count-5:
        print("FAST")
    elif duration < count+5:
        print("MEDIUM")
    else :
        print("SLOW")

def dom():
    choice = input("d or p (dominant)")
    if choice == "d": 
        f = open("dominant_text.txt")
    elif choice == "p":
        f = open("city_vibes.txt")
    else :
        f = False

    if f :
        for line in f:
            words = line.strip().split(" ")
            for word in words:  
                while True:
                    print(f"\t ***{word}***")
                    ans = input("\t ")
                    if(ans == word):
                        break
        f.close()



if __name__ == "__main__":
    main()
