from flask_frozen import Freezer
from app import app

# Monkey patch Frozen-Flask to work with newer Python versions
import flask_frozen
import collections.abc
flask_frozen.collections.Mapping = collections.abc.Mapping

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()