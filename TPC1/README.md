# TPC1: Somador ON/OFF

09/02/2025

## 👤 Autor  

- **Nome:** João Lobo  
- **Número de aluno:** A104356  

## 🎯 Objetivo

1. Pretende-se um programa que **some** todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a `string` `"off"` em qualquer combinação de maiúsculas e minúsculas, esse comportamento é **desligado**.
2. Sempre que encontrar a `string` `"on"` em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente **ligado**.
4. Sempre que encontrar o `char` `'='`, o **resultado** da soma é colocado na **saída**.

## 📝 Explicação da solução

O programa `on_off_sum` lê um ficheiro de texto e percorre o seu conteúdo carácter por carácter. A sua lógica baseia-se num estado de ativação booleano (on/off) que controla se os dígitos encontrados devem ser somados ou ignorados.

## 🏃‍♂️ Execução

O programa é executado pelo terminal, passando o ficheiro de *input* como argumento. 

```
$ python main.py <input_file>
```