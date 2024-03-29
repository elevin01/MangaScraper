from flask import Flask, render_template, request
from scraper import scrape_manga

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    manga_title = request.form['manga_title']
    manga_data = scrape_manga(manga_title)
    return render_template('result.html', manga_data=manga_data)

if __name__ == '__main__':
    app.run(debug=True)
