# TPC4: Analisador Léxico de SPARQL

10/03/2025

## 👤 Autor  

- **Nome:** João Lobo  
- **Número de aluno:** A104356  

## 🎯 Objetivo

Pretende-se criar um analisador léxico para a linguagem SPARQL, capaz de reconhecer os principais tokens desta linguagem de consulta a bases de dados RDF.

## 📝 Explicação da solução

O analisador léxico foi desenvolvido em Python utilizando a biblioteca [PLY](https://www.dabeaz.com/ply/ply.html).

Foi definida uma lista de tokens e expressões regulares para reconhecer comentários, palavras-chave, variáveis, prefixos, strings e números.

A ordem das regras no analisador léxico é fundamental para evitar conflitos. Palavras-chave devem ser processadas antes de identificadores genéricos, regras específicas antes de regras abrangentes e a regra de erro deve vir por último para capturar caracteres inválidos.

## 🏃‍♂️ Execução

O programa é executado pelo terminal, passando um ficheiro contendo uma query SPARQL como argumento.

```
$ python main.py <sparql_query_file>
```