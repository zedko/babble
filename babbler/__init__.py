from flask import Flask


app = Flask(__name__)

from babbler import routes
