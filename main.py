from cli import run_cli
from database import create_tables
import logging
from flask_app import app
from services import work_state

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    create_tables()
    run_cli()
    app.run(host='0.0.0.0', port=5000, debug=True)
    work_state()