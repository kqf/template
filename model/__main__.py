import click
from model.model import build_model


@click.command()
@click.option('--data',
              type=click.Path(exists=True),
              help='Path to the dataset',
              required=True)
def main(data):
    build_model()
