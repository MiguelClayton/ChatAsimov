# nome variavel do sistema: OPENAI_API_KEY
# valor da variavel: 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

import tkinter as tk
import openai
import os
import subprocess


def gerar_resposta():
    input_text = text_box.get('1.0', tk.END)

    openai.api_key = os.environ['OPENAI_API_KEY']
    prompt = input_text
    parametros = {'engine': 'text-davinci-003', 'prompt': prompt, 'temperature': 0.3, 'max_tokens': 1000}
    resposta = openai.Completion.create(**parametros)
    response_box.delete(1.0, tk.END)
    response_box.insert(tk.END, resposta.choices[0].text)


verifica = 'OPENAI_API_KEY'
if verifica not in os.environ:
    comando = 'setx OPENAI_API_KEY "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" /m'
    processo = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    saida, erro = processo.communicate()


janela = tk.Tk()
janela.title('Asimov')
janela.geometry('350x370')
janela.configure(background='#808080')

text_box = tk.Text(janela, bg='#C0C0C0', height=5, width=30)
text_box.grid(row=0, column=0, padx=10, pady=10)

botao = tk.Button(janela, text='Enviar', command=gerar_resposta)
botao.grid(row=0, column=1, padx=10, pady=10)

response_box = tk.Text(janela, bg='#C0C0C0', height=15, width=40)
response_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()
