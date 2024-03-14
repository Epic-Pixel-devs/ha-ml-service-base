from unittest import TestCase

import requests


class Test_banco_de_dados(TestCase):
    link1 = "http://127.0.0.1:5000"
    link2 = "http://192.168.1.2:5000"
    def criando_app(self):
        try:
            requests.get(self.link1)
            return "acesso aceito"
        except requests.exceptions.ConnectionError:
            return "erro"

    def enviado(self):
        self.assertTrue(self.create_app())


