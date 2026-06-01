# Sistema de Diagnostico de Internet

print("Olá, bem vindo ao sistema de diagnóstico de internet\n")

# Variavel para armazenar a resposta do usuario

internet = input("A internet está funcionando? (sim/não): ")

if internet == "sim":
    print("Nenhum problema detectado!\n")
else: 
    modem = input("As luzes do seu modem estão apagadas? (sim/não): ")
    
    if modem == "sim":
        print("Verifique a energia do modem")
    else: 
        print("Reinicie o modem")
