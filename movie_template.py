import sys
import json
import itertools

def generate(title=None, num_chapters='1'):
    document = dict()
    document['title'] = title
    document['year'] = ''
    chapters = [dict(number=str(c), title='', time='00:00:00', bookmarks=[]) for c in range(1, int(num_chapters)+1)]
    document['chapters'] = chapters
    json.dump(document, sys.stdout, indent=2)
