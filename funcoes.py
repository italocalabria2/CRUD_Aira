import re

palavras = {
    "amarelo": ["rua ", "avenida", "bairro", "@", "bomba", "hackear"],
    "vermelho": ["cpf", "senha", "cartao", "cartão"]
}


def validar_cpf(numero):
  # retirando coisas que não são dígitos
  cpf_sem_simbolos = re.sub(r"\D", "", numero)
    
  # checar a qtd de digitos depois de tratar
  if len(cpf_sem_simbolos) != 11:
    return False

  # primeiro passo: calcula o dígito 10 a partir dos 9 primeiros
  lista_digitos = []
  for digito in cpf_sem_simbolos:
    lista_digitos.append(int(digito))
    
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
    if len(numeros) == 11 and validar_cpf(texto):   #eu mexi aqui rosa
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