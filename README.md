##PyPages: Easier Pagination

<br>
**Do pagination in python like a charm.**

##install

    pip install PyPages

##usage

```python
from pypages import Paginator

# Inside view func
def view():
    # get current page
    page = 3
    # retrieve the objects of the certain page
    # you should handle your data pagination yourself(database query or other ways)
    # make sure use the same per_page value and pass in the right objects total number
    objects = range(10)
    p = Paginator(100, per_page=10, current=page, range_num=5)
    # you can attach your objects to the paginator
    p.objects = objects
    return render_all(p=p)
    
def render_all(p):
    print "Your objects:"
    for o in p.objects:
        print o
    print "Your pages:"
    print "<ul>"
    print "<li><a href='1'>first</a></li>"
    for page in p.pages:
        if page == p.current:
            print "<li>%s</li>" % page
        else:
            print "<li><a href='%s'>%s</a></li>" % (page, page)
    print "<li><a href='%s'>last</a></li>" % p.page_num
    print "</ul>"

def render(p):
    print "Your objects:"
    for o in p.objects:
        print o
    print "Your pages:"
    print "<ul>"
    if p.has_previous:
        print "<li><a href='%s'>previous</a></li>" % p.previous
    print "<li>%s/%s</li>" % (p.current, p.page_num)
    if p.next: # pythonic, of course you can check p.has_next too
        print "<li><a href='%s'>next</a></li>" % p.next
    print "</ul>"
```

##api

*class* pypages.**Paginator**(*object_num, per_page=10, current=1, start=None, range_num=10*)  
***Parameters:***  

* **object_num** – the total number of items
* **per_page** – the maximum number of items to include on a page, default 10
* **current** – the current page number, default 1
* **start** – the start index for your page range, default to be current page minus half of the page range length
* **range_num** – the maximum page range length, default 10

    NOTICE: **page range** is the pages that will be displayed, like you have one page "5, 6, 7, 8, 9, 10", then your page range ``start`` is 5 and ``range_num`` is 6.

***Attributes:*** 

* **object_num** - the total number of items
* **per_page** – the maximum number of items to include on a page
* **current** – the current page number
* **start** – the start index for your page range
* **range_num** – the maximum page range length
* **end** - the end index for your page range
* **page_num** - the total number of pages
* **pages** - the page range, a list like `[4, 5, 6, 7, 8]`
* **has_previous** - bool value to indicate whether current page have previous page
* **has_next** - bool value to indicate whether current page have next page
* **previous** - the previous page number, if do not exist, will be `None`
* **next** - the next page number, if do not exist, will be `None`
