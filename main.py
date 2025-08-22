import time

class Tamaghosi:
    def __init__(self, nome: str):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0
        
    def alimentar(self):
        self.fome -= 10
        self.fome = max(0, self.fome)  # evita valores negativos
        print(f"{self.nome} foi alimentado. Fome agora: {int(self.fome)}")
   

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.tedio -= self.tedio * (quantidade / 100)
            print(f"{self.nome} brincou. Seu tédio agora é {int(self.tedio)}.")

    def getHumor(self):
        humor = 100 - ((self.fome + self.tedio) / 2)
        if humor >= 80:
            return "Muito Feliz"
        elif humor >= 50:
            return "Feliz"
        elif humor >= 20:
            return "Triste"
        else:
            return "Bravo"

    def vida(self):
        #aumenta a perda de saúde baseado no tanto de fome e tédio
        if self.fome > 90 or self.tedio > 90:
            self.saude -= 20
            print(f"Alerta, a saúde de {self.nome} está baixa")
        elif self.fome > 70 or self.tedio > 70:
            self.saude -= 10
            print(f"{self.nome} não está se sentindo bem. A saúde está diminuindo.")
        elif self.fome > 50 or self.tedio > 50:
            self.saude -= 5

        if self.saude <= 0:
            self.saude = 0
            print(f"\n{self.nome} infelizmente faleceu...... Fim de jogo!")
            return False
        
        return True

    def tempoPassando(self):
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5
        self.tedio = min(self.tedio, 100)
        self.fome = min(self.fome, 100)

class Tamaghosi_dragao(Tamaghosi):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.fogo = 50

    def soltar_fogo(self):
        print(f"{self.nome} soltou fogo!")
        self.tedio = max(0, self.tedio - 10)

    def voar(self):
        print(f"{self.nome} está voando! A saúde aumentou um pouco.")
        self.saude = min(100, self.saude + 5)

    def dormir(self):
        print(f"{self.nome} está dormindo na caverna.")
        self.saude = min(100, self.saude + 10)
        self.fome += 5


class TamaghosiRobo(Tamaghosi):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.bateria = 100

    def recarregar(self):
        self.bateria = 100
        print(f"{self.nome} foi recarregado e a bateria está em 100%.")

    def desligar(self):
        print(f"{self.nome} desligou. Bom descanso!")
        self.saude = min(100, self.saude + 10)
        self.bateria = max(0, self.bateria - 10)

    def cantar(self):
        print(f"{self.nome} está cantando 'Bily Jean' de Michael Jackson.")
        self.tedio = max(0, self.tedio - 15)


class Tamaghosi_Bruxo(Tamaghosi):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.forca = 100

    def lancar_Magia(self):
        print(f"{self.nome} lançou o feitiço 'Lumos', o ambiente ficou mais claro!")
        self.tedio = max(0, self.tedio - 10)

    def casa(self):
        print(f"{self.nome} foi para a melhor casa (Grifinória).")
        self.saude = min(100, self.saude + 5)
        self.fome += 5

    def usarVarinha(self):
        print(f"{self.nome} usou a varinha 'Relíquias da Morte'.")
        self.tedio = max(0, self.tedio - 20)


def main():
    """
    Função principal que executa o jogo do Tamaghosi.
    """
    print("Bem-vindo ao Tamaghosi!")
    print("Escolha o tipo do seu bichinho:")
    print("1. Dragão")
    print("2. Robô")
    print("3. Bruxo")
    
    pet_type = input("Digite o número correspondente: ")
    pet_name = input("Dê um nome ao seu novo bichinho: ")

    pet = None
    if pet_type == '1':
        pet = Tamaghosi_dragao(pet_name)
    elif pet_type == '2':
        pet = TamaghosiRobo(pet_name)
    elif pet_type == '3':
        pet = Tamaghosi_Bruxo(pet_name)
    else:
        print("Opção inválida. Criando um bichinho Tamaghosi padrão.")
        pet = Tamaghosi(pet_name)

    print(f"\n{pet.nome} é seu novo bichinho virtual! Cuide bem dele(a).")

    #loop principal do jogo que continua até o usuário querer sair ou o pet morrer
    while True:
        print("\n--- status do seu pet ---")
        print(f"Nome: {pet.nome}")
        print(f"Saúde: {int(pet.saude)}")
        print(f"Fome: {int(pet.fome)}")
        print(f"Tédio: {int(pet.tedio)}")
        print(f"Humor: {pet.getHumor()}")

        print("\nO que você quer fazer?")
        print("1. Alimentar")
        print("2. Brincar")
        
        #prompt pra exibir pra cada tipo de pet
        if isinstance(pet, Tamaghosi_dragao): # o insistance verifica qual é o tipo do pet para mostrar suas ações exclusivas no prompt

            print("3. Soltar fogo")
            print("4. Voar")
            print("5. Dormir")
        elif isinstance(pet, TamaghosiRobo):
            print("3. Recarregar")
            print("4. Desligar")
            print("5. Cantar")
        elif isinstance(pet, Tamaghosi_Bruxo):
            print("3. Lançar magia")
            print("4. Visitar a casa")
            print("5. Usar varinha")
            
        print("6. Sair do jogo")

        choice = input("Digite sua escolha: ")

        if choice == '1':
            pet.alimentar()
        elif choice == '2':
            pet.brincar(50)
        elif isinstance(pet, Tamaghosi_dragao) and choice == '3': #o end garante que a ação ssó executa se o pet for do tipo correto e o usuário tiver escolhido a opção certa

            pet.soltar_fogo()
        elif isinstance(pet, Tamaghosi_dragao) and choice == '4':
            pet.voar()
        elif isinstance(pet, Tamaghosi_dragao) and choice == '5':
            pet.dormir()
        elif isinstance(pet, TamaghosiRobo) and choice == '3':
            pet.recarregar()
        elif isinstance(pet, TamaghosiRobo) and choice == '4':
            pet.desligar()
        elif isinstance(pet, TamaghosiRobo) and choice == '5':
            pet.cantar()
        elif isinstance(pet, Tamaghosi_Bruxo) and choice == '3':
            pet.lancar_Magia()
        elif isinstance(pet, Tamaghosi_Bruxo) and choice == '4':
            pet.casa()
        elif isinstance(pet, Tamaghosi_Bruxo) and choice == '5':
            pet.usarVarinha()
        elif choice == '6':
            print(f"Obrigado por jogar! Tchau, {pet.nome}!")
            break
        else:
            print("Escolha inválida, por favor tente novamente.")
        
        #o tempo passa e o estado do pet muda
        pet.tempoPassando()
        
        #verifica se o pet está vivo, se não tiver, o loop acaba
        if not pet.vida():
            break
            
        time.sleep(1) #pausa por 1 segundo pra simular o tempo passando

if __name__ == "__main__":
    main()



# --- Lógica das contas do programa ---

# Alimentar -> reduz a fome em uma porcentagem.
# Ex: fome = 40, alimentar(50) -> fome cai 50% -> nova fome = 20.

# Brincar -> reduz o tédio em uma porcentagem
# Ex: tédio = 60, brincar(50) -> tédio cai 50% -> novo tédio = 30.

# Humor -> calculado pela média da fome e do tédio.
# Fórmula: humor = 100 - ((fome + tédio) / 2)
# Quanto menor fome + tédio, melhor o humor.

# Tempo passando (a cada rodada):
# - idade aumenta +0.2
# - fome aumenta +5
# - tédio aumenta +2.5
# (valores limitados até 100)

# Saúde -> cai dependendo do nível de fome/tédio:
# - acima de 50 -> perde 5
# - acima de 70 -> perde 10
# - acima de 90 -> perde 20
# - se saúde chegar a 0 -> bichinho morre

# Ações especiais (dependem do tipo de pet):
# Dragão -> soltar fogo (-10 tédio), voar (+5 saúde), dormir (+10 saúde, +5 fome)
# Robô   -> recarregar (bateria = 100), desligar (+10 saúde, -10 bateria), cantar (-15 tédio)
# Bruxo  -> lançar magia (-10 tédio), visitar casa (+5 saúde, +5 fome), usar varinha (-20 tédio)
