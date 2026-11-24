import funcoes as f

prompts = []

print("Bem-vindo ao Semáforo da AIRA.")
print("Aqui você pode testar seus prompts e o semáforo lhe ajuda a definir seu próximo passo.")
while True:
    print()
    print("MENU PRINCIPAL")
    print("---------------------------------")
    print("1 - Testar um novo prompt.")
    print("2 - Listar seus prompts.")
    print("3 - Atualizar um prompt.")
    print("4 - Deletar um prompt.")
    print("5 - Buscar prompts por palavra.")
    print("6 - Fazer backup.")
    print("7 - Recuperar via backup.")
    print("0 - Encerrar o programa.")
    print("---------------------------------")
    try:
        op = int(input("Qual a opção desejada? "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue

    if op == 1:
        f.criar(prompts)
    elif op == 2:
        f.listar(prompts)
    elif op == 3:
        f.atualizar(prompts)
    elif op == 4:
        f.deletar(prompts)
    elif op == 5:
        f.buscar(prompts)
    elif op == 6:
        f.salvar_backup(prompts)
    elif op == 7:
        prompts = f.recuperar_backup()
    elif op ==  0:
        print("------------------------")
        print("Programa encerrado.")
        break
    else:
        print("Opcao invalida")