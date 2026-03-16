#!/usr/bin/env python3
"""
Script para generar PDF del documento de investigación
"""
import markdown
from weasyprint import HTML, CSS
from pathlib import Path

# Leer el archivo markdown
md_path = Path(__file__).parent / "research-insurtech-ai-agents.md"
with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convertir markdown a HTML
md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])
html_content = md.convert(md_content)

# CSS para el PDF
css = CSS(string='''
@page {
    size: A4;
    margin: 2cm;
    @top-center {
        content: "Investigación: Agentes de IA para Seguros";
        font-size: 10px;
        color: #666;
    }
    @bottom-center {
        content: counter(page);
        font-size: 10px;
    }
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #333;
}

h1 {
    color: #1a365d;
    font-size: 24pt;
    border-bottom: 3px solid #2b6cb0;
    padding-bottom: 10px;
    margin-top: 30px;
}

h2 {
    color: #2b6cb0;
    font-size: 18pt;
    margin-top: 25px;
    border-bottom: 1px solid #bee3f8;
    padding-bottom: 5px;
}

h3 {
    color: #2c5282;
    font-size: 14pt;
    margin-top: 20px;
}

h4 {
    color: #4a5568;
    font-size: 12pt;
    margin-top: 15px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
    font-size: 10pt;
}

th {
    background-color: #2b6cb0;
    color: white;
    padding: 10px;
    text-align: left;
    font-weight: bold;
}

td {
    border: 1px solid #e2e8f0;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #f7fafc;
}

code {
    background-color: #edf2f7;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: "SF Mono", Monaco, "Courier New", monospace;
    font-size: 9pt;
}

pre {
    background-color: #1a202c;
    color: #e2e8f0;
    padding: 15px;
    border-radius: 5px;
    overflow-x: auto;
    font-size: 9pt;
    line-height: 1.4;
}

pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
}

blockquote {
    border-left: 4px solid #2b6cb0;
    margin: 15px 0;
    padding: 10px 20px;
    background-color: #ebf8ff;
    font-style: italic;
}

ul, ol {
    margin: 10px 0;
    padding-left: 25px;
}

li {
    margin: 5px 0;
}

strong {
    color: #1a365d;
}

hr {
    border: none;
    border-top: 2px solid #e2e8f0;
    margin: 30px 0;
}

/* Primera página - portada */
h1:first-of-type {
    text-align: center;
    font-size: 28pt;
    margin-top: 100px;
    border-bottom: none;
}

/* Links */
a {
    color: #2b6cb0;
    text-decoration: none;
}

/* Tabla de contenidos */
.toc {
    background-color: #f7fafc;
    padding: 20px;
    border-radius: 5px;
    margin: 20px 0;
}
''')

# HTML completo con estilos
full_html = f'''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Investigación: Agentes de IA para la Industria de Seguros</title>
</head>
<body>
{html_content}
</body>
</html>
'''

# Generar PDF
output_path = Path(__file__).parent / "research-insurtech-ai-agents.pdf"
HTML(string=full_html).write_pdf(output_path, stylesheets=[css])

print(f"PDF generado exitosamente: {output_path}")
