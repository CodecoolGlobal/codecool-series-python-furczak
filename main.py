from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows/most-rated/')
@app.route('/shows/most-rated/<int:page>/')
def shows_most_rated(page=1):
    page_number = queries.get_page_number()['num']
    shows = queries.get_most_rated_shows(page)
    return render_template('most_rated.html', title='Most rated shows',
                           shows=shows, num=page_number, current_page=page)


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
