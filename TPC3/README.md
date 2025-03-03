# TPC3: Conversor de _Markdown_ para HTML  

23/02/2025

## 👤 Autor  

- **Nome:** João Lobo  
- **Número de aluno:** A104356

## 🎯 Objetivo

Pretende-se criar em Python um pequeno conversor de _Markdown_ para HTML para os seguintes elementos:

- Cabeçalhos

```md
# Título
## Subtítulo
### Subsubtítulo
```

- **Bold**

```md
**Negrito**
```

- *Itálico*

```md
*Itálico*
```

- Lista númerada

```md
1. Primeiro item
2. Segundo item
3. Terceiro item
```

- Link

```md
[Isto é um link](https://di.uminho.pt)
```

- Imagem

```md
![Texto alternativo](https://di.uminho.pt/img/logotipo_eeum.gif)
```

## 📝 Explicação da solução

A solução foi desenvolvida em Python e faz uso do módulo `re` para realizar substituições baseadas em expressões regulares (Regex).

Por exemplo, para cabeçalhos, usamos a expressão, para capturar o texto:

```re
# (.*)
```

E a seguinte expressão para adicionar as tags HTML necessárias:

```re
<h1>\1</h1>
```

## 🏃‍♂️ Execução

O programa é executado pelo terminal, passando o ficheiro _Markdown_ a converter para HTML como argumento.  

```
$ python main.py <markdown_file>
```
