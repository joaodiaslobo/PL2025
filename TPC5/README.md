# TPC5: Máquina de *Vending*

17/03/2025

## 👤 Author  

- **Nome:** João Lobo  
- **Número de aluno:** A104356

## 🎯 Objetivo

O objetivo deste projeto é criar um analisador léxico e processador para um sistema de máquina de vendas. O sistema pode listar os produtos disponíveis, aceitar moedas e notas como pagamento, processar a seleção de produtos e devolver troco quando necessário.

## 📝 Explicação da solução

O sistema de máquina de vendas foi implementado em Python utilizando a biblioteca [PLY](https://www.dabeaz.com/ply/ply.html) para análise léxica.

### Design do Analisador Léxico

Foi definida uma série de tokens para reconhecer os principais comandos utilizados na máquina de vendas:

- **LISTAR**: Mostra os produtos disponíveis.
- **SAIR**: Encerra a sessão, devolvendo troco se necessário.
- **SELECIONAR**: Escolhe um produto com base no seu código.
- **MOEDA**: Aceita diferentes valores de moedas.
- **NOTA**: Aceita denominações válidas de notas.

## 🏃‍♂️ Execução

O programa é executado no terminal, opcionalmente especificando um ficheiro de _stock_ como argumento. Se nenhum ficheiro for fornecido, o programa utiliza o `stock.json` como padrão.

```
$ python main.py <ficheiro>
```
