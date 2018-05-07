import random
from collections import deque

SUITE = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
P1 = ""
P2 = ""
DESK = []
talia_P1 = []
talia_P2 = []
#player_one_deck = [] # dodane 1.1
#player_two_deck = [] # dodane 1.1

class Deck(object):
    #complete_deck = []


    def __init__(self, suite, ranks):

        print("Class'a inicjalizowana!")
        self.suite = suite
        self.ranks = ranks
        self.complete_deck = [] #talia do stworzenia talii
        self.shuffled_deck = []  #talia potasowanych kart
        self.player_one_deck = [] # deck of player1
        self.player_two_deck = [] # deck of player2

    def create_deck(self): #tworzymy talie kart z 2-list
        for i in range(len(self.suite)):
            for j in range(len(self.ranks)):
                el = self.suite[i] + self.ranks[j]
                #print(el)
                self.complete_deck.append(el)
        return self.complete_deck

    def shuffle_shuffle(self): # z talii gotowych kart , po jej potasowaniu
        random.shuffle(self.complete_deck)
        self.shuffled_deck = self.complete_deck
        #print(self.shuffled_deck)
        print('\n')
        #print(len(self.shuffled_deck))
        return self.shuffled_deck

    def for_two_player(self):
        #global player_one_deck,player_two_deck
        print("\nRozdaje pierwszemu P1\n")
        self.player_one_deck = self.shuffled_deck[:26]
        #print(self.player_one_deck)
        #print(len(self.player_one_deck))
        print("\nRozdaje drugiemu P2\n")
        self.player_two_deck = self.shuffled_deck[26:]
        #print(self.player_two_deck)
        #print(len(self.player_two_deck))
        print("Karty rozdane! Gracze maja swoje talie!\n\n")
        return self.player_one_deck, self.player_two_deck


class Hand(Deck):

    def __init__(self):
        Deck.__init__(self,SUITE,RANKS)
        Deck.create_deck(self)
        Deck.shuffle_shuffle(self)
        Deck.for_two_player(self)
        self.hand_p1 = [] # aktualne karty na rece P1
        self.hand_p2 = [] # aktualne karty na rece P2
        #Deck.__init__(self,SUITE,RANKS)

    def dobierz_karty_P1(self):
        info = "Gracz %s dobiera karty!\n" % (self.nameP1)
        print(info)
        #print(self.player_one_deck)
        self.hand_p1 = self.player_one_deck#dodaje pierwsza dobierz_karte
        print(self.hand_p1)
        print("%s ma karty\n" % (self.nameP1))
        talia_P1 = self.hand_p1
        return self.hand_p1

    def dobierz_karty_P2(self):
        info = "Gracz %s dobiera karty!" % (self.nameP2)
        print(info)
        #print(self.player_two_deck)
        self.hand_p2 = self.player_two_deck
        print(self.hand_p2)
        print("%s konczy dobierac\n" % (self.nameP2))
        talia_P2 = self.hand_p2
        return self.hand_p2

    def odrzuc_karte_P1(self): # tutaj dodac parametr N oznaczajacy miejsce karty na rece
        #print("Gracz {}, odrzuca karty".format(self.nameP1))
        self.hand_p1.remove(self.hand_p1[0])# tutaj bedzie N-1
        talia_P1 = self.hand_p1#
        #print(self.hand_p1)
        return self.hand_p1, talia_P1

    def odrzuc_karte_P2(self): # tutaj dodac parametr N oznaczajacy miejsce karty na rece
        #print("Gracz {} odrzuca karty".format(self.nameP2))
        self.hand_p2.remove(self.hand_p2[0])# tutaj bedzie N-1
        talia_P2 = self.hand_p2
        #print(self.hand_p2)
        return self.hand_p2, talia_P2


class Player(Hand):

    def __init__(self):
        Hand.__init__(self)
        self.nameP1 = P1
        self.nameP2 = P2
        self.DESK = DESK


    def set_player_name_P1(self):#ustawia name gracza P1
        P1 = input("Gracz P1 podaj swoj nick:\n")
        print("Gracz P1: ", P1)
        self.nameP1 = P1
        return self.nameP1

    def set_player_name_P2(self):#ustawia name gracza P2
        P2 = input("Gracz P2 podaj swoj nick:\n")
        print("Gracz P2: ", P2)
        self.nameP2 = P2
        return self.nameP2

    def czy_mam_karty(self):
        if (len(self.hand_p1) >= 0):
            #print(self.hand_p1)
            print("Na rece mam jeszcze: ", len(self.hand_p1))
            talia_P1 =self.hand_p1#
        return self.hand_p1, talia_P1


    def zagraj_karte_P1(self):
        #print(self.hand_p1)
        self.DESK.append(self.hand_p1[0])
        print("Gracz %s zagrywa karte %s"%(self.nameP1, self.hand_p1[0]))
        talia_P1 = self.hand_p1#
        print("\n")#,self.DESK)
        return self.DESK, self.hand_p1


    def zagraj_karte_P2(self):
        #print(self.hand_p2)
        self.DESK.append(self.hand_p2[0])
        print("Gracz %s zagrywa karte %s" %  (self.nameP2, self.hand_p2[0]))
        talia_P2 = self.hand_p2
        print("Stoł:\n\t\t",self.DESK)
        return self.DESK, self.hand_p2


gracz = Player()
gracz.set_player_name_P1()
gracz.set_player_name_P2()
gracz.dobierz_karty_P1()
gracz.dobierz_karty_P2()
print("\n")
#print(talia_P1)
def ruch():
    global wybor
    print("\n\nTwoj ruch {}".format(gracz.nameP1))
    print("Wybierz cyfre 1 lub 2:\n")
    print("1. Zagraj karte\n2.Ile mam kart na rece")

    choose = int(input("1 czy 2\n"))
    wybor = choose
    print(choose)
    return wybor
# Poczatek gry
print("War is starting in 3... 2 ... 1..\n GO!!!\n\n\n")
while (len(gracz.hand_p1) != 0) or (len(gracz.hand_p2) != 0):
    ruch()
    if (wybor == 1):
        gracz.zagraj_karte_P1()
        gracz.odrzuc_karte_P1()
        gracz.zagraj_karte_P2()

        gracz.odrzuc_karte_P2()
        place1 = gracz.DESK[0][1]
        place2 = gracz.DESK[1][1]

        if len(gracz.DESK[0]) == 3:
            zmienna1 = gracz.DESK[0][1]
            print("jest dyszka na pierwszym")
            zmienna1 = 58
            if zmienna1 > ord(gracz.DESK[1][1]):
                for i in range(len(gracz.DESK)):
                    gracz.hand_p1.append(gracz.DESK[i])

                del gracz.DESK[:]   #czyszczenie stolu
                print(gracz.hand_p1)
                print("Gracz {} zgarnia karty!".format(gracz.nameP1))
            else:
                for i in range(len(gracz.DESK)):
                    gracz.hand_p2.append(gracz.DESK[i])

                    del gracz.DESK[:] #czyszczenie stolu
                    print("Gracz {} zgarnia karty!".format(gracz.nameP2))
                    print(gracz.hand_p2)

        elif len(gracz.DESK[1]) == 3:
            zmienna2 = gracz.DESK[1][1]
            print("jest dyszka na drugim")
            zmienna2 = 58
            if zmienna2 > ord(gracz.DESK[0][1]):
                for i in range(len(gracz.DESK)):
                    print(len(gracz.DESK))
                    print(i)
                    gracz.hand_p2.append(gracz.DESK[i])

                    del gracz.DESK[:] #czyszczenie stolu
                    print("Gracz {} zgarnia karty!".format(gracz.nameP2))
                    print(gracz.hand_p2)
            else:
                for i in range(len(gracz.DESK)):
                    print(len(gracz.DESK))
                    print(i)
                    gracz.hand_p1.append(gracz.DESK[i])

                del gracz.DESK[:]   #czyszczenie stolu
                print(gracz.hand_p1)
                print("Gracz {} zgarnia karty!".format(gracz.nameP1))


        elif place1.isupper() & place2.isupper():
            starter = ["J", "Q", "K", "A"]
            alter = ["W", "X", "Y", "Z"]

            pozycja1 = starter.index(place1)
            pozycja2 = starter.index(place2)

            w1 = alter[pozycja1]
            w2 = alter[pozycja2]
            if w1 > w2:
                for i in range(len(gracz.DESK)):
                    gracz.hand_p1.append(gracz.DESK[i])

                del gracz.DESK[:]   #czyszczenie stolu
                print(gracz.hand_p1)
                print("Gracz {} zgarnia karty!".format(gracz.nameP1))
            elif w1 < w2:
                for i in range(len(gracz.DESK)):
                    gracz.hand_p2.append(gracz.DESK[i])

                del gracz.DESK[:] #czyszczenie stolu
                print("Gracz {} zgarnia karty!".format(gracz.nameP2))
                print(gracz.hand_p2)
            else:
                print("Mamy wojne!")


        elif (gracz.DESK[0][1] > gracz.DESK[1][1]): #wygral P1
            for i in range(len(gracz.DESK)):
                gracz.hand_p1.append(gracz.DESK[i])

            del gracz.DESK[:]   #czyszczenie stolu
            print(gracz.hand_p1)
            print("Gracz {} zgarnia karty!".format(gracz.nameP1))

        elif (gracz.DESK[0][1] < gracz.DESK[1][1]): #wygral PC
            for i in range(len(gracz.DESK)):
                gracz.hand_p2.append(gracz.DESK[i])

            del gracz.DESK[:] #czyszczenie stolu
            print("Gracz {} zgarnia karty!".format(gracz.nameP2))
            print(gracz.hand_p2)

        elif(gracz.DESK[0][1] == gracz.DESK[1][1]):
            print("Mamy wojne")
            continue
        else:
            continue

    elif (wybor == 2):
        gracz.czy_mam_karty()
    else:
        print("Nie masz takiego ruchu!")
        continue

#gracz.zagraj_karte_P1()
#gracz.odrzuc_karte_P1()
#gracz.zagraj_karte_P2()
#gracz.odrzuc_karte_P2()
