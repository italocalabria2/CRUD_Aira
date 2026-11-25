# Semáforo da AIRA

Projeto AIRA – Grupo 3 (CESAR School)

Aplicação em Python que ajuda a decidir se um prompt é seguro para enviar a uma IA. Cada prompt recebe uma cor, como num semáforo, conforme o risco de conter dados sensíveis.

| Cor | Significado |
|---|---|
| 🟢 Verde | Tudo certo. Pode enviar o prompt. |
| 🟡 Amarelo | Atenção. O texto pode conter informação sensível. |
| 🔴 Vermelho | Perigo. Alta chance de vazamento de dados sensíveis. |

## Como executar

Requer Python 3. Não há dependências externas.

```bash
python app.py   # versão no terminal
python gui.py   # versão com interface gráfica (tkinter)
```

## Operações (CRUD)

Os prompts ficam em uma lista em memória. Cada item é uma tupla `(texto, cor)`.

| Menu | Operação | O que faz |
|---|---|---|
| 1 | **Criar** | Recebe um prompt, mascara CPFs válidos como `[CPF]` e calcula a cor. |
| 2 | **Listar** | Mostra todos os prompts com número e cor. |
| 3 | **Atualizar** | Troca o texto de um prompt pelo número e recalcula a cor, com a mesma máscara de CPF. |
| 4 | **Deletar** | Remove um prompt pelo número. |
| 5 | **Buscar** | Lista os prompts que contêm uma palavra, sem diferenciar maiúsculas de minúsculas. |
| 6 | **Backup** | Grava os prompts em `prompts.txt`, sobrescrevendo o arquivo. |
| 7 | **Recuperar** | Substitui os prompts em memória pelos do arquivo. |
| 0 | **Sair** | Encerra o programa. |

Backup e recuperação pedem confirmação (`S`/`N`). Entradas inválidas voltam ao menu sem encerrar o programa.

## Como a cor é definida

A função `descobrir_cor` começa em verde e sobe o nível conforme o conteúdo:

- **Amarelo:** termos como `rua`, `avenida`, `bairro`, `@`, `bomba`, `hackear`, ou qualquer número com 8 dígitos ou mais.
- **Vermelho:** termos como `cpf`, `senha`, `cartão`, um CPF válido ou um número de 16 dígitos (cartão).

O CPF é validado pelos dígitos verificadores. Sequências de dígitos iguais, como `111.111.111-11`, são rejeitadas.

## Formato do backup

Uma linha por prompt, no formato `texto**cor`. Como o texto é salvo já mascarado, o CPF nunca vai para o arquivo.

## Estrutura

```
app.py       Menu no terminal e laço principal
funcoes.py   CRUD, validação de CPF, cálculo de cor e backup
gui.py       Interface gráfica (tkinter)
prompts.txt  Arquivo de backup
```

## Limitações conhecidas

- A interface gráfica (`gui.py`) ainda não tem backup nem máscara de CPF.
- Um prompt que contenha `**` corrompe a leitura do backup.
- Recuperar sem existir `prompts.txt` gera erro.

## Equipe

Ítalo Calábria, Lucas Gabriel, Rosa Cozzi, Luiz Fernando Cruz da Silva, Raphael Ting e João Guilherme.
