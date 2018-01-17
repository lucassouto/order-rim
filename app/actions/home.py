""" Home Page Actions """
from app import app

@app.route('/')
def index():
        return 'Hello', 200
