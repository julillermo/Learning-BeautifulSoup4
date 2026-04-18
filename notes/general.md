# Making the soup

- You pass in-memory string into the `BeautifulSoup()` constructor.
  - You typically first perform a read operation from a file (using `with open(...)`) or a an API call using `requests` or `httpx` to generate the string
- The `BeautifulSoup()` constructor converts to **Unicode**
- Defaults to HTML parser unless otherwise specified.

# Kinds of Objects

## Tag

The HTML tag in an HTML document

```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
```

#### Name

- `tag.name`
- This is essentially the hardcoded text of the tag (ex. `<title></title>` -> `title`)

#### Attributes

- `tag['id']`
  - if `<b id="boldest">` -> `boldest`
- `tag.attrs`
  - Alternative way to call asside from the above
- Treat tags like a python dictionary (key-value pair). Once loaded into the `BeautifulSoup()` constructor, the contents can be edited.
- If an attribute contains more than 1 value ex. `<p class="body strikeout"></p>`, those will be captured as `["body", "strikeout"]`
  - Only attributes that can be **multi-valued**, as defined by the HTML standard, work as described above.
  - Other attributes that aren't **multi-valued** will captuire spaces as a string.
  - You can also enforce to ignore **multi-valued** attributes when instantiating a BeauituflSoup instance
    - Pass in `multi_valued_attributes=None` into the constructor
  - This **multi-valued** option is disabled when parsed using `xml`
- How to input multiple attributes
  - `rel_sup.a['rel'] = ['index', 'contents']` -> `<p>Back to the <a rel="index contents">homepage</a></p>`

##### Multi-valued attributes

## NavigabbleString

## BeauitulSoup

## Comment
