from operator import truediv
import random
letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
palabra="benja"
frase =""
n=0
cuenta=0
a=True
while a:
    numero_letra = random.randint(0,26)
    frase=frase+letras[numero_letra]
    
    if frase==palabra:
        a=False
    elif len(frase) >= 5 :
        print(frase)
        frase=""
    cuenta=cuenta+1

print("intentos=",cuenta)