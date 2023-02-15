# # Millionaire
import random
import os
import time
import winsound
from playsound import playsound
indexCorrectAnswer = 2
isCheck = True
cavablar = ["a", "b", "c","d"]
jokers = ['f', 'g', 'h']
# Functions-------------------------------------------------------------------------------------------------------------------------------
def checkAnswer():
    global checkpoint
    global isCheck
    if answer == questions[checkpoint][indexCorrectAnswer] and answer not in jokers :
        print(f"cavab dogrudur! {bankMoney[checkpoint]}$ qazandiniz")
        playsound('correct answer.mp3')
        checkpoint += 1
    elif answer != questions[checkpoint][indexCorrectAnswer] and answer not in jokers and checkpoint >4 and checkpoint <10 and answer!="y":
        print(f"Oyun bitdi cavab yanlisdir! qazanciniz {bankMoney[4]} $")
        playsound('wrong answer.mp3')
        isCheck = False
    elif answer != questions[checkpoint][indexCorrectAnswer] and answer not in jokers and checkpoint >9  and answer!="y":
        print(f"Oyun bitdi cavab yanlisdir! qazanciniz {bankMoney[9]} $")
        playsound('wrong answer.mp3')
        isCheck = False
    elif answer != questions[checkpoint][indexCorrectAnswer] and answer not in jokers and checkpoint < 6 and answer!="y":
        print("Oyun bitdi cavab yanlisdir! qazanciniz 0 $")
        playsound('wrong answer.mp3')
        isCheck = False
    elif answer == "y" and checkpoint >= 5:
        print(f"Oyundan cekildiniz  {bankMoney[checkpoint - 1]}$ Pul qazandiniz!")
        playsound('wrong answer.mp3')
        isCheck = False
def checkjokers():
    if answer== "f":
        jokers.remove("f")
        os.system('cls')
        playsound("67 50-50.mp3")
        for que in questions:
            if que == questions[checkpoint]:
                print("Question".center(30, '='))
                print(f'{checkpoint+1}'.center(30, '='))
                print(f'{bankMoney[checkpoint]}$'.center(30, '='))
                print(que[0])
                if que[indexCorrectAnswer]=="a":
                    print(f"A){que[1][0]}")
                    print(f"B){que[1][1]}")
                elif que[indexCorrectAnswer]=="b":
                    print(f"B){que[1][1]}")
                    print(f"C){que[1][2]}")
                elif que[indexCorrectAnswer]=="c":
                    print(f"C){que[1][2]}")
                    print(f"D){que[1][3]}")
                elif que[indexCorrectAnswer]=="d":
                    print(f"D){que[1][3]}")
                    print(f"A){que[1][0]}")
                print('Help Jokers'.center(30, '='))
                for i in jokers:
                    if i == "g":
                        print(f"[{i}]-Call Friend")
                    elif i == "h":
                        print(f"[{i}]-Audience")              
    if answer=="g":
        chance = random.randint(1,100)
        print("Dosta zeng edilir...")
        time.sleep(0.3)
        winsound.Beep(400, 2000)
        jokers.remove("g")
        if chance<=70:
            print(f"dostunuzun qerarina gore dogru cavab {questions[checkpoint][indexCorrectAnswer]}-dir")
        if chance > 70:
            if ord(questions[checkpoint][indexCorrectAnswer])>=97 and ord(questions[checkpoint][indexCorrectAnswer])!=100 :
                a = questions[checkpoint][indexCorrectAnswer]
                b = ord(a)
                print(f"dostunuzun qerarina gore dogru cavab {chr(b+1)}-dir")
            elif ord(questions[checkpoint][indexCorrectAnswer])== 100 :
                a = questions[checkpoint][indexCorrectAnswer]
                print(f"dostunuzun qerarina gore dogru cavab 'a'-dir")
    if answer=="h":
        chance=chance = random.randint(1,100)
        print("Auditoriya qerar verir...")
        time.sleep(0.3)
        playsound("68 Ask The Audience.mp3")
        jokers.remove("h")
        if chance <= 70:
            print(f"Auditoriyanin qerarina gore dogru cavab {questions[checkpoint][indexCorrectAnswer]}-dir")
        if chance > 70:
            if ord(questions[checkpoint][indexCorrectAnswer])>=97 and ord(questions[checkpoint][indexCorrectAnswer])!=100:
                a = questions[checkpoint][indexCorrectAnswer]
                b = ord(a)
                print(f"Auditoriyanin qerarina gore dogru cavab {chr(b+1)}-dir")
            elif ord(questions[checkpoint][indexCorrectAnswer])== 100 :
                a = questions[checkpoint][indexCorrectAnswer]
                print(f"Auditoriyanin qerarina gore dogru cavab 'A'-dir")
def que(checkpoint):
    for que in questions:
        if que == questions[checkpoint] :
            time.sleep(0.2)
            os.system('cls')
            time.sleep(0.2)
            print("Question".center(30, '='))
            time.sleep(0.2)
            print(f'{checkpoint+1}'.center(30, '='))
            time.sleep(0.2)
            print(f'{bankMoney[checkpoint]}$'.center(30, '='))
            time.sleep(0.2)
            print(f"{que[0]}")
            time.sleep(0.2)
            print(f"A){que[1][0]}")
            time.sleep(0.2)
            print(f"B){que[1][1]}")
            time.sleep(0.2)
            print(f"C){que[1][2]}")
            time.sleep(0.2)
            print(f"D){que[1][3]}")
            time.sleep(0.2)
            if len(jokers)>0:
                time.sleep(0.2)
                print('Help Jokers'.center(30, '='))
                time.sleep(0.2)
            for i in jokers:
                if i == "f":
                    time.sleep(0.2)
                    print(f"[{i}]-50/50")
                elif i == "g":
                    time.sleep(0.2)
                    print(f"[{i}]-Call Friend")
                elif i == "h":
                    time.sleep(0.2)
                    print(f"[{i}]-Audience")
            if checkpoint>4:
                 print(f"Oyundan {bankMoney[checkpoint - 1]} $ pulu goturub cekilmek ucun - [y]")
            answer = input("Cavab:")
            return answer
questions = [
    ['Həkim sizə 3 dərman verir ve bunları yarımsaat arayla qəbul etməyinizi deyir, dərmanlar nə qədər müddətdə bitər?', ['2saat', '3saat', '1saat', '0.5 saat'], 'c'],
    ['Bəzi aylar 30 gün bəziləri 31 gündür , necə ayda 28 gün var?', ['1', '12', '10', '11'], 'b'],
    ['Fermerin 17 qoyunu var, qoyun sürüsü xəstəliyə tutuldu, 9-u ağır xəstələndi digərləri isə öldü,neçə qoyun qaldı?', ['9', '17', '0', '8'], 'a'],
    ['UEFA çempionlar liqasını 2016-2017-2018-ci illərdə qazanan futbol klubu hansı Klubdur?', ['Real Madrid', 'Barcelona', 'Bayer Munchen', 'Liverpool'], 'a'],
    ['2-ci dünya müharibəsində Almanya dəmir ehtiyyatını hansı ölkədən əldə edirdi?', ['İlgiltərə', 'Norveç', 'Türkiyə', 'Azərbaycan'], 'b'],
    ['1918-ci ildə Azərbaycanın paytaxtı hansı şəhər olub?', ['Bakı', 'İrəvan', 'Təbriz', 'Gəncə'], 'd'],
    ['2008-ci Pekin olimpiyadalarında Azərbaycana qızıl medan gətirən cudoçumuz?', ['Elnur Məmmədli', 'Nazim Hüseynov', 'Beslan Mudranov', 'Kəramət Hüseynov'], 'a'],
    ['Telefonu ixtira edən kim olmusdur?', ['Graham Fuller', 'Graham Bell', 'Nikola Tesla', 'Graham Grell'], 'b'],
    ['Azərbaycanın sahəsi necə km-dir?', ['86.6 min km2', '90 min km2', '80 min km2', '85.6 min km2'], 'a'],
    ['İnsan beyninin yaddaşı nə qədərdir?', ['1tb', '2tb', '4tb', '5tb'], 'c'],
    ['Domino daşları içərisində çəkisi ən yüngül olan daş hansıdı', ['6 qoşa', '1 qoşa', 'ağ qoşa', '2 qoşa'], 'a'],
    ['İnsan gözü neçə megapixel-dir?', ['200', '1', '576', '1000'], 'c'],
    ['Dünya sağlamlıqq birliyinin qısaldılmış beynəlxalq adı nədir?', ['Unicef', 'Who', 'Nato', 'Uhw'], 'b'],
    ['Bir gün neçə saniyədir?', ['86000', '88600', '86400', '84800'], 'c'],
    ['Hansı ölkənin 2 dənə paytaxtı var?', ['Cənubi Afrika', 'Senegal', 'El Salvador', 'Venezuella'], 'a'],
]
random.shuffle(questions)
bankMoney = [100,200,300,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000]
checkpoint = 0
playsound("10 Let's Play.mp3")
while isCheck:
    if checkpoint == 0:
        answer = que(checkpoint)
        while isCheck and checkpoint==0:
            if answer in cavablar:
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 1:
        answer = que(checkpoint)
        while isCheck and checkpoint == 1:
            if answer in cavablar:
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 2:
        answer = que(checkpoint)
        while isCheck and checkpoint == 2:
            if answer in cavablar:
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 3:
        answer = que(checkpoint)
        while isCheck and checkpoint == 3:
            if answer in cavablar:
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 4:
        answer = que(checkpoint)
        while isCheck and checkpoint == 4:
            if answer in cavablar:
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 5:
        answer = que(checkpoint)
        while isCheck and checkpoint == 5:
            if answer in cavablar or answer == "y":
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint ==6:
        answer =que(checkpoint)
        while isCheck and checkpoint == 6:
            if answer in cavablar or answer == "y":
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 7:
        answer = que(checkpoint)
        while isCheck and checkpoint == 7:
            if answer in cavablar or answer == "y":
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 8:
        answer = que(checkpoint)
        while isCheck and checkpoint == 8:
            if answer in cavablar or answer == "y":
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 9:
        print("Tebrikler 2-ci Checkpointe catdiniz")
        answer = que(checkpoint)
        while isCheck and checkpoint == 9:
            if answer in cavablar or answer == "y":
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 10:
        answer = que(checkpoint)
        while isCheck and checkpoint == 10:
            if answer in cavablar or answer == "y":
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 11:
        answer = que(checkpoint)
        while isCheck and checkpoint == 11:
            if answer in cavablar or answer == "y":
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 12:
        answer = que(checkpoint)
        while isCheck and checkpoint == 12:
            if answer in cavablar or answer == "y":
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 13:
        answer = que(checkpoint)
        while isCheck and checkpoint == 13:
            if answer in cavablar or answer == "y":
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint == 14:
        answer = que(checkpoint)
        while isCheck and checkpoint == 14:
            if answer in cavablar or answer == "y":
                checkAnswer()
            elif answer in jokers:
                checkjokers()
                answer = input("Cavab:")
            else:
                print("daxiletme yanlisdir!")
                answer = input("Cavab:")
    elif checkpoint==15:
        print("Winner!")
        time.sleep(0.5)
        print("\t\tWinner!")
        time.sleep(0.5)
        print("\t\t\t\tWinnerrr!")
        time.sleep(0.5)
        print("1 Million".center(30,"$"))
        break


