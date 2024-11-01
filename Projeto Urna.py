import tkinter as tk 
window=tk.Tk()
window.title("Urna Eletrônica")
window.geometry("1200x800")

Introdução = tk.Label(text="O que deseja fazer?")
Introdução.pack()

Candidatos= tk.Button(text="Lista dos candidatos")

Votos = []
Partido = ["22","30","16","55","29","80","11","44","50"]
def Urna():
    print(f"O que vc quer fazer na urna?\n Digite 1 para ver os candidatos\n Digite 2 para votar\n Digite 3 para contabilizar os votos\n")
    x=input("")
    if x == "1":
        print("Alexandre Ramagem - 22\n Carol Sponza - 30\n Cyro Garcia - 16\n Eduardo Paes - 55\n Henrique Simonard - 29\n Juliete Pantoja - 80\n Marcelo Queiroz - 11\n Rodrigo Amorim - 44\n Tarcísio Motta - 50\n")
        Urna()
    elif x == "2":
        Voto=input("Digite o número de seu candidato: ")
        if Voto in Partido:
            print("Voto concluido.\n")       
            global Votos
            Votos.append(Voto)
            Urna()
        else:
            print("Candidato não encontrado.\n")
            Urna()
    elif x == "3":
        ContagemDeVotos()
    else:
        print("Opção invalida, tente novamente.")
        Urna()

def ContagemDeVotos():
    Ramagem=0
    Sponza=0
    Garcia=0
    Paes=0
    Simonard=0
    Queiroz=0
    Pantoja=0
    Amorim=0
    Motta=0
    for i in Votos:
        if i == "22":
            Ramagem = (Ramagem + 1)
        elif i=="30":
            Sponza = (Sponza + 1)
        elif i=="16":
            Garcia = (Garcia + 1)
        elif i=="55":
            Paes = (Paes + 1)
        elif i=="29":
            Simonard = (Simonard + 1)
        elif i =="80":
            Pantoja = (Pantoja + 1)
        elif i =="11":
            Queiroz = (Queiroz + 1)
        elif i =="44":
            Amorim = (Amorim+1)
        elif i =="50":
            Motta = (Motta + 1)
        else:
            pass
    print(f"O Alexandre Ramagem recebeu {Ramagem} votos")
    print(f"A Carol Sponza recebeu {Sponza} votos")
    print(f"O Cyro Garcia recebeu {Garcia} votos")
    print(f"O Eduardo Paes recebeu {Paes} votos")
    print(f"O Fernando Simonard recebeu {Simonard} votos")
    print(f"A Juliette Pantoja recebeu {Pantoja} votos")
    print(f"O Marcelo queiroz recebeu {Queiroz} votos")
    print(f"O Rodrigo Amorim recebeu {Amorim} votos")
    print(f"O Tarcisio Motta recebeu {Motta} votos")

Urna()