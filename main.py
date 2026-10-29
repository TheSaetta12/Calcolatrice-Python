from calcoli import somma, sottrai, moltiplica, dividi

while True:
    print("\nBenvenuti nella Calcolatrice!")
    print("1. Somma")
    print("2. Sottrai")
    print("3. Moltiplica")
    print("4. Dividi")
    print("0. Annulla la Calcolatrice")
    num1 = int(input("Primo numero: "))
    num2 = int(input("Secondo numero: "))
    scelta = input("Scelta: ")
    match scelta:
        case "1":
            risultato_finale = somma(num1,num2)
            print(f"Hai scelto Somma, il risultato è: {risultato_finale}")
        case "2":
            risultato_finale = sottrai(num1,num2)
            print(f"Hai scelto Sottrai, il risultato è: {risultato_finale}")
        case "3":
            risultato_finale = moltiplica(num1,num2)
            print(f"Hai scelto Moltiplica, il risultato è: {risultato_finale}")
        case "4":
            risultato_finale = dividi(num1,num2)
            print(f"Hai scelto Dividi, il risultato è: {risultato_finale}")
        case "0":
            print("Annullamento in corso...")
            break
        case _:
            print("Numero non riconosciuto.")