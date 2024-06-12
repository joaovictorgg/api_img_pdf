# Conversor de Imagem para PDF

Este é um aplicativo desktop simples desenvolvido em Python que permite converter imagens (PNG, JPG, JPEG) para um arquivo PDF.

## Funcionalidades

- Selecionar múltiplas imagens de uma vez.
- Visualizar a lista de imagens selecionadas.
- Definir o nome do arquivo PDF de saída.
- Converter as imagens selecionadas em um arquivo PDF.

## Tecnologias Utilizadas

- Python
- Tkinter (para a interface gráfica)
- ReportLab (para gerar PDFs)
- PIL (Python Imaging Library) para manipulação de imagens

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas Python necessárias:
    - Tkinter (incluído na instalação padrão do Python)
    - ReportLab
    - PIL (Pillow)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/conversor-imagem-pdf.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd conversor-imagem-pdf
    ```

3. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

4. Instale as dependências necessárias:
    ```bash
    pip install reportlab pillow
    ```

## Uso

1. Execute o aplicativo:
    ```bash
    python main.py
    ```

2. O aplicativo abrirá uma janela onde você pode:
    - Clicar no botão "Selecionar imagens" para escolher as imagens que deseja converter.
    - Visualizar a lista de imagens selecionadas.
    - Inserir o nome desejado para o arquivo PDF de saída.
    - Clicar no botão "Converter para PDF" para gerar o arquivo PDF.

## Estrutura do Código

- `main.py`: Contém a classe `ImagemParaPdfConversor` que gerencia a interface gráfica e a lógica de conversão das imagens para PDF.

## Capturas de Tela

(Incluir capturas de tela do aplicativo em uso)

## Contato

João Victor Gomes de Souza  
[![LinkedIn](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/joaovictorgomes-desouza/)


[Repositório no GitHub](https://github.com/joaovictorgg/api_img_pdf.git))

