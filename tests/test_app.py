"""Pruebas de arranque y ejecución básica, no auditoría exhaustiva."""
import os
import shutil
import tempfile
import unittest
from pathlib import Path
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
ENTRY = "ViajeUber.py"

class TestAplicacion(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.previous = Path.cwd()
        for file in ROOT.iterdir():
            if file.suffix in ('.py', '.json'):
                shutil.copy2(file, self.temp.name)
        os.chdir(self.temp.name)

    def tearDown(self):
        os.chdir(self.previous)
        self.temp.cleanup()

    def test_inicio(self):
        app = AppTest.from_file(str(Path(self.temp.name) / ENTRY), default_timeout=30).run()
        self.assertFalse(app.exception, str(app.exception))

    def test_calculo_o_menu(self):
        app = AppTest.from_file(str(Path(self.temp.name) / ENTRY), default_timeout=30).run()
        self.assertFalse(app.exception, str(app.exception))
        if ENTRY.startswith('ViajeUber'):
            app.text_input[0].set_value('Origen de ejemplo')
            app.text_input[1].set_value('Destino de ejemplo')
        if ENTRY.startswith('SimuladorBanco'):
            app.radio[0].set_value('Crear cuenta').run()
            self.assertGreater(len(app.text_input), 0)
        else:
            botones = [b for b in app.button if 'Calcular' in b.label]
            self.assertTrue(botones)
            botones[0].click().run()
            self.assertGreater(len(app.metric), 0)
        self.assertFalse(app.exception, str(app.exception))
