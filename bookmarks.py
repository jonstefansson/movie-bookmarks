import sys
import json

class Bookmarks:
    
    @staticmethod
    def display():
        document = json.load(sys.stdin)
        for chapter in document.get('chapters', []):
            print('{:>2} | {} |'.format(
                chapter.get('number'),
                chapter.get('time')
            ))
            for bookmark in chapter.get('bookmarks', []):
                print('{:>2} | {} | {}'.format(
                    '',
                    bookmark.get('time'),
                    bookmark.get('note')
                ))
                

    @staticmethod
    def starbookmarks():
        document = json.load(sys.stdin)
        chapters = document.get('chapters', [])
        bookmarks = [bookmark for chapter in chapters for bookmark in chapter.get('bookmarks') ]
        print(len(bookmarks))
