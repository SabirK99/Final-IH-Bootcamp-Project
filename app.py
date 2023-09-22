from flask import Flask, redirect, render_template, request, url_for, session
from database.schema import db, db_session, User
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import base64
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)



#first door at url is nothing ('/')
@app.route('/')
def home():
   return render_template('home.html', title="Hiss - Home")

@app.route('/top-books')
def top_books():
    return render_template('top_books.html')


@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')

@app.route('/about-us')
def about_us():
   return render_template('about_us.html', title="About Us")

@app.route('/book/<int:id>')
def book(id):
   book_details = next((book for book in books if book["id"] == id), None)
   if not book_details:
       return "Book not found", 404
   return render_template('book.html', book=book_details)

books = [
    {"id": 1, "title": "Art of War", "author": "Sun Tzu"},
    {"id": 2, "title": "Can't Hurt Me", "author": "David Goggins"},
    {"id": 3, "title": "Aesop's Fables", "author": "Aesop", "summary": "A collection of fables credited to Aesop, a slave and storyteller believed to have lived in ancient Greece between 620 and 564 BCE."}
]

@app.route('/book/<book_id>')
def book_page(book_id):
    # For now, we'll just return the book name. 
    # Later, this can be replaced with a detailed book page
    # pulling info from a database or other source.
    return render_template('book_page.html', book_id=book_id)




@app.route('/search', methods=["GET"])
def search():
    query = request.args.get('query', '').lower()
    search_results = [book for book in books if query in book['title'].lower()]
    return render_template('search_results.html', results=search_results)



@app.route('/genre/<genre_name>')
def genre_detail(genre_name):
   
    descriptions = {
        "Romance": "A genre that focuses on the romantic relationships between characters.",
        "Thriller": "A genre characterized by suspenseful, fast-paced events.",

    }

    recommended_books = {
        "Romance": ["The Notebook", "Pride and Prejudice", "Outlander", "The Rosie Project"],
        "Thriller": ["The Girl with the Dragon Tattoo", "The Da Vinci Code", "Gone Girl", "The Reversal"],
 
    }

    description = descriptions.get(genre_name, "Description not available.")
    books = recommended_books.get(genre_name, [])

    return render_template('genre_detail.html', genre_name=genre_name, description=description, books=books)

@app.route('/art_of_war')
def art_of_war():
   return render_template('art_of_war.html')


@app.route('/aesops-fables')
def aesops_fables():
    encoded_pdf = pdf_to_base64('static/aesops_fables.pdf')
    return render_template('aesops_fables.html', encoded_pdf=encoded_pdf)


@app.route('/cant_hurt_me')
def cant_hurt_me():
   return render_template('cant_hurt_me.html')

@app.route('/the_witcher')
def the_witcher():
   return render_template('the_last_wish.html')

@app.route('/psycho_cybernetics')
def psycho_cybernetics():
   return render_template('psycho_cybernetics.html')

def pdf_to_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

@app.route('/results-dashboard')
def results_dashboard():
    return render_template('dashboard.html')



if __name__ == "__main__":
   app.run(debug=True)