# Financial-news-collectors

# Introduction


# How to use it


# Technical details

## Back-of-the-envelope calculations

## Technology stack

## How it works

# Future functionalities


* Due to Bloomberg's anti bot features (which blocks any get request to urls), it was decided to open/close a browser everytime a url is visted. This, even if a bit unperformant, circumbents this issue and allows for retrieval of the pages.

## To DO

* Add logging functionality
* Add unit testing to at least the basic extraction functions
* Improve documentation
* Add frontend to do some basic analytics
* Replace SQL insert functionality to do it more efficiently (currently it is being done via pandas)
* Add type hinting to all functions