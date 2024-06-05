
from random import randint

# Lista de NPCs
lista_npcs = []

# Dados do jogador
player = {
    "nome": "Bilbu",
    "level": 1,
    "dano": 25,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
}

# Função para criar um NPC
def criar_npc():
    level = randint(0, 20)
    novo_npc = {
        "nome": f"monstro #{level}",
        "level": level,
        "dano": level * 5,
        "hp": 100 * level,
        "hp_max": 100 *level,
        "exp": 7 * level
    }
    return novo_npc

# Função para gerar vários NPCs
def gerar_npcs(n_npcs):
    for _ in range(n_npcs):
        novo_npc = criar_npc()
        lista_npcs.append(novo_npc)

#level up

def level_up():
    if player ['exp'] >= player['exp_max']:
        player ['level'] += 1
        player ['exp_max'] = player ['exp_max'] * 2
        player ['hp_max'] += 20
        player ['dano'] = player['dano'] * player['level'] 




# Função para exibir as informações de um NPC
def exibir_npcs(npc):
    print(
        f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']}"
    )
# Função para exibir as informações do player
def exibir_player():
    print(
        f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}"
    )

#iniciar batalha
def iniciar_batalha(npc):
    while player["hp"] > 0 and npc["hp"] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)
        

        if player["hp"] > 0:
            print(f" o {player['nome']} venceu e ganhou {npc['exp']} de XP")
            player ['exp'] += npc['exp']
            exibir_player()
        else:
            print(f"o {npc['nome']} venceu")
            exibir_npc

        level_up()

# Função para atacar um NPC
def atacar_npc(npc):
    npc['hp'] -= player['dano']

# Função para atacar o jogador
def atacar_player(npc):
    player['hp'] -= npc['dano']


def exibir_info_batalha(npc):
    print(f"player: {player['hp']}/{player['hp_max']}")
    print(f"npc: {npc['nome']}  // Dano: {npc['dano']} : {npc['hp']}/{npc['hp_max']} ")
    print("----------------------------------------------")

# Gerar NPCs
gerar_npcs(5)

# Exibir todos os NPCs gerados

def exibir_npc():
    for npc in lista_npcs:
        exibir_npc(npc)

# Selecionar um NPC para atacar
npc_selecionado = lista_npcs[0]

# Atacar o NPC selecionado
iniciar_batalha(npc_selecionado)