# TPC2: Análise de um *dataset* de obras musicais

16/02/2025

## 👤 Autor  

- **Nome:** João Lobo  
- **Número de aluno:** A104356  

## 🎯 Objetivo

Pretende-se um programa que leia um *dataset* de obras músicais e cálcule os seguintes resultados:
1. Lista **ordenada alfabeticamente** dos **compositores** musicais;
2. Distribuição das **obras por período**: quantas obras catalogadas em cada período;
3. Dicionário em que a cada período está a associada uma **lista alfabética** dos títulos das obras desse período.

## 📝 Explicação da solução

Foi necessário desenvolver um *parser* de ficheiros CSV para estruturar corretamente a informação das obras musicais a serem analisadas. Esse *parser* percorre todos os caracteres do ficheiro e, conforme o seu tipo, cria novas entradas ou preenche os campos das existentes. Foi dada atenção especial ao conteúdo delimitado por aspas, pois este pode conter caracteres como `\n` e `;`, o que poderia comprometer a correta interpretação dos dados.

O cálculo dos resultados foi bastante simples, tendo recorrido as funcões primitivas do *python*, como o *sort* e estruturas como dicionários e listas.

## 🏃‍♂️ Execução

O programa é executado pelo terminal, passando o ficheiro com um *dataset* como argumento. 

```
$ python main.py <dataset_file>
```