#!/usr/bin/env python3

import argparse
from template import Template
from bookmarks import Bookmarks

def template():
    """Generates a template to bootstrap a new data file
    
    Usage: ./movie.py template -n 20 --title 'Bull Durham'
    """
    Template.generate(title=cli_args.title, num_chapters=cli_args.number)

def bookmarks():
    """Displays bookmarks with chapters
    
    Usage: ./movie.py bookmarks < data/movie_file.json
    """
    Bookmarks.display()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Toolkit for working with movie files'
    )

    parser.add_argument(
        dest='command',
        metavar='command',
        help='The command to execute: template | bookmarks',
        choices=['template', 'bookmarks']
    )

    parser.add_argument(
        '-n', '--number'
    )

    parser.add_argument(
        '-t', '--title'
    )

    cli_args = parser.parse_args()
    # invoke the function designated by the command argument
    locals()[cli_args.command]()
