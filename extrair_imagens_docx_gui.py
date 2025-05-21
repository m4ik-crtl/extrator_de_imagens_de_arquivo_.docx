
import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os

def extrair_imagens_docx(docx_path):
    pasta_saida = os.path.join(os.path.dirname(docx_path), "imagens_extraidas")
    os.makedirs(pasta_saida, exist_ok=True)
    imagens = []

    with zipfile.ZipFile(docx_path, 'r') as docx_zip:
        for item in docx_zip.namelist():
            if item.startswith("word/media/"):
                nome_arquivo = os.path.basename(item)
                caminho_destino = os.path.join(pasta_saida, nome_arquivo)
                with docx_zip.open(item) as fonte, open(caminho_destino, "wb") as destino:
                    destino.write(fonte.read())
                imagens.append(nome_arquivo)

    return pasta_saida, imagens

def selecionar_arquivo():
    caminho = filedialog.askopenfilename(title="Selecione o arquivo .docx", filetypes=[("Documentos Word", "*.docx")])
    if caminho:
        pasta_saida, imagens = extrair_imagens_docx(caminho)
        if imagens:
            messagebox.showinfo("Sucesso", f"{len(imagens)} imagem(ns) extraída(s) para: {pasta_saida}")
        else:
            messagebox.showinfo("Aviso", "Nenhuma imagem encontrada no arquivo.")


janela = tk.Tk()
janela.title("Extrator de Imagens DOCX")
janela.geometry("400x200")
janela.resizable(False, False)

rotulo = tk.Label(janela, text="Clique no botão abaixo para escolher o arquivo .docx", pady=20)
rotulo.pack()

botao = tk.Button(janela, text="Selecionar arquivo .docx", command=selecionar_arquivo, height=2, width=30, bg="#005860", fg="white")
botao.pack()

janela.mainloop()
