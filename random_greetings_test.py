import unittest
import random_greetings

class RandomGreetings(unittest.TestCase):
    
    # abrir_csv
    
    # buscar_termos_validos

    # definir_saudacao
    def test_definir_saudacao_madrugada_com_sucesso(self):
        self.assertEquals(random_greetings.definir_saudacao(3), "Boa madrugada")

    def test_definir_saudacao_dia_com_sucesso(self):
        self.assertEquals(random_greetings.definir_saudacao(7), "Bom dia")

    def test_definir_saudacao_tarde_com_sucesso(self):
        self.assertEquals(random_greetings.definir_saudacao(13), "Boa tarde")
        
    def test_definir_saudacao_noite_com_sucesso(self):
        self.assertEquals(random_greetings.definir_saudacao(19), "Boa noite")

    # montar_response

if __name__ == '__main__':
    unittest.main()

