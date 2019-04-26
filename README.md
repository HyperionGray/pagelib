# Pagelib
Pagelib is currently underdevelopment and is not ready for production or development environments.

## Introduction
Pagelib turns nasty HTML strings into friendly HTML objects.

An HtmlPage object is construced from an HTML string:
```
>>> from pagelib import HtmlPage
>>> page = HtmlPage('<html><head><title>Hello</title><meta name="description" content="Some page you've downloaded from the web and now have to parse."></meta></head><body><p>Hello, world!</p></body></html>')
>>> page
HtmlPage(title=Hello, bytes=121)
```

Components of the page can be accessed through it's properties:
```
>>> page.title
'Hello'
>>> page.description
'Some page you've downloaded from the web and now have to parse.'
>>> page.language_code
'en'
>>> page.language
'English'
>>> page.text
'Hello, world!'
```

Pagelib exposes a [parsel](https://github.com/scrapy/parsel) selector that can be used to extract further elements from the page using xpaths or css:
```
>>> page.selector.xpath('//p/text()').extract()
['Hello, world!']
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
