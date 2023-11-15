letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz"




def encrypt(t, o):                   #"Text rotation+en" mainīgas definēšana
  r = ""
  for c in t:                  #Mainīga definēšana, kas būs vajadzīgs šifrēšanā
    if (letters.find(c) == -1):  
      r += c
    else:                      #Mainīga definēšana, prētējā gadijumā
      r += (letters[(letters.find(c) + o) % len(letters)])
  return r




def decrypt(t, o):                  #"Text rotation-de" mainīgas definēšana
  r = ""
  for c in t:                 #Mainīga definēšana, kas būs vajadzīgs dešifrēšanā
    if (letters.find(c) == -1):  
      r += c
    else:                     #Mainīga definēšana, prētējā gadijumā
      r += (letters[(letters.find(c) - o) % len(letters)])
  return r




režims = """  
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(režims))          #Funkcijas izvelēšana




if mode == 1:                 #Pirmā funkcija, jeb šifrēšana
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + encrypt(text, rotation))
elif mode == 2:               #Otrā funkcija, jeb atšifrēšana
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decrypt(text, rotation))
elif mode == 3:               #Trešā funkcija, jeb bruteforcing ~...?
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")