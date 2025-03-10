from Analizer import evaluate_password,generate_strong_password

#Aquí hacemos el menu del analizer

def main():

    print("\n🔐 Password Strength Analyzer 🔐")

    while True: 
        choice = input("\n1. Evaluar contraseña\n2. Generar contraseña segura\n3. Salir\n>")

        if choice == "1":
            pwd = input("Ingresa tu contraseña: ")
            print(f"Seguridad: {evaluate_password(pwd)}")
        elif choice == "2" :
            print(f"Contraseña generada : {generate_strong_password()}")
        elif choice == "3":
            print("Hasta pronto...")
            break
        else:
            print("**** Ingresa un numero valido, no seas así ****") 


if __name__ == "__main__":
    main()