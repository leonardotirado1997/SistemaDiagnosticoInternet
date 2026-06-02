# Dicionario - Base de Conhecimento

regras = {
    ("febre", "tosse"): "Gripe",
    ("dor_garganta", "febre"): "Infecção na garganta",
    ("vomito", "dor_estomago"): "Intoxicação Alimentar (virose, caganeira)"
}

#####################################
# INTRODUÇÃO DO SISTEMA
#####################################
print("Bem vindos ao sistema especialista em diagnósticos médicos")

#####################################
# Inicio do programa
#####################################

# cria um array de sintomas para ser preenchido em tempo de execução 
sintomas_agrupados = []

# Pergunta os sintomas até a pessoa digitar FIM
while True:
    sintoma = input('Informe um sintoma ou fim \n Sintomas Disponiveis: \n("febre", "tosse", "dor_garganta", "febre", "vomito", "dor_estomago"): ')

    # Se o usuario digitar fim, iremos sair do sistema
    if sintoma == "fim":
        print("Obrigado, volte sempre")
        break

    sintomas_agrupados.append(sintoma)

print ("\n Analisando...")

encontrou = False

for regra, diagnostico in regras.items():
    if all(s in sintomas_agrupados for s in regra):
        print(f"Diagnóstico Sugerido: {diagnostico}")
        encontrou = True

if not encontrou:
    print("Deve ser virose")        



