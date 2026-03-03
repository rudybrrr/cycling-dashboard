import flask
import os 
from dotenv import load_dotenv

load_dotenv()
secret_key = os.getenv('SECRET_KEY')

app = flask.Flask(__name__)
app.secret_key = secret_key