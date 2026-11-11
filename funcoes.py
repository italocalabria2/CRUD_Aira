
def criar(prompts):
    texto = input("Digite o prompt: ")
    numeros = ""
    for c in texto:
        if c in "0123456789":
            numeros = numeros + c

    converter_minusculo = texto.lower()

    cor = "verde"
    if "rua " in converter_minusculo or "Rua " in converter_minusculo or "avenida" in converter_minusculo or "Avenida" in converter_minusculo or "bairro" in converter_minusculo or "Bairro" in converter_minusculo or "@" in converter_minusculo:
        cor = "amarelo"
    elif "bomba" in converter_minusculo or "Bomba" in converter_minusculo or "hackear" in converter_minusculo or "Hackear" in converter_minusculo:
        cor = "amarelo"
    elif len(numeros) >= 8:
        cor = "amarelo"
    elif "cpf" in converter_minusculo or "CPF" in converter_minusculo or "senha" in converter_minusculo or "Senha" in converter_minusculo or "cartao" in converter_minusculo or "cartão" in converter_minusculo:
        cor = "vermelho"
    elif len(numeros) == 11 and "." in converter_minusculo:
        cor = "vermelho"
    elif len(numeros) == 16:
        cor = "vermelho"

    if len(numeros) == 11:
        converter_minusculo = converter_minusculo.replace(numeros, 'CPF')

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
    numeros = ""
    for c in texto:
        if c in "0123456789":
            numeros = numeros + c
    converter_minusculo = texto.lower()

    cor = "verde"
    if "rua " in converter_minusculo or "Rua " in converter_minusculo or "avenida" in converter_minusculo or "Avenida" in converter_minusculo or "bairro" in converter_minusculo or "Bairro" in converter_minusculo or "@" in converter_minusculo:
        cor = "amarelo"
    if "bomba" in converter_minusculo or "Bomba" in converter_minusculo or "hackear" in converter_minusculo or "Hackear" in converter_minusculo:
        cor = "amarelo"
    if len(numeros) >= 8:
        cor = "amarelo"
    if "cpf" in converter_minusculo or "CPF" in converter_minusculo or "senha" in converter_minusculo or "Senha" in converter_minusculo or "cartao" in converter_minusculo or "cartão" in converter_minusculo:
        cor = "vermelho"
    if len(numeros) == 11 and "." in converter_minusculo:
        cor = "vermelho"
    if len(numeros) == 16:
        cor = "vermelho"

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

