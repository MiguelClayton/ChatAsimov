# nome variavel do sistema: OPENAI_API_KEY
# valor da variavel: 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

import tkinter as tk
import openai
import os
import subprocess


def enviar_mensagem():
    mensagem = text_box.get("1.0", "end-1c")  # Obter texto da caixa de texto
    if mensagem:
        # Adicionar a mensagem à caixa de texto de respostas
        response_box.config(state="normal")
        response_box.insert("end", f"Você: {mensagem}\n")
        response_box.config(state="disabled")

        # Limpar a caixa de entrada
        text_box.delete("1.0", "end")

        input_text = text_box.get('1.0', tk.END)
        openai.api_key = os.environ['OPENAI_API_KEY']
        prompt = input_text
        parametros = {'engine': 'text-davinci-003', 'prompt': prompt, 'temperature': 0.3, 'max_tokens': 1000}
        resposta = openai.Completion.create(**parametros)
        response_box.delete(1.0, tk.END)
        response_box.insert(tk.END, resposta.choices[0].text)


def limpar_conversa():
    # Limpar a caixa de texto de respostas
    response_box.config(state="normal")
    response_box.delete("1.0", "end")
    response_box.config(state="disabled")


'''def gerar_resposta():
    input_text = text_box.get('1.0', tk.END)

    openai.api_key = os.environ['OPENAI_API_KEY']
    prompt = input_text
    parametros = {'engine': 'text-davinci-003', 'prompt': prompt, 'temperature': 0.3, 'max_tokens': 1000}
    resposta = openai.Completion.create(**parametros)
    response_box.delete(1.0, tk.END)
    response_box.insert(tk.END, resposta.choices[0].text)
'''

verifica = 'OPENAI_API_KEY'

if verifica not in os.environ:
    comando = 'setx OPENAI_API_KEY "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" /m'
    processo = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    saida, erro = processo.communicate()


janela = tk.Tk()
janela.title('Asimov')
janela.geometry('400x500')
janela.configure(background='#ECE5DD')


'''botao = tk.Button(janela, text='Enviar', command=gerar_resposta)
botao.grid(row=0, column=1, padx=10, pady=10)

response_box = tk.Text(janela, bg='#C0C0C0', height=15, width=40)
response_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

text_box = tk.Text(janela, bg='#C0C0C0', height=5, width=30)
text_box.grid(row=0, column=0, padx=10, pady=10)'''


# Botão para enviar mensagem
botao_enviar = tk.Button(janela, text='Enviar', command=enviar_mensagem)
botao_enviar.pack(side='bottom', pady=10)

# Botão para limpar a conversa
botao_limpar = tk.Button(janela, text='Limpar Conversa', command=limpar_conversa)
botao_limpar.pack(side='bottom', pady=10)

# Caixa de texto para entrada de texto
text_box = tk.Text(janela, bg='white', height=3)
text_box.pack(side='bottom', fill='both', padx=10, pady=10)

# Caixa de texto para exibição de mensagens
response_box = tk.Text(janela, bg='white', height=15)
response_box.pack(side='top', fill='both', expand=True, padx=10, pady=10)
response_box.config(state="disabled")  # Impede a edição da caixa de texto de respostas

janela.mainloop()
