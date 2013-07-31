# component.py [![Build Status](https://travis-ci.org/import/component.py.png)](https://travis-ci.org/import/component.py) [![Coverage Status](https://coveralls.io/repos/import/component.py/badge.png?branch=master)](https://coveralls.io/r/import/component.py?branch=master)




Component.py is a python library that makes using [component(1)](https://github.com/component/component/) components from within your python application easy.

Right now this is just a collection of vague ideas in my head which over time will hopefully settle into a stable, usable library but until then expect breaking changes frequently. I not sure how/if some of the things I want can be implemented in python.

## Want to get involved?

You can open an issue detailing any concerns you may have or functionality you desire.

## What is wrong with PyPI?

Lot's of things, which I can't be bothered to actually write out now so just imagine a list of compelling reasons and nod slowly and think to yourself "hmm, yep he is right".

## Basic Idea

If you don't know what component(1) is then go and [check that out](https://github.com/component/component/) first.

Component was designed for javascript but the ideas behind it (small, highly modular, pieces of code) can also apply to server-side stuff, and indeed this works well with Node.js. But why stop there? I want to use this with my python projects.

Python components are just like regular components except they include python files an example python component is below:

```
danielchatfield-example-component/
    __init__.py
    component.json
    template.html
    styles.css
```

This component has a python file, an html template file and a stylesheet. Often python components will just have python files.

To see more implementation details check out the [WIP spec](https://github.com/import/component.py/wiki/Spec-for-Component.py)