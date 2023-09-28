import click

from views.authentication import login, signup


@click.group()
def cli():
    pass


@click.group()
def authentication():
    pass


authentication.add_command(login)
authentication.add_command(signup)
