import tkinter as tk
from tkinter import messagebox

class UrnaEletronica:
    def __init__(self, master):
        self.master = master
        self.master.title("Escolha seu candidato a prefeito")
        self.master.geometry("1280x600")

        self.votos = {22: 0, 30: 0, 16: 0, 55: 0, 29:0, 80:0, 11:0, 44:0, 50:0, 'nulo': 0}
        self.total_votos = 0
        self.votos_restantes = 10
        self.candidatos_segundo_turno = []

        

        # Nome dos candidatos
        self.nomes_candidatos = {
            22: "Alexandre Ramagem",
            30: "Carol Sponza",
            16: "Cyro Garcia",
            55: "Eduardo Paes",
            29: "Henrique Simonard",
            80: "Juliete Pantoja",
            11: "Marcelo Queiroz",
            44: "Rodrigo Amorim",
            50: "Tarcísio Motta"
        }

        self.atualiza_instrucoes()

        # Campo de entrada
        self.entrada_candidato = tk.Entry(master, font=("Arial", 16), width=5)
        self.entrada_candidato.pack(pady=10)

        # Botão para confirmar voto
        self.botao_confirmar = tk.Button(master, text="Confirmar Voto", command=self.confirmar_voto, width=20, height=2, bg='green', fg='white')
        self.botao_confirmar.pack(pady=20)

        # Área de exibição de resultados
        self.resultado_label = tk.Label(master, text="22 - Alexandre Ramagem 30 - Carol Sponza 16 - Cyro Garcia 55 - Eduardo Paes 29 -Henrique Simonard,80 - Juliete Pantoja,11 - Marcelo Queiroz,44 - Rodrigo Amorim,50 - Tarcísio Motta")
        self.resultado_label.pack(pady=20)

        # Vincula teclas de atalho
        self.master.bind('<Return>', lambda event: self.confirmar_voto())
        self.master.bind('<space>', lambda event: self.votar_nulo())

        # Label de votos restantes
        self.label_votos_restantes = tk.Label(master, text=f"Votos Restantes: {self.votos_restantes}", font=("Arial", 16))
        self.label_votos_restantes.pack(pady=10)


    def atualiza_instrucoes(self):
        instrucoes = ("Digite o número do candidato ou deixe em branco para Voto Nulo:")
        self.label = tk.Label(self.master, text=instrucoes, font=("Arial", 20))
        self.label.pack(pady=20)

    def confirmar_voto(self):
        voto = self.entrada_candidato.get().strip()

        if voto == "":
            self.votar_nulo()
            return
        
        else:
            try:
                candidato = int(voto)
                if candidato not in self.votos:
                    messagebox.showerror("Erro", "Número de candidato inválido. Digite 22, 30, 16, 55, 29, 80, 11, 44, ou 50.")
                    return
            except ValueError:
                messagebox.showerror("Erro", "Por favor, digite um número válido ou deixe em branco para Voto Nulo.")
                return

        if messagebox.askyesno("Confirmação", f"Você tem certeza que deseja votar no {self.nomes_candidatos.get(candidato, 'Voto Nulo')}?"):
            self.votar(candidato)

        self.entrada_candidato.delete(0, tk.END)

    def votar_nulo(self):
        if messagebox.askyesno("Confirmação", "Você tem certeza que deseja votar nulo?"):
            self.votar('nulo')

    def votar(self, candidato):
        if self.total_votos < 10:
            self.votos[candidato] += 1
            self.total_votos += 1
            self.votos_restantes -= 1
            self.label_votos_restantes.config(text=f"Votos Restantes: {self.votos_restantes}")
            messagebox.showinfo("Voto Registrado", f"Parabéns, seu voto foi registrado como {self.nomes_candidatos.get(candidato, 'Voto Nulo')}!")

            if self.total_votos == 10:  # Se o total de votos atingir 10
                self.finalizar_votacao()
        else:
            messagebox.showinfo("Eleições Encerradas", "As eleições foram encerradas. Não há mais votos permitidos.")

    def finalizar_votacao(self):
        max_votos = max(self.votos.values())
        candidatos_empate = [candidato for candidato, votos in self.votos.items() if votos == max_votos and candidato != 'nulo']

        if len(candidatos_empate) > 1:
            self.iniciar_segundo_turno(candidatos_empate)
        else:
            vencedor = candidatos_empate[0] if candidatos_empate else None
            self.limpar_tela_e_exibir_vencedor(vencedor)

    def limpar_tela_e_exibir_vencedor(self, vencedor):
        # Limpa a tela
        self.label.config(text="")
        self.resultado_label.config(text="")
        self.label_votos_restantes.config(text="")

        if vencedor:
            messagebox.showinfo("Eleições Encerradas", f"Vencedor: {self.nomes_candidatos[vencedor]}!\n\n O seu prefeito é: {self.nomes_candidatos[vencedor]}!")
        else:
            messagebox.showinfo("Eleições Encerradas", "Não houve vencedor.")

    def iniciar_segundo_turno(self, candidatos):
        self.votos = {candidato: 0 for candidato in candidatos}
        self.total_votos = 0
        self.votos_restantes = 10
        self.label_votos_restantes.config(text=f"Votos Restantes: {self.votos_restantes}")

        self.candidatos_segundo_turno = candidatos
        candidatos_str = ', '.join(self.nomes_candidatos[candidato] for candidato in candidatos)
        messagebox.showinfo("Segundo Turno", f"Houve um empate! Iniciando segundo turno entre: {candidatos_str}")

        # Atualiza a interface para o segundo turno
        self.label.config(text=f"Digite o número do candidato (1: {self.nomes_candidatos[candidatos[0]]}, 2: {self.nomes_candidatos[candidatos[1]]}):")
        self.resultado_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = UrnaEletronica(root)
    root.mainloop()
