import csv
from tabulate import tabulate
import itertools
from itertools import combinations_with_replacement
import datetime
# print(bsss)
# print(arr)
# _________________________________________


def sedosona():
    print("""
                        $$$$$$$$$$$$$$$$$   EEEEEEEEEEEEEEE   DDDDDDDDDDDDDDDDDD
                        $$$$$$$$$$$$$$$$$   EEEEEEEEEEEEEEE   DDDDDDDDDDDDDDDDDDD             OOOOOOO
                        $$$$$$$             EEEEE             DDDD           DDDDD          OOO     OOO
                        $$$$$$$             EEEEE             DDDD            DDDDD        OOO       OOOO
                        $$$$$$$$$$$$$$$$$   EEEEEEEEE         DDDD             DDDDD      OOOO       OOOO
                        $$$$$$$$$$$$$$$$$   EEEEEEEEE         DDDD             DDDD       OOOO       OOOO
                                $$$$$$$   EEEEE             DDDD            DDDD        OOOO       OOOO
                                $$$$$$$   EEEEE             DDDD           DDDD           OOO     OOO
                        $$$$$$$$$$$$$$$$$   EEEEEEEEEEEEEEE   DDDDDDDDDDDDDDDDDD              OOOOOOO
                        $$$$$$$$$$$$$$$$$   EEEEEEEEEEEEEEE   DDDDDDDDDDDDDDDDD

                                            $$$$$$$$$$$$$$$$$                               NNNNNN          NNN         AAAAAAAAAAAAAAAA
                                            $$$$$$$$$$$$$$$$$                               NNN NNN         NNN         AAAAAAAAAAAAAAAA
                                            $$$$$$$                      OOOOOOO            NNN  NNN        NNN         AAA          AAA
                                            $$$$$$$                    OOO     OOO          NNN   NNN       NNN         AAA          AAA
                                            $$$$$$$$$$$$$$$$$         OOO       OOOO        NNN    NNN      NNN         AAAAAAAAAAAAAAAA
                                            $$$$$$$$$$$$$$$$$        OOOO       OOOO        NNN     NNN     NNN         AAAAAAAAAAAAAAAA
                                                    $$$$$$$        OOOO       OOOO        NNN      NNN    NNN         AAA          AAA
                                                    $$$$$$$        OOOO       OOOO        NNN       NNN   NNN         AAA          AAA
                                            $$$$$$$$$$$$$$$$$          OOO     OOO          NNN        NNN  NNN         AAA          AAA
                                            $$$$$$$$$$$$$$$$$            OOOOOOO            NNN         NNN NNN         AAA          AAA
    """)
    print()


fName = str(datetime.datetime.now()).replace(":", "-").replace(".", "-")


def generateFormChar():
    b = input("Enter your characters Ex (ab6@c1!) : ")
    arr = list(b.strip())
    x = len(arr)
    count = 0
    print("THIS FOR : "+b)
    for i in range(1, x+1):
        l = list(itertools.product(arr, repeat=i))
        print("level" + str(i),
              " / number of possiable values in this level : " + str(len(l)))
        count += len(l)
        with open(fName+'.csv', mode='a+', newline='') as filename:
            filename = csv.writer(filename, delimiter='|',
                                  quotechar='|', quoting=csv.QUOTE_MINIMAL)
            # filename.writerow(
            #     "------------------------------------------------------------------")
            # filename.writerow("THIS FOR : "+b)
            filename.writerow(["level " + str(
                i) + "/ number of possiable values in this level : "+str(len(l))])
            # filename.writerow(
            #     "_________________________")
            filename.writerows(l)
            # filename.writerow(
            #     "------------------------------------------------------------------ End level"+str(i))

        print(tabulate(l, tablefmt="fancy_grid"))
    print("------------------------------------------------------------------")
    print("number of all values : ", str(count))
    print()
    cho = input(
        "scan again ? [y/n] \n[change] for change the scan way \nEnter your choise: ")
    if cho == "y":
        print()
        generateFormChar()
    elif cho == "change":
        print()
        chooses()
    elif cho == "n":
        print()
        print("thank you")


def generateFormWord():
    b = input(
        "Enter your words separeted by ',' note that your white space will be included : ")
    arr = list(b.split(","))
    # print(arr)
    x = len(arr)
    count = 0
    print("THIS FOR : "+b)
    for i in range(1, x+1):
        l = list(itertools.product(arr, repeat=i))
        print("level" + str(i),
              " / number of possiable values in this level : " + str(len(l)))
        count += len(l)
        with open(fName+'.csv', mode='a+', newline='') as filename:
            filename = csv.writer(filename, delimiter='|',
                                  quotechar='|', quoting=csv.QUOTE_MINIMAL)
            # filename.writerow("THIS FOR : "+b)

            filename.writerow(["level " + str(
                i) + "/ number of possiable values in this level : "+str(len(l))])
            filename.writerows(l)
        print(tabulate(l, tablefmt="fancy_grid"))
    print("------------------------------------------------------------------")
    print("number of all values : ", str(count))
    print()
    print(
        "scan again ? [y/n] \n[change] for change the scan way \nEnter your choise:")
    cho = input()
    if cho == "y":
        print()
        generateFormWord()
    elif cho == "change":
        print()
        chooses()
    elif cho == "n":
        print()
        print("thank you")


def chooses():
    choose = input(
        "[c] for character combination \n[w] for word combination \nEnter your choise: ")
    print()
    if choose == "c":
        generateFormChar()
    elif choose == "w":
        generateFormWord()
    else:
        print("wrong choise")


sedosona()
chooses()
