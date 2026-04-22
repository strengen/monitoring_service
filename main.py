from services import app, work_state, run_cli, create_tables
import logging
import threading
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    if len(sys.argv) < 2:
        logging.error('Please specify the mode either \"runserver\" or \"cli\"')
        sys.exit(1)
    create_tables()
    if sys.argv[1] == 'runserver':
        t = threading.Thread(target=work_state, daemon=True)
        t.start()
        app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
    elif sys.argv[1] == 'cli':
        sys.argv.pop(1)
        run_cli()
    else:
        logging.error(f'Unknown command \"{sys.argv[1]}\"')


if __name__ == '__main__':
    main()
