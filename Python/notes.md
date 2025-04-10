# Introdução e primeiros comandos

- Apresentação da linguagem Python.
- Uso do `print()` para exibir mensagens.

```python
print("Olá, mundo!")
```

# Variáveis e Tipos Primitivos
- Tipos primitivos: `int`, `float`, `bool`, `str`.
- Leitura com `input()` sempre retorna string.
- Conversão de tipos com `int()`, `float()`, `bool()` e `str()`.
- `type()` mostra o tipo de uma variável.

```python
n = input('Digite algo: ')
print(type(n))
```

# Operadores Aritméticos
- Operadores: `+`, `-`, `*`, `/`, `**` (potência), `//` (divisão inteira), `%` (resto)
- Ordem de precedência: `()`, `**`, `* / // %`, `+ -`

```python
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
print(f'A soma é {s}')
```

# Utilizando Módulos
- Módulo `math`: `ceil`, `floor`, `trunc`, `pow`, `sqrt`, `factorial`
- Importação total ou parcial de bibliotecas

```python
from math import sqrt, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(ceil(raiz))
```

# Manipulando texto (Strings)
- Fatiamento: `frase[0:5]`
- Análise: `len()`, `count()`, `find()`
- Transformações: `replace()`, `upper()`, `lower()`, `capitalize()`, `title()`, `strip()`
- Divisão: `split()`, `join()`

```python
frase = 'Curso em Vídeo Python'
print(frase.upper())
```

# Mais sobre Strings
- Uso de operadores `in` e funções de busca.
- Identificação de palavras, posições e uso de `strip()` para limpeza de espaços.

```python
nome = input("Digite seu nome completo: ")
print('Seu nome tem Silva?', 'SILVA' in nome.upper())
```

# Manipulando Números
- Leitura de números com `input()` e conversão para `int` ou `float`.
- Cálculos matemáticos com operadores e funções

```python
n = int(input("Digite um número: "))
print(f"Dobro: {n*2}, Triplo: {n*3}, Raiz: {n**0.5:.2f}")
```

# Condições Simples e Compostas
- `if`, `else`, `elif`
- Operadores relacionais e lógicos: `==`, `!=`, `<`, `>`, `and`, `or`, `not`

```python
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2
if m >= 6:
    print('Aprovado')
else:
    print('Reprovado')
```

# Cores no Terminal
- Sequência ANSI: `\033[estilo;text;backgroundm`
- Estilos: `0`, `1`, `4`, `7` (normal, negrito, sublinhado, negativo)
- Texto: `30 a 37`, Fundo: `40 a 47`

```python
print('\033[1;33;44mTexto colorido\033[m')
```

# Condições Aninhadas
- `if` dentro de `if`, estrutura mais detalhada de decisão

```python
nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome in ['Maria', 'Pedro', 'Paulo']:
    print('Seu nome é bem popular.')
else:
    print('Seu nome é bem normal.')
```

# Estrutura de Repetição FOR
- `for` com `range(início, fim, passo)`
- Pode iterar listas, strings, e mais

```python
for i in range(1, 10, 2):
    print(i)
```

# Estrutura de Repetição WHILE
- `while` roda enquanto a condição for verdadeira
- Usado para laços indefinidos ou com sentinela

```python
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'Soma vale {s}')
```




