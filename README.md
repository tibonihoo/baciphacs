baciphacs
=========

Bar charts in pure HTML and CSS.

This library is designed for the kind of (desesperate) situation where
you want to display bar charts but with the constraint that your HTML
document must not depend on additional files or remote webservices.

baciphacs will use basic HTML code with some bits of CSS style embeded
in tags, to display a reasonably readable chart.

If you need pretty or advanced graphs and don't have any strict
constraints on your HTML's dependency, many libraries exists that
generate much much better looking graphs.

baciphacs is licensed under [the 2 close BSD License](LICENSE.txt),
and more detailed information about it can be found at
[GitHub](https://github.com/tibonihoo/baciphacs).

It is tested on Travis-CI: [![Build Status](https://travis-ci.org/tibonihoo/baciphacs.png?branch=master)](https://travis-ci.org/tibonihoo/baciphacs) [![Coverage Status](https://coveralls.io/repos/tibonihoo/baciphacs/badge.png)](https://coveralls.io/r/tibonihoo/baciphacs)


Example for horizontal bar charts
---------------------------------

```python
from baciphacs import DataSample
from baciphacs import GenerateHTMLHorizontalBarChart

data = [("ba",3,2),("c",6,1),("i",2,1),("p",4,1),("h",4,1),("a",3,1),("cs",3,2)]
dataSamples = [DataSample._make(t) for t in data]
print GenerateHTMLHorizontalBarChart(dataSamples,numStdev=2,color="blue")
```

The Python code above will generate an HTML snippet that [renders like a bar chart](http://htmlpreview.github.io/?https://github.com/tibonihoo/baciphacs/blob/master/doc/index.html).

