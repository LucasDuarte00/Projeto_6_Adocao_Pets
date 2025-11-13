from flask import Flask, render_template, request
import json
import resend

resend.api_key = "re_hPdPsRSD_Lr4nGto1BJdXBDft4UjmR5iH"

with open('contatos.json', 'r', encoding='utf-8') as arquivo:
    contatos = json.load(arquivo)


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']
        
        contato = {}
        contato['nome'] = nome
        contato['email'] = email
        contato['mensagem'] = mensagem 
        contatos.append(contato)
        
        with open('contatos.json', 'w', encoding='utf-8')as arquivo:
            json.dump(contatos, arquivo, indent=4, ensure_ascii=False)
        
        email_html = f"""
        <h1>Novo contato de {nome}!</h1><br>
        <p>Email: {email}</p><br>
        <p>{mensagem}</p><br>
        """
        r = resend.Emails.send({
            "from":"onboarding@resend.dev",
            "to":"lucasduartedias46@gmail.com" , 
            "subject":"Contato para adoção de pets.", 
            "html": email_html 
            })

    return render_template('index.html')



if __name__ =='__main__':
    app.run(debug=True)