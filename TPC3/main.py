import sys
import re

def markdown_to_html(markdown_to_html):
    # Cabeçalhos
    markdown_to_html = re.sub(r'### (.*)', r'<h3>\1</h3>', markdown_to_html)
    markdown_to_html = re.sub(r'## (.*)', r'<h2>\1</h2>', markdown_to_html)
    markdown_to_html = re.sub(r'# (.*)', r'<h1>\1</h1>', markdown_to_html)
    
    # Texto a Negrito
    markdown_to_html = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown_to_html)
    
    # Texto em Itálico
    markdown_to_html = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown_to_html)
    
    # Listas Numeradas
    markdown_to_html = re.sub(r'\n\d+\. (.*)', r'\n<li>\1</li>', markdown_to_html)
    markdown_to_html = re.sub(r'(<li>.*</li>)', r'<ol>\n\1\n</ol>', markdown_to_html, flags=re.DOTALL)

    # Imagens
    markdown_to_html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown_to_html)
    
    # Links
    markdown_to_html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown_to_html)
    
    return f"""<!DOCTYPE html>
<html lang='pt'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Conversão Markdown para HTML</title>
</head>
<body>
{markdown_to_html}
</body>
</html>
    """

def main():
    if len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        file = "example.md"

    with open(file, "r", encoding="utf-8") as f:
        markdown = f.read()
    
    html = markdown_to_html(markdown)

    with open(file, "r", encoding="utf-8") as f:
        markdown = f.read()

    html = markdown_to_html(markdown)
    output_file = file.replace(".md", ".html")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    main()