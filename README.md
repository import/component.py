# component.py [![Build Status](https://travis-ci.org/import/component.py.png)](https://travis-ci.org/import/component.py) [![Coverage Status](https://coveralls.io/repos/import/component.py/badge.png?branch=master)](https://coveralls.io/r/import/component.py?branch=master)




Component.py is a python library that makes consuming bower components from 
within your python application easy.

## What is wrong with PyPI?

Lot's of things, which I can't be bothered to actually write out now so just 
imagine a list of compelling reasons and nod slowly and think to yourself 
"hmm, yep he is right".

## Basic Idea

Bower was designed for the frontend but the ideas behind it can also apply 
to server-side stuff, and indeed this works well with Node.js. But why stop 
there? I want to use this with my python projects.


```
danielchatfield-example-component/
    __init__.py
    bower.json
    template.html
    styles.css
```

A python bower component must provide an __init__.py file otherwise python 
will not allow it to be loaded as a module.

To see more implementation details check out the [WIP spec](https://github.com/import/component.py/wiki/Spec-for-Component.py)