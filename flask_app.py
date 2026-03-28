from flask import Flask, render_template, request
from database import Book, PriceHistory, get_book
import matplotlib.pyplot as plt
import io
import base64
from peewee import fn
import statistics 


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/price_history', methods=['POST', 'GET'])
def price_history() -> str:
    if request.method == 'POST':
        item = request.form.get('content')
        book = get_book(item)
        if not book:
            return render_template('price_history.html', error="Please enter a book title.")
        price_history = PriceHistory.select().where(PriceHistory.book == book).order_by(PriceHistory.created_at.desc())
        if not price_history:
            return render_template('price_history.html', error="No price history found for this book.")
        return render_template('price_history.html', price_history=price_history, book_title=book.title)
    
    else:
        return render_template('price_history.html')

@app.route('/analytics', methods=['POST', 'GET'])
def analytics() -> str:
    if request.method == 'POST':
        item = request.form.get('content')
        book = get_book(item)
        if not book:
            return render_template('analytics.html', error="Please enter a book title.")
        try:
            buf = io.BytesIO()
            prices = [p.price for p in PriceHistory.select(PriceHistory.price).where(PriceHistory.book == book)]
            if not prices:
                return render_template('analytics.html', error="No price history found for this book.")
            min_price = min(prices)
            max_price = max(prices)
            avg_price = round(statistics.mean(prices), 2)
            fig, ax = plt.subplots()
            ax.plot([int(num + 1) for num in range(len(prices))], prices)
            ax.grid(True)
            ax.set_title(f'Price analysis of \"{book.title}\"')
            fig.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode()
            return render_template('analytics.html', img_base64=img_base64, min_price=min_price, 
                                   max_price=max_price, avg_price=avg_price)
        except Exception as e:
            return render_template('analytics.html', error=f"An error occurred while processing the data: {e}")
        
    else:
        return render_template('analytics.html')


@app.route('/database', methods=['GET'])
def database() -> str:
    books = Book.select().order_by(Book.title)
    return render_template('database.html', books=books)

