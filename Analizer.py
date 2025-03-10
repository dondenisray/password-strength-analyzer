import re
import random
import string

#Vamos a evaluar la seguridad de una contraseña y devolveremos una puntuación y su consecuente clasificacion

def evaluate_password(password):

    score = 0 

    #Verificamos la longitud

    if len(password) >= 8 : 
        score += 1 
    if len(password) >= 12 :
        score += 1

    #Verificamos si hay caracteres especiales

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score +=1

    #Verificamos números

    if re.search(r"\d",password):
        score += 1

    #Asignamos la clasificación

    if score <= 2:
        return "**** DÉBIL ****"
    elif score <=4:
        return "**** MEDIA ****"
    else:
        return "**** FUERTE ****"
    
#Vamos a generar una contraseña aleatoria fuerte
def generate_strong_password(lenght = 12):

    characters = string.ascii_letters + string.digits + "!@#$%^&*()"

    return "".join(random.choice(characters) for _ in range(lenght))





