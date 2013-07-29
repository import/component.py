# Spec

This is very much a work in progress.

### Consuming components in python

Not sure how things are going to work out yet, probably going to be either:

```python
from component import example_content
```

Which requires some magic to get it to import the right module (although I'm fairly confident that I know how to do this).

Downsides of this approach is 

```python
from component import require

example_component = require("example-component")
```