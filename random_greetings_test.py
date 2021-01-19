import unittest
import random_greetings

class RandomGreetings(unittest.TestCase):
    
    # abrir_csv
    def test_abrir_csv_com_sucesso_validando_numero_linhas(self):
        arquivo_csv = random_greetings.abrir_csv("test/lista_correta.csv")
        numero_linhas = sum(1 for linha in arquivo_csv)
        self.assertEqual(numero_linhas, 10345)

    def test_abrir_csv_sem_linhas_deve_retornar_zero_linhas(self):
        arquivo_csv = random_greetings.abrir_csv("test/lista_vazia.csv")
        numero_linhas = sum(1 for linha in arquivo_csv)
        self.assertEqual(numero_linhas, 0)

    # buscar_termos_validos
    def test_buscar_termos_validos_com_sucesso_deve_retornar_numero_correto_de_elementos(self):
        arquivo_csv = random_greetings.abrir_csv("test/lista_correta.csv")
        lista_termos = random_greetings.buscar_termos_validos(arquivo_csv)
        self.assertEqual(len(lista_termos), 9684)

    def test_buscar_termos_validos_com_apenas_2_colunas_arquivo_deve_retornar_lista_vazia(self):
        arquivo_csv = random_greetings.abrir_csv("test/lista_com_2_colunas.csv")
        lista_termos = random_greetings.buscar_termos_validos(arquivo_csv)
        self.assertEqual(len(lista_termos), 0)

    def test_buscar_termos_validos_sem_elementos_validos_deve_retornar_lista_vazia(self):
        arquivo_csv = random_greetings.abrir_csv("test/lista_apenas_familias.csv")
        lista_termos = random_greetings.buscar_termos_validos(arquivo_csv)
        self.assertEqual(len(lista_termos), 0)

    # definir_saudacao
    def test_definir_saudacao_madrugada_com_sucesso(self):
        self.assertEqual(random_greetings.definir_saudacao(3), "Boa madrugada")

    def test_definir_saudacao_dia_com_sucesso(self):
        self.assertEqual(random_greetings.definir_saudacao(7), "Bom dia")

    def test_definir_saudacao_tarde_com_sucesso(self):
        self.assertEqual(random_greetings.definir_saudacao(13), "Boa tarde")
        
    def test_definir_saudacao_noite_com_sucesso(self):
        self.assertEqual(random_greetings.definir_saudacao(19), "Boa noite")

    # montar_response
    def test_montar_response_com_sucesso(self):
        cumprimento = "Boa noite, meu Esmaltador de metais não-preciosos"
        self.assertEqual(random_greetings.montar_response(cumprimento).decode(), '{"cumprimento": "Boa noite, meu Esmaltador de metais não-preciosos"}')

if __name__ == '__main__':
    unittest.main()
