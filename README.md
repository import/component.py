# component.py [![Build Status](https://travis-ci.org/import/component.py.png)](https://travis-ci.org/import/component.py) [![Coverage Status](https://coveralls.io/repos/import/component.py/badge.png?branch=master)](https://coveralls.io/r/import/component.py?branch=master)




Component.py is a python library that makes consuming small components from within your python application easy.

## What is wrong with PyPI?

Lot's of things, which I can't be bothered to actually write out now so just imagine a list of compelling reasons and nod slowly and think to yourself 
"hmm, yep he is right".

## We don't need another package manager!

I know, which is why component isn't a package manager - it works with whatever package manager you use ([Bower](http://bower.io/), [component(1)](https://github.com/component/component/)). The only condition is that your package manager installs all components into a single, flat directory (no nested dependencies):

```
components/
    a-component/
    another-component/
    a-dependency/
```

# Usage

## Defining a component

A python component is just a python package and thus has to have an `__init__.py` file.

## Consuming a component

Technically you can just use regular python imports:

```python
import my_component
from another_component import trevor
```

However I reccomend that instead you use `component.require` like so:

```python

from component import require
my_component = require("my-component")
```

The reasons for this are:

* We want to be able to use hyphens in names (like how node modules work).
* In the future components will be able to export objects (which will not work with regular imports) e.g.:

```python
qrcode = require("qrcode")
qrcode(url="http://www.danielchatfield.com")
```

```python
import qrcode
qrcode.qrcode(url="http://www.danielchatfield.com")
```


To see more implementation details check out the [WIP spec](https://github.com/import/component.py/wiki/Spec-for-Component.py)