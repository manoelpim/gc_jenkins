import unittest
from temperatura import fahrenheit_para_celsius, celsius_para_fahrenheit

class TestConversaoTemperatura(unittest.TestCase):

    # Teste para verificar a conversão de Fahrenheit para Celsius
    def test_fahrenheit_para_celsius(self):
        # Testando a conversão de 32°F para 0°C
        self.assertEqual(fahrenheit_para_celsius(32), 100.0)
        # Testando a conversão de 212°F para 100°C
        self.assertEqual(fahrenheit_para_celsius(212), 100.0)

    # Teste para verificar a conversão de Celsius para Fahrenheit
    def test_celsius_para_fahrenheit(self):
        # Testando a conversão de 0°C para 32°F
        self.assertEqual(celsius_para_fahrenheit(0), 32.0)
        # Testando a conversão de 100°C para 212°F
        self.assertEqual(celsius_para_fahrenheit(100), 212.0)

if __name__ == '__main__':
    unittest.main()