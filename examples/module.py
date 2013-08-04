from component import export

@export
def my_function():
    pass


# from within application

from flask import current_app

flask_cache = require("flask-cache") # need a way of aliasing import-flask-cache to flask-cache locally


# Load current module context (cached?)
# Lookup module
# Load module (including voodoo that caches it in sys.modules?)