# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

cyfry1 = "1 2 3 4 5 6 7 8 9 0"
cyfry = cyfry1.split()
duze1 = "A B C D E F G H I J K L M N P Q R S T U V W X Y Z"

duze = duze1.split()
znaki1 = "!  # $ % ^ & * ( ) - + [ ]"
znaki = znaki1.split()
male1 = " a b c d e f g h i j k l m n o p q r s t u v w x y z"
male = male1.split()

def generuj(ile):
        haslo, haslo1, haslo2 = "", "", ""
        if ile < 8:
            ile = 8


        haslo1 = (
                haslo1
                + " "
                + random.choice(cyfry)
                + " "
                + random.choice(duze)
                + " "
                + random.choice(znaki)
                + " "
                + random.choice(male)
                + random.choice(znaki)
                + ""
        )
        # losuje  znaki,
        for i in range(ile):
            haslo2 = haslo2 + " " + random.choice(duze) + " " + random.choice(male)
        haslo3 = haslo2.split()
        haslo4 = haslo1.split()
        haslo5 = ""
        for i in range(4):
            haslo5 = haslo5 + " " + haslo4[i]
        haslo5 = haslo5 + " "
        for i in range(ile - 4):
            haslo5 = haslo5 + " " + haslo3[i]
        haslo6 = haslo5.split()
        random.shuffle(haslo6)
        for i in range(ile):
            haslo = haslo + haslo6[i]
        return haslo


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Generuj nowe hasło ")
    ile1 = int(input("podaj ilość znaków?"))
    print(generuj(ile1))
    k = input("press any button to exit")

