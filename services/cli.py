import argparse
import logging
from services import (
    update_data, get_price_history, get_analytics, 
    add_one_element, work_state, delete_element
)



def run_cli():
    parser = argparse.ArgumentParser(description='CLI for book price tracking', prog='Book price tracker')
    subparsers = parser.add_subparsers(help='Commands help')

    # Update database
    parser_update = subparsers.add_parser('update', aliases=['up'],help='Refresh the database')
    parser_update.set_defaults(func=lambda: update_data())

    # Update one element
    parser_single_update = subparsers.add_parser('add_single', aliases=['ads'], help='Add single element to the db')
    parser_single_update.add_argument('item', type=str, help='Book name')
    parser_single_update.add_argument('price', type=float, help='Price')
    parser_single_update.set_defaults(func=add_one_element)

    # Price history
    parser_history = subparsers.add_parser('history', aliases=['hi'], help='Get price history of a particular book')
    parser_history.add_argument('item', type=str, help='Book name')
    parser_history.set_defaults(func=get_price_history)

    # Analytics
    parser_analytics = subparsers.add_parser('analytics', aliases=['al'], help='Get analytics of a particular book')
    parser_analytics.add_argument('item', type=str, help='Book name')
    parser_analytics.set_defaults(func=get_analytics)

    # Delete element
    parser_delete = subparsers.add_parser('delete_element', aliases=['del'], help='Delete element from the db' )
    parser_delete.add_argument('item', type=str, help='Book name')
    parser_delete.set_defaults(func=delete_element)

    # Workstate
    parser_work_state = subparsers.add_parser('workstate', aliases=['ws'], help='Simulate the work of the service')
    parser_work_state.set_defaults(func=work_state)


    args = parser.parse_args()
    if hasattr(args, 'func'):
        kwargs = {k: v for k, v in vars(args).items() if k != 'func'}
        try:
            args.func(**kwargs)
        except Exception as e:
            logging.error(e)
    else:
        parser.print_help()