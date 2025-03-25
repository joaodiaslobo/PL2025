# TPC6: Recursivo descendente para expressões aritméticas

24/03/2025

## 👤 Autor  

- **Nome:** João Lobo  
- **Número de aluno:** A104356

## 🎯 Objetivo

O objetivo deste trabalho é desenvolver um analisador sintático para expressões aritméticas utilizando um analisador léxico baseado na biblioteca [PLY](https://www.dabeaz.com/ply/ply.html). O sistema deve ser capaz de interpretar expressões matemáticas escritas pelo utilizador e calcular o resultado corretamente, respeitando a precedência dos operadores.

## 📝 Explicação da solução

O sistema foi implementado em Python e segue a abordagem de análise sintática recursiva descendente para avaliar expressões aritméticas.

O analisador léxico reconhece os seguintes tokens:

- **NUM**: Representa números inteiros.
- **ADD (+)**: Representa a operação de adição.
- **SUB (-)**: Representa a operação de subtração.
- **MUL (*)**: Representa a operação de multiplicação.
- **DIV (/)**: Representa a operação de divisão.
- **PO (()**: Representa o parêntese a abrir.
- **PC ())**: Representa o parêntese a fechar.

Este utiliza expressões regulares para identificar esses tokens e atribuí-los corretamente.

## 🏃‍♂️ Execução

O programa é executado no terminal e permite ao utilizador inserir expressões matemáticas linha a linha:

```
$ python main.py
Enter expression: 2 * (3 + 4) - 5
Result: 9
```