from cli import run_cli
from database import create_tables
import logging
from flask_app import app

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    create_tables()
    run_cli()
    app.run(debug=True)