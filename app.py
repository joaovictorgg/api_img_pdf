
# Importar bibliotecas
import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from PIL import Image
import os

# Criar a class
class ImagemParaPdfConversor:
# Criar as defs (TUDO)  
     
    # Iniciar o root
    def __init__(self, root):
        self.root = root
        # Criar caminho onde as imagens serão armazenadas
        self.caminhos_imagem = []

        # Criar lugar onde ficará armazenado os nomes de PDF que será criado
        self.saida_pdf_nome = tk.StringVar()

        #Criar a listbox para armazenar as imagens que serão convertidas
        self.img_selecionadas_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        
        # Iniciar a UI
        self.iniciar_ui()
    
    # Criar botões e componentes da UI
    def iniciar_ui(self):
        # Titulo
        titulo_label = tk.Label(self.root, text="Conversor de Imagem - PDF", font=("Helvetica",
        16, "bold"))
        titulo_label.pack(pady=10)

        # Botão de selecionar imagens
        botao_selecionar_imagens = tk.Button(self.root, text="Selecionar imagens", command=self.selecionar_imagens)
        botao_selecionar_imagens.pack(pady=(0, 10))

        # Lista das imagens armazenadas
        self.img_selecionadas_listbox.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

        # Texto para indicar onde colocar o nome desejado do arquivo
        label = tk.Label(self.root, text="Coloque o nome do arquivo em PDF")
        label.pack()

        # Local onde sera inserido nome do PDF
        nome_entry_pdf = tk.Entry(self.root, textvariable=self.saida_pdf_nome, width = 40, justify='center')
        nome_entry_pdf.pack()

        # Botão de converter
        botao_converter = tk.Button(self.root, text="Converter para PDF", command=self.converter_img_para_pdf)
        botao_converter.pack(pady=(0, 10))

    # Iniciar função dos comandos - 1°Botão
    def selecionar_imagens(self):

        #Iniciar o funcionamento do Click de selecionar imagens
        self.caminhos_imagem = filedialog.askopenfilenames(title="Selecionar imagens", 
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        # Iniciar a próxima função de de atualizar as imagens
        self.atualizar_imgs_selecionadas_listbox()

    # Iniciar função dos comandos
    def atualizar_imgs_selecionadas_listbox(self):

        # Checar se tem um nome, e caso tecnha deletar esse nome
        self.img_selecionadas_listbox.delete(0, tk.END)

        # SPLITAR a imagem para que seja inserido somente um novo nome na imagem
        for caminho_imagem in self.caminhos_imagem:
            _, caminho_imagem = os.path.split(caminho_imagem)
            self.img_selecionadas_listbox.insert(tk.END, caminho_imagem)

    # Iniciar funcionamento de criar o PDF
    def converter_img_para_pdf(self):
        if not self.caminhos_imagem:
            return
        
        # Se funcionar, atualziar para o nome escolhido pelo User
        caminho_saida_pdf = self.saida_pdf_nome.get() + ".pdf" if self.saida_pdf_nome.get() else "saida.pdf"
        
        # Criar o pdf usando Canvas
        pdf = canvas.Canvas(caminho_saida_pdf, pagesize=(612, 792))

        # Inserir imagem/ns no PDF
        for caminho_imagem in self.caminhos_imagem:
            img = Image.open(caminho_imagem) 
            tamanho_widht = 540
            tamanho_height = 720
            fator_escala = min(tamanho_widht /img.width, tamanho_height /img.height)
            novo_widht = img.width * fator_escala
            novo_height = img.height * fator_escala
            x_centro = (612 - novo_widht) /2
            y_centro = (792 - novo_height) /2

            # Definir cor da página do PDF
            pdf.setFillColorRGB(255, 255, 255)
            pdf.rect(0, 0, 612, 792, fill=True)
            # Botar imagem no centro
            pdf.drawInlineImage(img, x_centro, y_centro, width=novo_widht, height=novo_height)
            pdf.showPage()
        
        # Salvar PDF
        pdf.save()

# Iniciar o TK e dar call no mainloop
def main():
    root = tk.Tk()
    root.title("Imagem para PDF")
    conversor = ImagemParaPdfConversor(root)
    root.geometry("400x600")
    root.mainloop()

#Iniciar o mainloop
if __name__ == "__main__":
    main()