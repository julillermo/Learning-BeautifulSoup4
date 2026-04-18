from bs4 import BeautifulSoup

RAW_SAMPLE_HMTL = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


def prettify_demo(soup_obj: BeautifulSoup):
    print(soup_obj.prettify())


def simple_navigation_demo(soup_obj: BeautifulSoup):

    title = soup_obj.title
    # <title>The Dormouse's story</title>

    title_name = title.name if title else None
    # u'title'

    title_string = title.string if title else None
    # u'The Dormouse's story'

    title_parent = title.parent if title else None

    title_parent_name = title_parent.name if title_parent else None
    # u'head'

    p_tag = soup_obj.p
    # <p class="title"><b>The Dormouse's story</b></p>

    p_tag_class_attr = p_tag["class"] if p_tag else None
    # u'title'

    a_tag = soup_obj.a
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    soup_obj.find_all("a")
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    soup_obj.find(id="link3")
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

    print(f"soup.title: {title}\n")
    print(f"soup.title.name: {title_name}\n")
    print(f"soup.title.string: {title_string}\n")
    print(f"soup.title.parent.name: {title_parent_name}\n")
    print(f"soup.p: {soup_obj.p}\n")
    print(f"soup.p['class']: {p_tag_class_attr}\n")
    print(f"soup.a: {a_tag}\n")
    print(f"soup.find_all('a'): {soup_obj.find_all('a')}\n")
    print(f"soup.find(id='link3'): {soup_obj.find(id='link3')}\n")


def extract_all_urls(soup_obj: BeautifulSoup):
    all_a_tags = soup_obj.find_all("a")
    for link in all_a_tags:
        print(link.get("href"))


def extract_all_text_from_page(soup_obj: BeautifulSoup):
    print(soup_obj.get_text())


def main():
    soup = BeautifulSoup(RAW_SAMPLE_HMTL, "html.parser")
    # prettify_demo(soup)
    # simple_navigation_demo(soup)
    # extract_all_urls(soup)
    extract_all_text_from_page(soup)


if __name__ == "__main__":
    main()
