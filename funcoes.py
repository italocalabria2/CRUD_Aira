import re

palavras = {
    "amarelo": ["rua ", "avenida", "bairro", "@", "bomba", "hackear"],
    "vermelho": ["cpf", "senha", "cartao", "cartão"]
}


def validar_cpf(numero):

    # checar a qtd de digitos
    if len(numero) != 11:
        return False
    # primeiro passo: calcula o dígito 10 a partir dos 9 primeiros
    lista_digitos = []
    for digito in numero:
        lista_digitos.append(int(digito))

    # checa se os dígitos são todos iguais
    if sum(lista_digitos) == (lista_digitos[0]*11):
        return False

    soma_1 = 0
    lista_pesos_1 = list(range(10, 1, -1))

    lista_nova = lista_digitos[0:9]

    # somatório com pesos
    for idx, digito in enumerate(lista_nova):
        soma_1 += digito * lista_pesos_1[idx]

    # cálculo do módulo
    resto_1 = soma_1 % 11

    # calculando o dígito 10
    if resto_1 < 2:
        d_10 = 0
    else:
        d_10 = 11 - resto_1

    # segundo passo: calcula o dígito 11 a partir dos 9 primeiros dígitos + o d_10
    lista_nova.append(d_10)

    lista_pesos_2 = range(11, 1, -1)
    soma_2 = 0

    for idx, digito in enumerate(lista_nova):
        if idx > 10:
            break
        soma_2 += digito * lista_pesos_2[idx]

    resto_2 = soma_2 % 11

    if resto_2 < 2:
        d_11 = 0
    else:
        d_11 = 11 - resto_2

    # validação
    if d_10 == lista_digitos[9] and d_11 == lista_digitos[10]:
        return True
    else:
        return False
# Eu tirei um print que tu tava usando de teste aqui rosa

def descobrir_cor(texto):
    numeros = []
    
    for palavra in texto.split():
        # retirando coisas que não são dígitos
        palavra_sem_simbolos = re.sub(r"\D", "", palavra)
        if len(palavra_sem_simbolos) > 0:
           numeros.append(palavra_sem_simbolos)

    converter_minusculo = texto.lower()

    cor = "verde"

    for palavra in palavras["amarelo"]:
        if palavra in converter_minusculo:
            cor = "amarelo"
    for numero in numeros:
        if len(numero) >= 8:
            cor = "amarelo"

    for palavra in palavras["vermelho"]:
        if palavra in converter_minusculo:
            cor = "vermelho"
    for numero in numeros:
        if validar_cpf(numero):   #eu mexi aqui rosa
            cor = "vermelho"
        if len(numero) == 16:
            cor = "vermelho"

    return cor


def criar(prompts):
    texto = input("Digite seu prompt: ")
    cor = descobrir_cor(texto)
    numeros = []
    numeros_original = []
        
    for palavra in texto.split():
        # retirando coisas que não são dígitos
        palavra_sem_simbolos = re.sub(r"\D", "", palavra)
        if len(palavra_sem_simbolos) > 0:
            numeros.append(palavra_sem_simbolos)
            numeros_original.append(palavra)
    for id, numero in enumerate(numeros):
        if validar_cpf(numero):
            texto = texto.replace(numeros_original[id], "[CPF]")
    prompts.append((texto, cor))
    if cor == "vermelho":
        resposta = "Vermelho = PERIGO! Alta probabilidade de vazamento de dados sensíveis."
    elif cor == "amarelo":
        resposta = "Amarelo = ATENÇÃO! O texto pode conter alguma informação sensível."
    elif cor == "verde":
        resposta = "Verde = TUDO CERTO! Pode mandar o prompt na IA de sua escolha."
    print("Resultado da avaliação: ", resposta)


def listar(prompts):
    if len(prompts) == 0:
        print("Nenhum prompt na memória. Tente criar novos prompts.")
    for i in range(len(prompts)):
        print(i + 1, "-", prompts[i][0], "-", prompts[i][1])


def atualizar(prompts):
    listar(prompts)
    if len(prompts) == 0:
       return
    numeros = []
    numeros_original = []
    try:
        print("Atenção! Adicionar um valor invalido irá retornar ao menu principal sem atualizar nenhum prompt.")
        n = int(input("Qual número do prompt que deseja mudar? "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return
    if n < 1 or n > len(prompts):
        print("Número invalido")
        return
    texto = input("Digite seu novo prompt: ")
    cor = descobrir_cor(texto)
    for palavra in texto.split():
    # retirando coisas que não são dígitos
        palavra_sem_simbolos = re.sub(r"\D", "", palavra)
        if len(palavra_sem_simbolos) > 0:
            numeros.append(palavra_sem_simbolos)
            numeros_original.append(palavra)
    for id, numero in enumerate(numeros):
        if validar_cpf(numero):
            texto = texto.replace(numeros_original[id], "[CPF]")
    prompts[n - 1] = (texto, cor)
    if cor == "vermelho":
        resposta = "Vermelho = PERIGO! Alta probabilidade de vazamento de dados sensíveis."
    elif cor == "amarelo":
        resposta = "Amarelo = ATENÇÃO! O texto pode conter alguma informação sensível."
    elif cor == "verde":
        resposta = "Verde = TUDO CERTO! Pode mandar o prompt na IA de sua escolha."
    print("Atualizado! Resultado: ", resposta)


def deletar(prompts):
    listar(prompts)
    if len(prompts) == 0:
        return
    
    try:
        print("Atenção! Adicionar um valor invalido irá retornar ao menu principal sem apagar nenhum prompt.")
        n = int(input("Qual número do prompt que deseja apagar? "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return
    if n < 1 or n > len(prompts):
        print("Número invalido")
        return
    if len(prompts) == 1:
        prompts.pop(n - 1)
        prompts = []
    else:
        prompts.pop(n - 1)
    print("Apagado!")


def buscar(prompts):
    if len(prompts) == 0:
        print("Nenhum prompt")
        return

    palavra = input("Digite a palavra para buscar: ")
    palavra = palavra.lower()

    achou = False
    for i in range(len(prompts)):
        if palavra in prompts[i][0].lower():
            print(i + 1, "-", prompts[i][0], "-", prompts[i][1])
            achou = True

    if achou == False:
        print("Nada encontrado")

def salvar_backup(prompts):
    nao_aceito = True
    while nao_aceito:   
        print("Atenção! Esta operação irá remover todos os prompts do arquivo e substituí-los pelos prompts da memória.")
        cont = input("Deseja continuar com esta operação? S/N\n")
        if cont == "S":
            nao_aceito = False
        elif cont == "N":
            return
        else:
            print("Valor incorreto. Favor informar 'S' para 'Sim' e 'N' para 'Não'.")
    nome_arquivo = "prompts.txt"
    backup = open(nome_arquivo, "w", encoding="UTF-8")
    for prompt in prompts:
       backup.write(f"{prompt[0]}**{prompt[1]}\n")
    backup.close()
    print("Backup criado com sucesso! Você pode encontrá-lo no arquivo prompts.txt.")

def recuperar_backup(prompts):
    prompts_backup = []
    nao_aceito = True
    while nao_aceito:   
        print("Atenção! Esta operação irá remover todos os prompts da memória e substituí-los pelos prompts do arquivo.")
        cont = input("Deseja continuar com esta operação? S/N\n")
        if cont == "S":
            nao_aceito = False
        elif cont == "N":
            return prompts
        else:
            print("Valor incorreto. Favor informar 'S' para 'Sim' e 'N' para 'Não'.")
    nome_arquivo = "prompts.txt"
    backup = open(nome_arquivo, "r", encoding="UTF-8")
    lista_prompts = backup.readlines()
    backup.close()
    for linha in lista_prompts:
        linha = linha.rstrip('\n')
        if linha == '':
            continue
        termos = linha.split("**")
        prompt = (termos[0], termos[1])
        prompts_backup.append(prompt)
    print("Prompts importados com sucesso!")
    return prompts_backup
