import sys
import json
import itertools

class Template:
    
    @staticmethod
    def generate(title=None, num_chapters='1'):
        document = dict(
            title=title,
            year='',
            chapters=[
                dict(
                    number=str(c),
                    title='',
                    time='00:00:00',
                    bookmarks=[
                        dict(time='00:00:00', note='')
                    ]
                ) for c in range(1, int(num_chapters)+1)
            ]
        )
        json.dump(document, sys.stdout, indent=2)
