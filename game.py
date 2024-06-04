import random 
bot = ['batu','gunting','kertas']

while True:
    x = random.choice(bot)
    data = input("Masukan pilihan :")
    
    if data == x:
        print(f"pilihanmu adalah {data}")
        print(f"pilihan bot adalah {x}")
        print("Hasil seri\n\n")
        
    elif data == 'batu' and x == 'gunting':
        print(f"pilihanmu adalah {data}")
        print(f"pilihan bot adalah {x}")
        print("Kamu Menang\n\n")
    elif data == 'kertas' and x == 'batu':
        print(f"pilihanmu adalah {data}")
        print(f"pilihan bot adalah {x}")
        print("Kamu Menang\n\n")
    elif data == 'gunting' and x == 'kertas':
        print(f"pilihanmu adalah {data}")
        print(f"pilihan bot adalah {x}")
        print("Kamu Menang\n\n")
         
    elif data == 'gunting' and x == 'batu':
        print(f"pilihanmu adalah {data}")
        print(f"pilihan bot adalah {x}")
        print("Kamu Kalah\n\n")
    elif data == 'batu' and x == 'kertas':
        print(f"pilihanmu adalah {data}")
        print(f"pilihan bot adalah {x}")
        print("Kamu Kalah\n\n")
    elif data == 'kertas' and x == 'batu':
        print(f"pilihanmu adalah {data}")
        print(f"pilihan bot adalah {x}")
        print("Kamu Kalah\n\n")
    else:
        print("Program Valid!!")
        break