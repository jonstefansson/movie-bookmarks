# movie-bookmarks

A little bit of Python and JSON to keep track of bookmarks in some of my favorite movies.

## Usage

Generate the JSON structure for a new movie file. Specify the title and number of scenes/chapters.

```bash
./movie.py template --number 16 --title 'La La Land'
```

Generate a bookmarks listing.

```bash
./movie.py bookmarks < data/la_la_land.json
```
