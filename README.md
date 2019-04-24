# Pagelib
Pagelib turns nasty HTML strings into friendly HTML objects.

Pagelib is currently underdevelopment and is not ready for production or development environments.

## Quickstart
```
from pagelib import HtmlPage
page = HtmlPage('<html><head><title>Hello</title></head><body>Hello, world!</body></html>')

print(page.title)
'Hello'

print(page.text)
'Hello, world!'
```

## Installation

### Installing from PyPI
```
$ pip install pagelib
```

### Dependencies
Pagelib depends on [libicu-dev](https://packages.debian.org/sid/libicu-dev), which can be installed by running the following command:

```
$ sudo apt install libicu-dev

```
