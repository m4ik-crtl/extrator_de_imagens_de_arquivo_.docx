# 🖼️ Extrator de Imagens de Arquivo .docx

Este utilitário permite extrair todas as imagens de documentos Microsoft Word (`.docx`) de forma simples e visual. Ideal para quem deseja recuperar ilustrações de relatórios, apresentações ou manuais técnicos criados no Word.

## 💻 Funcionalidades

- Interface gráfica (GUI) simples e leve  
- Seleção de arquivos via explorador de arquivos  
- Cria automaticamente uma pasta com as imagens extraídas  
- Compatível com documentos `.docx` do Word 2007 em diante  

## 🛠️ Tecnologias Utilizadas

- Python 3.x  
- Tkinter (GUI nativa do Python)  
- zipfile (para leitura do `.docx`)  

## 📦 Como usar

### ▶️ Rodando via Python

1. Clone o repositório ou baixe o script:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```
2. Instale o Python: 
    https://www.python.org/downloads/

3. Execute o script:

```bash
python extrair_imagens_docx_gui.py 
```

### ▶️ Gerando o .exe

1. Instale o PyInstaller:

```bash
pip install pyinstaller
```

2. Gere o executável: 

```bash
pyinstaller --noconsole --onefile extrair_imagens_docx_gui.py
```
3. O `.exe` será salvo na pasta `dist/`.

### 🗂️ Estrutura de Saída

Ao selecionar um arquivo `.docx` as imagens serão extraídas automaticamente para: 

```bash
<mesma_pasta_do_docx>/imagens_extraidas/
