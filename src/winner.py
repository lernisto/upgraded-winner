import click

@click.command()
def main():
    click.echo(f"Hello, {__name__}.")

