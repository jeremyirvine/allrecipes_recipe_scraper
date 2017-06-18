# Allrecipes.com Recipe Scraper (Python)
A python recipe scraper that stores the images, name, ingredients and instructions in the same directory

# Installing Drivers
This scraper needs the aid of a chrome web driver provided by google.<br>
Go and get chromedriver_win32.zip (_mac64 for OSX, _linux64 and _linux32 for 64 bit and 32 bit linux respectively) from https://chromedriver.storage.googleapis.com/index.html?path=2.30/, extract it, and put it in ```C:\Program Files\chromedriver\chromedriver.exe```

# Usage
Using the tool is quite simple, in the source code set `page_start` and `page_end` to some page numbers<br>
Example:
```python
...
page_start = 100

page_end = 150
...
```
This will scrape 50 pages (~20 recipes each) page 100-150