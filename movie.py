#!/usr/bin/env /Users/jon/Documents/dev/python/workbench/venv/bin/python3

from template import Template
from bookmarks import Bookmarks
import click


@click.group()
def cli():
    pass


@click.command()
@click.option('--count', default=1, help='number of chapters')
@click.option('--title', required=True, help='Movie title')
def template(count, title):
    """Generates a template to bootstrap a new data file
    """
    Template.generate(title=title, num_chapters=count)


@click.command()
@click.argument('input', type=click.File('rt'))
def bookmarks(input):
    """Displays bookmarks with chapters
    """
    Bookmarks.display(input)


cli.add_command(template)
cli.add_command(bookmarks)


if __name__ == '__main__':
    cli()
