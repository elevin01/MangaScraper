from flask import Flask, render_template, request
from scraper import scrape_manga

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    manga_title = request.form['manga_title']
    manga_data = scrape_manga(manga_title)
    if manga_data:
        #print(f"This was called!{manga_data}")
        return render_template('result.html', manga_data=manga_data)
    else:
        manga_data = {'title': 'Default Title',
            'latest_chapter': 'Default Latest Chapter',
            'latest_chapter_link': 'Default Latest Chapter Link'}
        return render_template('result.html', manga_data=manga_data)

if __name__ == '__main__':
    app.run(debug=True)


