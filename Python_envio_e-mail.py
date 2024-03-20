import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import traceback

def enviar_email(destinatario, assunto, mensagem):
    # Config. do servidor SMTP
    server_smtp = 'smtp.example.com'
    porta_smtp = 587
    usuario = 'email@email.com'
    senha = 'senha'

    # Criando o objeto de e-mail
    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adicionando o corpo da mensagem
    corpo = mensagem
    msg.attach(MIMEText(corpo, 'plain'))

    # Conectando-se ao servidor SMTP e enviando o e-mail
    try:
        with smtplib.SMTP(server_smtp, porta_smtp) as servidor:
            servidor.starttls()
            servidor.login(usuario, senha)
            servidor.send_message(msg)
            print("E-mail enviado!")
    except Exception as e:
        print("Erro ao enviar e-mail:", e)

def meu_codigo():
    # definição de números
    num1 = 600
    num2 = 66
    # soma
    soma = num1 + num2 
    # impressão do resultado
    print(soma)
    try:
        resultado = 10 / 0
    except Exception as e:
        # Se ocorrer um erro, envie um e-mail de alerta!
        erro = traceback.format_exc()  # Obtém o rastreamento do erro
        enviar_email('destinatario@email.com', 'Erro no script', erro)
    else:
        # Se não houver erro, envie um e-mail de sucesso!
        enviar_email('destinatario@email.com', 'Script executado com sucesso', 'O script foi executado com sucesso!')

if __name__ == "__main__":
    meu_codigo()
