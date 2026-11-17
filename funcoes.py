palavras = {
    "amarelo": ["rua ", "avenida", "bairro", "@", "bomba", "hackear"],
    "vermelho": ["cpf", "senha", "cartao", "cartão"]
}


def descobrir_cor(texto):
    numeros = ""
    for c in texto:
        if c in "0123456789":
            numeros = numeros + c

    converter_minusculo = texto.lower()

    cor = "verde"

    for palavra in palavras["amarelo"]:
        if palavra in converter_minusculo:
            cor = "amarelo"
    if len(numeros) >= 8:
        cor = "amarelo"

    for palavra in palavras["vermelho"]:
        if palavra in converter_minusculo:
            cor = "vermelho"
    if len(numeros) == 11 and "." in converter_minusculo:
        cor = "vermelho"
    if len(numeros) == 16:
        cor = "vermelho"

    return cor


def criar(prompts):
    texto = input("Digite o prompt: ")
    cor = descobrir_cor(texto)
    numeros = ""
    for c in texto:
        if c in "0123456789":
            numeros = numeros + c
    if len(numeros) == 11:
        texto = texto.replace(numeros, "CPF")
    prompts.append([texto, cor])
    print("Resultado:", cor)


def listar(prompts):
    if len(prompts) == 0:
        print("Nenhum prompt")
    for i in range(len(prompts)):
        print(i + 1, "-", prompts[i][0], "-", prompts[i][1])


def atualizar(prompts):
    listar(prompts)
    n = int(input("Qual numero quer mudar? "))
    if n < 1 or n > len(prompts):
        print("Numero invalido")
        return
    texto = input("Digite o novo prompt: ")
    cor = descobrir_cor(texto)
    prompts[n - 1] = [texto, cor]
    print("Atualizado! Resultado:", cor)


def deletar(prompts):
    listar(prompts)
    n = int(input("Qual numero quer apagar? "))
    if n < 1 or n > len(prompts):
        print("Numero invalido")
        return
    prompts.pop(n - 1)
    print("Apagado!")