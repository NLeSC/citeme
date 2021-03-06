# Citeme

Citeme is a package to easily add citations to your code similar to bibtex
citations. Using decorators on your functions and classes a library of
citations is built when those functions and classes are used.

At the end of your script you can output the citations to a bibtex file,
html or plain text

## Examples

### Writing to a bibtex file
```python
import citeme

@citeme.article('my_handle', {
    'author': 'Johnny Awesome',
    'title': 'A short guide to being awesome',
    'journal': 'Acme Journal on Cartoon Properties',
    'year': '2017',
    'volume': '4'
})
def my_func():
    return True

# Calling the function will add the citation to the
# library
my_func()

# Write all the citations to a bibtex file
write_to_bibtex('called.bib')
```

#### Resulting called.bib
```latex
@article{my_handle,
 author = {Johnny Awesome},
 journal = {Acme Journal on Cartoon Properties},
 title = {A short guide to being awesome},
 volume = {4},
 year = {2017}
}
```

### iPython Notebooks
You can use this package in a notebook as well. To display the notebook inline use the `display_bibliography` function.
See the example notebook for more information.

### Terminal Output
```python
import citeme

@citeme.article('my_handle', {
    'author': 'Johnny Awesome',
    'title': 'A short guide to being awesome',
    'journal': 'Acme Journal on Cartoon Properties',
    'year': '2017',
    'volume': '4'
})
def my_func():
    return True

# Calling the function will add the citation to the
# library
my_func()

# Write the citations to the standard out
citeme.print_references()

# Example output
>>> article my_handle {'volume': '4', 'author': 'Johnny Awesome', 'journal': 'Acme Journal on Cartoon Properties', 'title': 'A short guide to being awesome', 'year': '2017'}
```

### HTML Output
Html output can be created using the `write_to_html` function. If you have beautiful soup installed (version 3 or 4) the output will be
pretty printed.

#### Full html output
```python
import citeme

@citeme.article('my_handle', {
    'author': 'Johnny Awesome',
    'title': 'A short guide to being awesome',
    'journal': 'Acme Journal on Cartoon Properties',
    'year': '2017',
    'volume': '4'
})
def my_func():
    return True

# Calling the function will add the citation to the
# library
my_func()

# Write all the citations to a html file
# full=True means the html file will have html, head and body tags
citeme.write_to_html('called.html', full=True)
```
#### Resulting html file
```html
<html>
<head>
    <link rel="stylesheet" href="css/bibstyle.css" />
</head>
</html>
<body>
<fieldset class="the_bibliography">
    <legend>The Bibliography</legend>
    <ol class="references">
        <li>
        <cite class="bib-entry" id="my_handle">
        <span class="bib-entry-field bib-entry-author">Johnny Awesome</span>
        <span class="bib-entry-field bib-entry-title">A short guide to being awesome</span>
        <span class="bib-entry-field bib-entry-journal">Acme Journal on Cartoon Properties</span>
        <span class="bib-entry-field bib-entry-volume">4</span>
        <span class="bib-entry-field bib-entry-year">2017</span>
        </cite>
        </li>
    </ol>
</fieldset>
</body>
```

#### Bibliography only html output
```python
import citeme

@citeme.article('my_handle', {
    'author': 'Johnny Awesome',
    'title': 'A short guide to being awesome',
    'journal': 'Acme Journal on Cartoon Properties',
    'year': '2017',
    'volume': '4'
})
def my_func():
    return True

# Calling the function will add the citation to the
# library
my_func()

# Write all the citations to a html file
# full=False means the html file will _not_ have html, head and body tags
citeme.write_to_html('called.html', full=False)
```
#### Resulting html file
```html
<fieldset class="the_bibliography">
    <legend>The Bibliography</legend>
    <ol class="references">
        <li>
        <cite class="bib-entry" id="my_handle">
        <span class="bib-entry-field bib-entry-author">Johnny Awesome</span>
        <span class="bib-entry-field bib-entry-title">A short guide to being awesome</span>
        <span class="bib-entry-field bib-entry-journal">Acme Journal on Cartoon Properties</span>
        <span class="bib-entry-field bib-entry-volume">4</span>
        <span class="bib-entry-field bib-entry-year">2017</span>
        </cite>
        </li>
    </ol>
</fieldset>
```