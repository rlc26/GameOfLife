# lint_script.py
import sys
from flake8.main import application

def main():
    # Ajoute les fichiers à vérifier
    sys.argv.extend(["gameoflife/life.py", "gameoflife/life_test.py"])

    # Crée l'application Flake8
    app = application.Application()

    # Initialisation avec argv et configuration nécessaire
    app.initialize(argv=sys.argv)

    # Exécute le linting
    app.run_checks()
