import click

from list_cleanup import list_cleanup

@click.command()
@click.option('--key', required=True, type=str)
@click.option('--token', required=True, type=str)
@click.option('--board', required=True, type=str)
def main(key, token, board):
    list_cleanup(key, token, board)

if __name__ == '__main__':
    main()