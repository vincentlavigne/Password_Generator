import random

def GenPass():
    caracteres = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$%^&*(){}[]<>~+=-_\/|:;")
    caracteres = list(caracteres)
    nb_digit = int(input("Nombre de caractères? "))
    mot_de_passe = ''
    for i in range(nb_digit):
        char_hasard = random.choice(caracteres)
        mot_de_passe = mot_de_passe + char_hasard
    print(mot_de_passe)

GenPass()