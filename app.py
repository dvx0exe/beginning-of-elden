import mysql.connector
from mysql.connector import Error
import json
import bcrypt
import os
from dotenv import load_dotenv 

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

class Personagem:
    def __init__(self, nome, idade, classe):
        self.nome = nome  
        self.idade = idade
        self.classe = classe
        self.raca = ""
        self.vigor = 0
        self.mente = 0
        self.fortitude = 0
        self.forca = 0
        self.destreza = 0
        self.inteligencia = 0
        self.fe = 0
        self.arcano = 0
        self.build_escolhida = ""
        self.equipamento = []
        self.roupas = []
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode ser vazio!")
        self._nome = valor

    def __str__(self):
        msg = f"Nome: {self.nome}\n"
        msg += f"Idade: {self.idade}\n"
        msg += f"Classe: {self.classe}\n"
        msg += f"Raça: {self.raca}\n"
        msg += f"Vigor: {self.vigor}\n"
        msg += f"Mente: {self.mente}\n"
        msg += f"Fortitude: {self.fortitude}\n"
        msg += f"Força: {self.forca}\n"
        msg += f"Destreza: {self.destreza}\n"
        msg += f"Inteligência: {self.inteligencia}\n"
        msg += f"Fé: {self.fe}\n"
        msg += f"Arcano: {self.arcano}\n"
        msg += "Equipamento: " + ", ".join(self.equipamento) + "\n"
        msg += "Roupas: " + ", ".join(self.roupas) + "\n"
        msg += f"Build escolhida: {self.build_escolhida or 'Nenhuma'}\n"
        return msg

class Heroi(Personagem):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "Heroi")
        self.vigor = 14
        self.mente = 9
        self.fortitude = 12
        self.forca = 16
        self.destreza = 9
        self.inteligencia = 7
        self.fe = 8
        self.arcano = 11
        self.equipamento = ["Machado de batalha", "Escudo de couro"]

class Bandido(Personagem):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "Bandido")
        self.vigor = 10
        self.mente = 11
        self.fortitude = 10
        self.forca = 9
        self.destreza = 13
        self.inteligencia = 9
        self.fe = 8
        self.arcano = 14
        self.equipamento = ["Faca", "Arco curto", "Broquel", "Flecha de osso"]

class Astrologo(Personagem):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "Astrologo")
        self.vigor = 9
        self.mente = 15
        self.fortitude = 9
        self.forca = 8
        self.destreza = 12
        self.inteligencia = 16
        self.fe = 7
        self.arcano = 9
        self.equipamento = ["Cajado", "Espada curta", "Escudo"]

class Guerreiro(Personagem):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "Guerreiro")
        self.vigor = 11
        self.mente = 12
        self.fortitude = 11
        self.forca = 10
        self.destreza = 16
        self.inteligencia = 10
        self.fe = 8
        self.arcano = 9
        self.equipamento = ["2 Cimitarras", "Broquel", "Vestimentas de pano azul"]

class Prisioneiro(Personagem):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "Prisioneiro")
        self.vigor = 11
        self.mente = 12
        self.fortitude = 11
        self.forca = 11
        self.destreza = 14
        self.inteligencia = 14
        self.fe = 6
        self.arcano = 9
        self.equipamento = ["Estoc", "Cajado", "Escudo"]

class Confessor(Personagem):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "Confessor")
        self.vigor = 10
        self.mente = 13
        self.fortitude = 10
        self.forca = 12
        self.destreza = 12
        self.inteligencia = 9
        self.fe = 14
        self.arcano = 9
        self.equipamento = ["Espada larga", "Escudo", "Selo de dedo"]

class Miseravel(Personagem):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "Miseravel")
        self.vigor = 10
        self.mente = 10
        self.fortitude = 10
        self.forca = 10
        self.destreza = 10
        self.inteligencia = 10
        self.fe = 10
        self.arcano = 10
        self.equipamento = ["Porrete"]

class Vagabundo(Personagem):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "Vagabundo")
        self.vigor = 15
        self.mente = 10
        self.fortitude = 11
        self.forca = 14
        self.destreza = 13
        self.inteligencia = 9
        self.fe = 9
        self.arcano = 7
        self.equipamento = ["Espada longa", "Alabarda", "Escudo"]

class Profeta(Personagem):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "Profeta")
        self.vigor = 10
        self.mente = 14
        self.fortitude = 8
        self.forca = 12
        self.destreza = 8
        self.inteligencia = 7
        self.fe = 16
        self.arcano = 11
        self.equipamento = ["Lança", "Selo de dedo", "Escudo de Rickety", "Feitiço de cura"]

class Samurai(Personagem):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "Samurai")
        self.vigor = 12
        self.mente = 11
        self.fortitude = 13
        self.forca = 12
        self.destreza = 15
        self.inteligencia = 9
        self.fe = 8
        self.arcano = 8
        self.equipamento = ["Uchigatana", "Arco longo", "Escudo redondo de espinho vermelho", "Flechas de osso"]

class Builds:
    @staticmethod
    def build_heroi(personagem):
        escolha = input("Digite o número da build desejada para Herói (1-3): ")
        if escolha == "1":
            personagem.forca += 20
            personagem.vigor += 18
            personagem.fortitude += 15
            personagem.roupas.append("Armadura de Cavaleiro")
            personagem.equipamento.append("Espada Lendária")
            return "Força do Destino"
        elif escolha == "2":
            personagem.forca += 18
            personagem.destreza += 16
            personagem.vigor += 14
            personagem.roupas.append("Cota de Malha Real")
            personagem.equipamento.append("Machado de Guerra")
            return "Espírito Indomável"
        elif escolha == "3":
            personagem.forca += 22
            personagem.vigor += 16
            personagem.fortitude += 14
            personagem.roupas.append("Túnica do Herói")
            personagem.equipamento.append("Martelo de Guerra")
            return "Herói Ancestral"
        print("Build inválida! Usando 'Nenhuma' como padrão.")
        return "Nenhuma"

    @staticmethod
    def build_bandido(personagem):
        escolha = input("Digite o número da build desejada para Bandido (1-3): ")
        if escolha == "1":
            personagem.destreza += 20
            personagem.arcano += 12
            personagem.vigor += 10
            personagem.roupas.append("Manto das Sombras")
            personagem.equipamento.append("Adaga Silenciosa")
            return "Sombra Ardilosa"
        elif escolha == "2":
            personagem.destreza += 18
            personagem.mente += 16
            personagem.vigor += 12
            personagem.roupas.append("Vestimenta Leves")
            personagem.equipamento.append("Espada Curta")
            return "Lâmina Veloz"
        elif escolha == "3":
            personagem.destreza += 19
            personagem.arcano += 14
            personagem.vigor += 11
            personagem.roupas.append("Capuz do Ladrão")
            personagem.equipamento.append("Punhal de Assassino")
            return "Golpe Furtivo"
        print("Build inválida!")
        return "Nenhuma"

    @staticmethod
    def build_astrologo(personagem):
        escolha = input("Digite o número da build desejada para Astrólogo (1-3): ")
        if escolha == "1":
            personagem.inteligencia += 22
            personagem.mente += 20
            personagem.arcano += 15
            personagem.roupas.append("Robe Celestial")
            personagem.equipamento.append("Cajado da Aurora")
            return "Visão Estelar"
        elif escolha == "2":
            personagem.inteligencia += 20
            personagem.mente += 18
            personagem.arcano += 18
            personagem.roupas.append("Manto do Cosmos")
            personagem.equipamento.append("Vara Arcana")
            return "Mente Cósmica"
        elif escolha == "3":
            personagem.inteligencia += 24
            personagem.mente += 16
            personagem.arcano += 16
            personagem.roupas.append("Túnica de Estrelas")
            personagem.equipamento.append("Cajado Estelar")
            return "Conjurador Celestial"
        print("Build inválida!")
        return "Nenhuma"

    @staticmethod
    def build_guerreiro(personagem):
        escolha = input("Digite o número da build desejada para Guerreiro (1-3): ")
        if escolha == "1":
            personagem.forca += 18
            personagem.destreza += 15
            personagem.vigor += 16
            personagem.roupas.append("Armadura de Ferro")
            personagem.equipamento.append("Espada Grande")
            return "Fúria de Batalha"
        elif escolha == "2":
            personagem.forca += 16
            personagem.destreza += 18
            personagem.vigor += 14
            personagem.roupas.append("Cota de Aço")
            personagem.equipamento.append("Sabre de Aço")
            return "Disciplina de Aço"
        elif escolha == "3":
            personagem.forca += 17
            personagem.vigor += 20
            personagem.fortitude += 15
            personagem.roupas.append("Armadura Pesada")
            personagem.equipamento.append("Machado Pesado")
            return "Guardião de Ferro"
        print("Build inválida!")
        return "Nenhuma"

    @staticmethod
    def build_prisioneiro(personagem):
        escolha = input("Digite o número da build desejada para Prisioneiro (1-3): ")
        if escolha == "1":
            personagem.destreza += 18
            personagem.inteligencia += 14
            personagem.vigor += 12
            personagem.roupas.append("Vestimenta de Recluso")
            personagem.equipamento.append("Estoc Ágil")
            return "Redenção Sombria"
        elif escolha == "2":
            personagem.forca += 16
            personagem.destreza += 16
            personagem.vigor += 14
            personagem.roupas.append("Roupas de Fuga")
            personagem.equipamento.append("Espada Curta")
            return "Liberdade Conquistada"
        elif escolha == "3":
            personagem.destreza += 20
            personagem.mente += 12
            personagem.vigor += 12
            personagem.roupas.append("Manto do Rebelde")
            personagem.equipamento.append("Adaga Rápida")
            return "Espírito Rebelde"
        print("Build inválida!")
        return "Nenhuma"

    @staticmethod
    def build_confessor(personagem):
        escolha = input("Digite o número da build desejada para Confessor (1-3): ")
        if escolha == "1":
            personagem.fe += 22
            personagem.vigor += 16
            personagem.inteligencia += 10
            personagem.roupas.append("Vestes Sagradas")
            personagem.equipamento.append("Espada Sagrada")
            return "Devoto da Luz"
        elif escolha == "2":
            personagem.fe += 20
            personagem.fortitude += 18
            personagem.vigor += 14
            personagem.roupas.append("Armadura do Confessor")
            personagem.equipamento.append("Martelo Sagrado")
            return "Guardião da Fé"
        elif escolha == "3":
            personagem.fe += 24
            personagem.vigor += 14
            personagem.inteligencia += 12
            personagem.roupas.append("Manto do Redentor")
            personagem.equipamento.append("Cajado Divino")
            return "Redentor Sagrado"
        print("Build inválida!")
        return "Nenhuma"

    @staticmethod
    def build_miseravel(personagem):
        escolha = input("Digite o número da build desejada para Miserável (1-3): ")
        if escolha == "1":
            personagem.forca += 14
            personagem.vigor += 18
            personagem.mente += 12
            personagem.roupas.append("Traje do Renascido")
            personagem.equipamento.append("Porrete Modificado")
            return "Renascido na Dor"
        elif escolha == "2":
            personagem.forca += 16
            personagem.vigor += 16
            personagem.destreza += 12
            personagem.roupas.append("Vestimenta do Sobrevivente")
            personagem.equipamento.append("Clava de Adversidade")
            return "Caminho da Adversidade"
        elif escolha == "3":
            personagem.vigor += 20
            personagem.mente += 14
            personagem.fortitude += 12
            personagem.roupas.append("Armadura Resiliente")
            personagem.equipamento.append("Maça Pesada")
            return "Espírito Resiliente"
        print("Build inválida!")
        return "Nenhuma"

    @staticmethod
    def build_vagabundo(personagem):
        escolha = input("Digite o número da build desejada para Vagabundo (1-3): ")
        if escolha == "1":
            personagem.destreza += 18
            personagem.vigor += 14
            personagem.arcano += 12
            personagem.roupas.append("Manto do Errante")
            personagem.equipamento.append("Espada Curta")
            return "Errante das Sombras"
        elif escolha == "2":
            personagem.destreza += 16
            personagem.vigor += 16
            personagem.forca += 14
            personagem.roupas.append("Capa do Andarilho")
            personagem.equipamento.append("Sabre Tempestuoso")
            return "Andarilho da Tempestade"
        elif escolha == "3":
            personagem.destreza += 17
            personagem.vigor += 15
            personagem.forca += 13
            personagem.roupas.append("Traje Errante")
            personagem.equipamento.append("Adaga Versátil")
            return "Destino Errante"
        print("Build inválida!")
        return "Nenhuma"

    @staticmethod
    def build_profeta(personagem):
        escolha = input("Digite o número da build desejada para Profeta (1-3): ")
        if escolha == "1":
            personagem.fe += 24
            personagem.mente += 16
            personagem.arcano += 14
            personagem.roupas.append("Vestes do Profeta")
            personagem.equipamento.append("Lança Profética")
            return "Voz do Apocalipse"
        elif escolha == "2":
            personagem.fe += 22
            personagem.arcano += 18
            personagem.mente += 14
            personagem.roupas.append("Manto Visionário")
            personagem.equipamento.append("Cajado Oracular")
            return "Visões do Futuro"
        elif escolha == "3":
            personagem.fe += 26
            personagem.arcano += 16
            personagem.vigor += 12
            personagem.roupas.append("Túnica do Selo")
            personagem.equipamento.append("Espada dos Destinos")
            return "Selo do Destino"
        print("Build inválida!")
        return "Nenhuma"

    @staticmethod
    def build_samurai(personagem):
        escolha = input("Digite o número da build desejada para Samurai (1-3): ")
        if escolha == "1":
            personagem.destreza += 20
            personagem.vigor += 16
            personagem.forca += 14
            personagem.roupas.append("Armadura do Samurai")
            personagem.equipamento.append("Uchigatana")
            return "Caminho do Bushido"
        elif escolha == "2":
            personagem.destreza += 18
            personagem.vigor += 14
            personagem.forca += 13
            personagem.roupas.append("Vestimenta de Combate")
            personagem.equipamento.append("Katana Ligeira")
            return "Espírito Cortante"
        elif escolha == "3":
            personagem.destreza += 17
            personagem.vigor += 18
            personagem.forca += 15
            personagem.roupas.append("Traje do Honorável")
            personagem.equipamento.append("Katana Ancestral")
            return "Honra Eterna"
        print("Build inválida!")
        return "Nenhuma"

class TextBuild:
    @staticmethod
    def text_Heroi():
        return """
        ================================================== BUILDS PARA HERÓI ==================================================
        1 - Força do Destino
        Descrição: Build focada em alta força e vigor, ideal para combates diretos.
        Atributos recomendados: Força +20, Vigor +18, Fortitude +15.
        Roupas: Armadura de Cavaleiro (Vigor +2, Fortitude +1).
        Armas: Espada Lendária (Força +3, Vigor +1).
        ----------------------------------------------------------------------------------------------------
        2 - Espírito Indomável
        Descrição: Combina força bruta com agilidade para ataques rápidos e certeiros.
        Atributos recomendados: Força +18, Destreza +16, Vigor +14.
        Roupas: Cota de Malha Real (Destreza +2, Vigor +1).
        Armas: Machado de Guerra (Força +2, Destreza +2).
        ----------------------------------------------------------------------------------------------------
        3 - Herói Ancestral
        Descrição: Foco em combate corpo a corpo com ênfase na resistência e no dano físico.
        Atributos recomendados: Força +22, Vigor +16, Fortitude +14.
        Roupas: Túnica do Herói (Força +1, Vigor +1).
        Armas: Martelo de Guerra (Força +4, Fortitude +1).
        ----------------------------------------------------------------------------------------------------
        """

    @staticmethod
    def text_Bandido():
        return """
        ================================================== BUILDS PARA BANDIDO ==================================================
        1 - Sombra Ardilosa
        Descrição: Especialista em furtividade e ataques surpresa, explorando brechas inimigas.
        Atributos recomendados: Destreza +20, Arcano +12, Vigor +10.
        Roupas: Manto das Sombras (Destreza +2, Arcano +1).
        Armas: Adaga Silenciosa (Destreza +3, Arcano +1).
        ----------------------------------------------------------------------------------------------------
        2 - Lâmina Veloz
        Descrição: Build com foco em velocidade e precisão, perfeita para golpes rápidos.
        Atributos recomendados: Destreza +18, Mente +16, Vigor +12.
        Roupas: Vestes Leves (Destreza +2, Mente +1).
        Armas: Espada Curta (Destreza +3, Mente +1).
        ----------------------------------------------------------------------------------------------------
        3 - Golpe Furtivo
        Descrição: Aproveita ataques críticos e golpes de surpresa para eliminar o adversário.
        Atributos recomendados: Destreza +19, Arcano +14, Vigor +11.
        Roupas: Capuz do Ladrão (Arcano +2, Destreza +1).
        Armas: Punhal de Assassino (Destreza +3, Arcano +1).
        ----------------------------------------------------------------------------------------------------
        """

    @staticmethod
    def text_Astrologo():
        return """
        ================================================== BUILDS PARA ASTRÓLOGO ==================================================
        1 - Visão Estelar
        Descrição: Concentra-se em inteligência e mente para conjurar feitiços devastadores.
        Atributos recomendados: Inteligência +22, Mente +20, Arcano +15.
        Roupas: Robe Celestial (Inteligência +2, Mente +2).
        Armas: Cajado da Aurora (Inteligência +3, Arcano +2).
        ----------------------------------------------------------------------------------------------------
        2 - Mente Cósmica
        Descrição: Equilíbrio entre magia ofensiva e defesa mental, ideal para controlar a batalha.
        Atributos recomendados: Inteligência +20, Mente +18, Arcano +18.
        Roupas: Manto do Cosmos (Mente +2, Arcano +2).
        Armas: Vara Arcana (Inteligência +3, Mente +1).
        ----------------------------------------------------------------------------------------------------
        3 - Conjurador Celestial
        Descrição: Especialista em encantamentos à distância com feitiços precisos.
        Atributos recomendados: Inteligência +24, Mente +16, Arcano +16.
        Roupas: Túnica de Estrelas (Inteligência +2, Arcano +1).
        Armas: Cajado Estelar (Inteligência +4, Mente +1).
        ----------------------------------------------------------------------------------------------------
        """

    @staticmethod
    def text_Guerreiro():
        return """
        ================================================== BUILDS PARA GUERREIRO ==================================================
        1 - Fúria de Batalha
        Descrição: Build agressiva focada em ataques devastadores e alto dano físico.
        Atributos recomendados: Força +18, Destreza +15, Vigor +16.
        Roupas: Armadura de Ferro (Força +1, Vigor +2).
        Armas: Espada Grande (Força +4, Destreza +1).
        ----------------------------------------------------------------------------------------------------
        2 - Disciplina de Aço
        Descrição: Equilíbrio entre técnica e poder, usando espada com precisão letal.
        Atributos recomendados: Força +16, Destreza +18, Vigor +14.
        Roupas: Cota de Aço (Destreza +2, Vigor +1).
        Armas: Sabre de Aço (Força +3, Destreza +2).
        ----------------------------------------------------------------------------------------------------
        3 - Guardião de Ferro
        Descrição: Concentra-se na defesa robusta e em contra-ataques poderosos.
        Atributos recomendados: Força +17, Vigor +20, Fortitude +15.
        Roupas: Armadura Pesada (Vigor +3, Fortitude +2).
        Armas: Machado Pesado (Força +3, Fortitude +1).
        ----------------------------------------------------------------------------------------------------
        """

    @staticmethod
    def text_Prisioneiro():
        return """
        ================================================== BUILDS PARA PRISIONEIRO ==================================================
        1 - Redenção Sombria
        Descrição: Aproveita a agilidade e astúcia do prisioneiro para golpes furtivos.
        Atributos recomendados: Destreza +18, Inteligência +14, Vigor +12.
        Roupas: Vestimenta de Recluso (Destreza +2, Inteligência +1).
        Armas: Estoc Ágil (Destreza +3, Inteligência +1).
        ----------------------------------------------------------------------------------------------------
        2 - Liberdade Conquistada
        Descrição: Equilibra força e destreza para superar adversidades.
        Atributos recomendados: Força +16, Destreza +16, Vigor +14.
        Roupas: Roupas de Fuga (Força +1, Destreza +2).
        Armas: Espada Curta (Força +2, Destreza +2).
        ----------------------------------------------------------------------------------------------------
        3 - Espírito Rebelde
        Descrição: Foca em ataques rápidos e evasão para surpreender o inimigo.
        Atributos recomendados: Destreza +20, Mente +12, Vigor +12.
        Roupas: Manto do Rebelde (Destreza +2, Mente +1).
        Armas: Adaga Rápida (Destreza +3, Mente +1).
        ----------------------------------------------------------------------------------------------------
        """

    @staticmethod
    def text_Confessor():
        return """
        ================================================== BUILDS PARA CONFESSOR ==================================================
        1 - Devoto da Luz
        Descrição: Build centrada em fé para curas e ataques divinos com foco em milagres.
        Atributos recomendados: Fé +22, Vigor +16, Inteligência +10.
        Roupas: Vestes Sagradas (Fé +2, Vigor +1).
        Armas: Espada Sagrada (Fé +3, Vigor +1).
        ----------------------------------------------------------------------------------------------------
        2 - Guardião da Fé
        Descrição: Equilibra defesa e ataque usando o poder da fé para abater inimigos.
        Atributos recomendados: Fé +20, Fortitude +18, Vigor +14.
        Roupas: Armadura do Confessor (Fé +2, Fortitude +1).
        Armas: Martelo Sagrado (Fé +3, Fortitude +1).
        ----------------------------------------------------------------------------------------------------
        3 - Redentor Sagrado
        Descrição: Transforma a fé em dano e suporte com bênçãos e milagres.
        Atributos recomendados: Fé +24, Vigor +14, Inteligência +12.
        Roupas: Manto do Redentor (Fé +2, Inteligência +1).
        Armas: Cajado Divino (Fé +4, Vigor +1).
        ----------------------------------------------------------------------------------------------------
        """

    @staticmethod
    def text_Miseravel():
        return """
        ================================================== BUILDS PARA MISERÁVEL ==================================================
        1 - Renascido na Dor
        Descrição: Transforma a adversidade em poder com equilíbrio físico e mental.
        Atributos recomendados: Força +14, Vigor +18, Mente +12.
        Roupas: Traje do Renascido (Vigor +2, Mente +1).
        Armas: Porrete Modificado (Força +2, Vigor +1).
        ----------------------------------------------------------------------------------------------------
        2 - Caminho da Adversidade
        Descrição: Resistência e uso da dor para impulsionar ataques.
        Atributos recomendados: Força +16, Vigor +16, Destreza +12.
        Roupas: Vestimenta do Sobrevivente (Força +1, Vigor +2).
        Armas: Clava de Adversidade (Força +3, Destreza +1).
        ----------------------------------------------------------------------------------------------------
        3 - Espírito Resiliente
        Descrição: Maximiza resistência física e mental para batalhas prolongadas.
        Atributos recomendados: Vigor +20, Mente +14, Fortitude +12.
        Roupas: Armadura Resiliente (Vigor +3, Fortitude +1).
        Armas: Maça Pesada (Força +2, Fortitude +2).
        ----------------------------------------------------------------------------------------------------
        """

    @staticmethod
    def text_Vagabundo():
        return """
        ================================================== BUILDS PARA VAGABUNDO ==================================================
        1 - Errante das Sombras
        Descrição: Explora mobilidade e ataques surpresa para confundir inimigos.
        Atributos recomendados: Destreza +18, Vigor +14, Arcano +12.
        Roupas: Manto do Errante (Destreza +2, Arcano +1).
        Armas: Espada Curta (Destreza +3, Vigor +1).
        ----------------------------------------------------------------------------------------------------
        2 - Andarilho da Tempestade
        Descrição: Combina velocidade e força para golpes relâmpago e evasão rápida.
        Atributos recomendados: Destreza +16, Vigor +16, Força +14.
        Roupas: Capa do Andarilho (Destreza +2, Força +1).
        Armas: Sabre Tempestuoso (Destreza +3, Força +1).
        ----------------------------------------------------------------------------------------------------
        3 - Destino Errante
        Descrição: Versátil equilibrando agilidade com força bruta para diferentes situações.
        Atributos recomendados: Destreza +17, Vigor +15, Força +13.
        Roupas: Traje Errante (Destreza +2, Vigor +1).
        Armas: Adaga Versátil (Destreza +3, Força +1).
        ----------------------------------------------------------------------------------------------------
        """

    @staticmethod
    def text_Profeta():
        return """
        ================================================== BUILDS PARA PROFETA ==================================================
        1 - Voz do Apocalipse
        Descrição: Canaliza profecias destrutivas e feitiços devastadores com fé.
        Atributos recomendados: Fé +24, Mente +16, Arcano +14.
        Roupas: Vestes do Profeta (Fé +2, Arcano +1).
        Armas: Lança Profética (Fé +3, Mente +1).
        ----------------------------------------------------------------------------------------------------
        2 - Visões do Futuro
        Descrição: Prevê e manipula o campo de batalha com rituais místicos.
        Atributos recomendados: Fé +22, Arcano +18, Mente +14.
        Roupas: Manto Visionário (Arcano +2, Mente +1).
        Armas: Cajado Oracular (Fé +3, Arcano +1).
        ----------------------------------------------------------------------------------------------------
        3 - Selo do Destino
        Descrição: Altera o rumo do combate com rituais antigos e poder místico.
        Atributos recomendados: Fé +26, Arcano +16, Vigor +12.
        Roupas: Túnica do Selo (Fé +2, Vigor +1).
        Armas: Espada dos Destinos (Fé +4, Arcano +1).
        ----------------------------------------------------------------------------------------------------
        """

    @staticmethod
    def text_Samurai():
        return """
        ================================================== BUILDS PARA SAMURAI ==================================================
        1 - Caminho do Bushido
        Descrição: Precisão e disciplina com espadas, mantendo honra e equilíbrio.
        Atributos recomendados: Destreza +20, Vigor +16, Força +14.
        Roupas: Armadura do Samurai (Destreza +2, Vigor +1).
        Armas: Uchigatana (Destreza +3, Força +1).
        ----------------------------------------------------------------------------------------------------
        2 - Espírito Cortante
        Descrição: Ataques rápidos e cortes precisos priorizando agilidade.
        Atributos recomendados: Destreza +18, Vigor +14, Força +13.
        Roupas: Vestimenta de Combate (Destreza +2, Vigor +1).
        Armas: Katana Ligeira (Destreza +3, Força +1).
        ----------------------------------------------------------------------------------------------------
        3 - Honra Eterna
        Descrição: Tradição e poder para defesas sólidas e contra-ataques precisos.
        Atributos recomendados: Destreza +17, Vigor +18, Força +15.
        Roupas: Traje do Honorável (Vigor +2, Força +1).
        Armas: Katana Ancestral (Destreza +3, Força +1).
        ----------------------------------------------------------------------------------------------------
        """

def criar_conexao():
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        return conexao
    except Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None

def registrar_usuario():
    login = input("Digite um nome de usuário: ").strip()
    if not login:
        print("Nome de usuário não pode ser vazio!")
        return
    senha = input("Digite uma senha: ").strip()
    if not senha:
        print("Senha não pode ser vazia!")
        return
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    
    try:
        conexao = criar_conexao()
        if conexao is None:
            return
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO usuarios (login, senha) VALUES (%s, %s)", (login, senha_hash))
        conexao.commit()
        print("Usuário registrado com sucesso!")
    except Error as err:
        print(f"Erro ao registrar usuário: {err}")
    finally:
        if 'conexao' in locals() and conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

def login_usuario():
    login = input("Digite seu usuário: ").strip()
    senha = input("Digite sua senha: ").strip()
    
    try:
        conexao = criar_conexao()
        if conexao is None:
            return None
        cursor = conexao.cursor()
        cursor.execute("SELECT id, senha FROM usuarios WHERE login = %s", (login,))
        resultado = cursor.fetchone()
        
        if resultado and bcrypt.checkpw(senha.encode('utf-8'), resultado[1].encode('utf-8')):
            print("Login bem-sucedido!")
            return resultado[0]
        else:
            print("Usuário ou senha inválidos!")
            return None
    except Error as err:
        print(f"Erro ao fazer login: {err}")
        return None
    finally:
        if 'conexao' in locals() and conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

def salvar_personagem(personagem, usuario_id):
    try:
        conexao = criar_conexao()
        if conexao is None:
            return
        cursor = conexao.cursor()
        
        query = """INSERT INTO personagens (
            usuario_id, nome, idade, classe, raca, 
            vigor, mente, fortitude, forca, destreza, 
            inteligencia, fe, arcano, build_escolhida,
            equipamento, roupas
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        valores = (
            usuario_id,
            personagem.nome,
            personagem.idade,
            personagem.classe,
            personagem.raca,
            personagem.vigor,
            personagem.mente,
            personagem.fortitude,
            personagem.forca,
            personagem.destreza,
            personagem.inteligencia,
            personagem.fe,
            personagem.arcano,
            personagem.build_escolhida,
            json.dumps(personagem.equipamento),
            json.dumps(personagem.roupas)
        )
        
        cursor.execute(query, valores)
        conexao.commit()
        print("Personagem salvo com sucesso!")
    except Error as err:
        print(f"Erro ao salvar personagem: {err}")
    finally:
        if 'conexao' in locals() and conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

def listar_personagens(usuario_id):
    try:
        conexao = criar_conexao()
        if conexao is None:
            return
        cursor = conexao.cursor(dictionary=True)
        
        cursor.execute(
            """SELECT id, nome, idade, classe, raca, build_escolhida, 
            vigor, mente, fortitude, forca, destreza, inteligencia, 
            fe, arcano, equipamento, roupas 
            FROM personagens 
            WHERE usuario_id = %s""",
            (usuario_id,)
        )
        personagens = cursor.fetchall()
        
        if not personagens:
            print("Nenhum personagem encontrado.")
            return
        
        for p in personagens:
            equipamento = json.loads(p['equipamento']) if p['equipamento'] else []
            roupas = json.loads(p['roupas']) if p['roupas'] else []
            print("\n" + "=" * 50)
            print(f"ID: {p['id']}")
            print(f"Nome: {p['nome']}")
            print(f"Idade: {p['idade']}")
            print(f"Classe: {p['classe']}")
            print(f"Raça: {p['raca']}")
            print(f"Build escolhida: {p.get('build_escolhida', 'Nenhuma')}")
            print("\nATRIBUTOS:")
            print(f"  Vigor: {p['vigor']}")
            print(f"  Mente: {p['mente']}")
            print(f"  Fortitude: {p['fortitude']}")
            print(f"  Força: {p['forca']}")
            print(f"  Destreza: {p['destreza']}")
            print(f"  Inteligência: {p['inteligencia']}")
            print(f"  Fé: {p['fe']}")
            print(f"  Arcano: {p['arcano']}")
            print("\nEQUIPAMENTO:")
            print(f"  {', '.join(equipamento) if equipamento else 'Nenhum'}")
            print("\nVESTIMENTAS:")
            print(f"  {', '.join(roupas) if roupas else 'Nenhuma'}")
            print("=" * 50 + "\n")
            
    except Error as err:
        print(f"Erro ao listar personagens: {err}")
    finally:
        if 'conexao' in locals() and conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

def excluir_personagem(usuario_id):
    listar_personagens(usuario_id)
    try:
        personagem_id = int(input("\nDigite o ID do personagem a ser excluído: "))
    except ValueError:
        print("ID inválido! Deve ser um número.")
        return
    
    try:
        conexao = criar_conexao()
        if conexao is None:
            return
        cursor = conexao.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM personagens WHERE id = %s AND usuario_id = %s", (personagem_id, usuario_id))
        personagem = cursor.fetchone()
        
        if not personagem:
            print("Personagem não encontrado ou não pertence ao usuário!")
            return
        
        equipamento = json.loads(personagem['equipamento']) if personagem['equipamento'] else []
        roupas = json.loads(personagem['roupas']) if personagem['roupas'] else []
        print("\nDETALHES DO PERSONAGEM A SER EXCLUÍDO:")
        print(f"ID: {personagem['id']}")
        print(f"Nome: {personagem['nome']}")
        print(f"Idade: {personagem['idade']}")
        print(f"Classe: {personagem['classe']}")
        print(f"Raça: {personagem['raca']}")
        print(f"Build: {personagem.get('build_escolhida', 'Nenhuma')}")
        print(f"Vigor: {personagem['vigor']}")
        print(f"Mente: {personagem['mente']}")
        print(f"Fortitude: {personagem['fortitude']}")
        print(f"Força: {personagem['forca']}")
        print(f"Destreza: {personagem['destreza']}")
        print(f"Inteligência: {personagem['inteligencia']}")
        print(f"Fé: {personagem['fe']}")
        print(f"Arcano: {personagem['arcano']}")
        print(f"Equipamento: {', '.join(equipamento) if equipamento else 'Nenhum'}")
        print(f"Roupas: {', '.join(roupas) if roupas else 'Nenhuma'}")
        print("-" * 50)
        
        confirmacao = input("Tem certeza que deseja excluir este personagem? (s/n): ").strip().lower()
        if confirmacao == 's':
            cursor.execute("DELETE FROM personagens WHERE id = %s AND usuario_id = %s", (personagem_id, usuario_id))
            conexao.commit()
            print("Personagem excluído com sucesso!" if cursor.rowcount > 0 else "Falha na exclusão.")
        else:
            print("Exclusão cancelada.")
            
    except Error as err:
        print(f"Erro ao excluir personagem: {err}")
    finally:
        if 'conexao' in locals() and conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

def criar_personagem(usuario_id):
    nome = input("Digite o nome do personagem: ").strip()
    if not nome:
        print("Nome não pode ser vazio!")
        return
    
    while True:
        try:
            idade = int(input("Digite a idade do personagem: "))
            if idade <= 0:
                raise ValueError("Idade deve ser um número positivo!")
            break
        except ValueError as e:
            print(e if str(e) != "Idade deve ser um número positivo!" else "Idade inválida! Digite um número válido.")

    racas_disponiveis = ["Humano", "Elfo", "Anão", "Orc", "Gato", "Lagarto", "Dragão", "Cyborgue"]
    print("\nRaças disponíveis:", ", ".join(racas_disponiveis))
    raca = input("Digite a raça do personagem: ").capitalize()
    while raca not in racas_disponiveis:
        print("Raça inválida! Tente novamente.")
        raca = input("Digite a raça do personagem: ").capitalize()
    print(f"Raça escolhida: {raca}\n")

    classes_disponiveis = ["Heroi", "Bandido", "Astrologo", "Guerreiro", "Prisioneiro", "Confessor", "Miseravel", "Vagabundo", "Profeta", "Samurai"]
    print("Classes disponíveis:", ", ".join(classes_disponiveis))
    classe_digitada = input("Digite a classe do personagem: ").capitalize()

    BUILD_FUNCTIONS = {
        "Heroi": (Heroi, Builds.build_heroi, TextBuild.text_Heroi),
        "Bandido": (Bandido, Builds.build_bandido, TextBuild.text_Bandido),
        "Astrologo": (Astrologo, Builds.build_astrologo, TextBuild.text_Astrologo),
        "Guerreiro": (Guerreiro, Builds.build_guerreiro, TextBuild.text_Guerreiro),
        "Prisioneiro": (Prisioneiro, Builds.build_prisioneiro, TextBuild.text_Prisioneiro),
        "Confessor": (Confessor, Builds.build_confessor, TextBuild.text_Confessor),
        "Miseravel": (Miseravel, Builds.build_miseravel, TextBuild.text_Miseravel),
        "Vagabundo": (Vagabundo, Builds.build_vagabundo, TextBuild.text_Vagabundo),
        "Profeta": (Profeta, Builds.build_profeta, TextBuild.text_Profeta),
        "Samurai": (Samurai, Builds.build_samurai, TextBuild.text_Samurai),
    }

    if classe_digitada in BUILD_FUNCTIONS:
        classe, build_func, text_func = BUILD_FUNCTIONS[classe_digitada]
        personagem = classe(nome, idade)
        personagem.raca = raca
        print(f"\nClasse escolhida: {classe_digitada}\n")
        print(personagem)
        print(text_func())
        build_nome = build_func(personagem)
        personagem.build_escolhida = build_nome
        print(f"\nBuild escolhida: {build_nome}")
        print("\nDEPOIS DA BUILD:")
        print(personagem)
        salvar_personagem(personagem, usuario_id)
    else:
        print("Classe inválida!")
        return

def main():
    usuario_id = None
    
    while True:
        if not usuario_id:
            print("\n=== MENU PRINCIPAL ===\n1 - Registrar\n2 - Login\n3 - Sair")
            opcao = input("Selecione uma opção: ").strip()
            
            if opcao == "1":
                registrar_usuario()
            elif opcao == "2":
                usuario_id = login_usuario()
            elif opcao == "3":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")
        else:
            print("\n=== MENU DO USUÁRIO ===\n1 - Criar Personagem\n2 - Listar Personagens\n3 - Excluir Personagem\n4 - Logout")
            opcao = input("Selecione uma opção: ").strip()
            
            if opcao == "1":
                criar_personagem(usuario_id)
            elif opcao == "2":
                listar_personagens(usuario_id)
            elif opcao == "3":
                excluir_personagem(usuario_id)
            elif opcao == "4":
                usuario_id = None
                print("Logout realizado!")
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    main()
