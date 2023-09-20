# nome variavel do sistema: OPENAI_API_KEY
# valor da variavel: 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

import tkinter as tk
import openai
import os
import subprocess


def enviar_mensagem():
    input_text = text_box.get('1.0', tk.END)
    if input_text:
        response_box.config(state="normal")
        response_box.insert("end", f"Você: {input_text}\n")
        response_box.config(state="disabled")

        text_box.delete("1.0", "end")
    openai.api_key = os.environ['OPENAI_API_KEY']
    prompt = input_text
    parametros = {'engine': 'text-davinci-003', 'prompt': prompt, 'temperature': 0.3, 'max_tokens': 1000}
    resposta = openai.Completion.create(**parametros)
    response_box.delete(1.0, tk.END)
    response_box.insert(tk.END, resposta.choices[0].text)



'''def limpar_conversa():
    response_box.config(state="normal")
    response_box.delete("1.0", "end")
    response_box.config(state="disabled")'''


'''def gerar_resposta():
    input_text = text_box.get('1.0', tk.END)

    openai.api_key = os.environ['OPENAI_API_KEY']
    prompt = input_text
    parametros = {'engine': 'text-davinci-003', 'prompt': prompt, 'temperature': 0.3, 'max_tokens': 1000}
    resposta = openai.Completion.create(**parametros)
    response_box.delete(1.0, tk.END)
    response_box.insert(tk.END, resposta.choices[0].text)'''


verifica = 'OPENAI_API_KEY'

if verifica not in os.environ:
    comando = 'setx OPENAI_API_KEY "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" /m'
    processo = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    saida, erro = processo.communicate()


janela = tk.Tk()
janela.title('Asimov')
#janela.geometry('400x500')
janela.attributes('-fullscreen')
janela.configure(background='#ECE5DD')


'''botao = tk.Button(janela, text='Enviar', command=gerar_resposta)
botao.grid(row=0, column=1, padx=10, pady=10)

response_box = tk.Text(janela, bg='#C0C0C0', height=15, width=40)
response_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

text_box = tk.Text(janela, bg='#C0C0C0', height=5, width=30)
text_box.grid(row=0, column=0, padx=10, pady=10)

botao_limpar = tk.Button(janela, text='Limpar Conversa', command=limpar_conversa)
botao_limpar.pack(side='bottom', pady=10)'''

response_box = tk.Text(janela, bg='white', height=15)
response_box.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
response_box.config(state="disabled")

text_box = tk.Text(janela, bg='white', height=3)
text_box.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

botao_enviar = tk.Button(janela, text='Enviar', command=enviar_mensagem, width=20)
botao_enviar.grid(row=1, column=1, padx=10, pady=10, sticky='e')

janela.grid_rowconfigure(0, weight=1)  # A primeira linha (response_box) estica verticalmente
janela.grid_columnconfigure(0, weight=1)  # A primeira coluna (response_box) estica horizontalmente

janela.mainloop()
