"""Esse arquivo testa o arquivo main.py"""

import importlib  # para importar o módulo main dinamicamente
import io  # para capturar a saída do print
import sys  # para restaurar o stdout padrão e remover o módulo main do cache
import unittest  # para criar o caso de teste
from unittest.mock import patch  # para simular a entrada do usuário


class TestMain(unittest.TestCase):
    """Classe que testa o arquivo main.py"""

    def setUp(self):
        """
        Inicializa o ambiente de teste removendo o módulo principal do cache.
        Isso é necessário para ser capaz de importá-lo novamente em cada teste.
        """
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="1")
    def test_1(self, _mock_input):
        """Testa o main com o input 1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("2", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="5")
    def test_5(self, _mock_input):
        """Testa o main com o input 5"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("2\n3\n5\n7\n11", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="20")
    def test_20(self, _mock_input):
        """Testa o main com o input 20"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n31\n37"
            "\n41\n43\n47\n53\n59\n61\n67\n71",
            captured_output.getvalue().strip(),
        )
