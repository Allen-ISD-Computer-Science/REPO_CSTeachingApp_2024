#!/opt/homebrew/bin python3

# this is a script

# One liners are like Modern Art, With the exception of the artist, no one understands the meaning.

import os
import sys
import yaml
import time
import shutil

# assert ((len(sys.argv)) > 1 + 1) == 1
# assert ((len(sys.argv)) < 3 + 1) == 1

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    FAINT = "\033[2m"
    ITALIC = "\033[3m"

def fail(msg):
    print(msg) 
    exit(1)

def field(_for, _value, _color):
    print(f"{_color}{_for}{color.END}: {_value}")
    return 

def _list(selector):
    with open(f"articles/{selector}/config.yaml", 'r') as f: article = yaml.dump(yaml.safe_load(f))
    article = yaml.load(article, Loader=yaml.SafeLoader)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    article_title = article["title"]
    article_author = article["author"]
    article_time = time.localtime(article['published'])
    article_time = f"{months[article_time.tm_mon - 1]} {article_time.tm_mday} {article_time.tm_year}"
    article_languages = article['languages']
    article_languages.sort()
    languages_list_helper = ', '.join(['Russian' if language == 'ru' else 'Arabic' if language == 'ar' else 'Chinese' if language == 'zh' else 'Unknown' for language in article_languages])
    field("Title", article_title, color.YELLOW)
    field("Author", article_author, color.DARKCYAN)
    field("Published", article_time, color.PURPLE)
    field("Directory Key", selector, color.RED)
    field("Languages", 'English' + (str(', ' + languages_list_helper) if languages_list_helper != '' else ''), color.DARKCYAN)
    print(f"{color.FAINT}=========================={color.END}")

class Domain:

    @staticmethod
    def new(article_name): ...

    @staticmethod
    def get(selector): ...

    @staticmethod
    def remix(remixed_article_name, remix_article_name): ...

class Article(Domain):

    @staticmethod
    def new(article_name):
        if article_name in selectors: fail(f"Failed. Can not use special selectors in this context.")
        elif article_name in os.listdir("articles"): fail(f"Failed. Article \"{article_name}\" already exists.")
        name = f"articles/{article_name}"
        os.mkdir(f"{name}")
        os.mkdir(f"{name}/assets")
        os.close(os.open(f"{name}/config.yaml", os.O_CREAT))
        os.close(os.open(f"{name}/contents.md", os.O_CREAT))
        print(f"Created new article \"{article_name}\".")

    @staticmethod
    def get(selector):
        if os.path.isdir(os.path.join("articles", selector)) is True or selector in selectors: print(f"{color.FAINT}=========================={color.END}")
        if selector in selectors:
            if selector == "all":
                for dir in os.listdir("articles"):
                    if str(dir).startswith("."): continue 
                    else: _list(dir)
        else:
            if os.path.isdir(os.path.join("articles", selector)): _list(selector)
            else: fail("Failed. Article does not exist.")

    @staticmethod
    def remix(remixed_article_name, remix_article_name):
        if remixed_article_name in selectors: fail(f"Failed. Can not use special selectors in this context.")
        elif remixed_article_name not in os.listdir("articles"): fail(f"Failed. Article \"{remixed_article_name}\" does not exist.")
        elif remix_article_name in os.listdir("articles"): fail(f"Failed. Article \"{remixed_article_name}\" already exists.")
        shutil.copytree(os.path.join("articles", remixed_article_name), os.path.join("articles", remix_article_name))
        print(f"SUCCESS! Article \"{remix_article_name}\" has been remixed from \"{remixed_article_name}\".")

class Page(Domain):

    @staticmethod
    def new(page_name): 
        if page_name in selectors: fail(f"Failed. Can not use special selectors in this context.")
        elif f"{page_name}.md" in os.listdir("pages"): fail(f"Failed. Page \"{page_name}\" already exists.")
        name = f"pages/{page_name}.md"
        os.close(os.open(f"{name}", os.O_CREAT))
        print(f"Created new page \"{page_name}\".")
        return

    @staticmethod
    def get(selector):
        if os.path.isfile(os.path.join("pages", f"{selector}.md")) is True or selector in selectors: print(f"{color.FAINT}=========================={color.END}")
        if selector in selectors:
            if selector == "all":
                for dir in os.listdir("pages"):
                    if str(dir).startswith("."): continue 
                    print(dir)
        else:
            if os.path.isfile(os.path.join("pages", f"{selector}.md")): print(f"{selector}.md")
            else: fail("Failed. Page does not exist.")
        print(f"{color.FAINT}=========================={color.END}")

    @staticmethod
    def remix(remixed_page_name, remix_page_name):
        if remixed_page_name in selectors: fail(f"Failed. Can not use special selectors in this context.")
        elif str(remixed_page_name + ".md") not in os.listdir("pages"): fail(f"Failed. Page \"{remixed_page_name}\" does not exist.")
        elif remix_page_name in os.listdir("pages"): fail(f"Failed. Page \"{remixed_page_name}\" already exists.")
        os.close(os.open(f"pages/{remix_page_name}.md", os.O_CREAT))
        with open("pages/" + remixed_page_name + ".md", 'r') as f: 
            data = f.read()
            with open("pages/" + remix_page_name + ".md", 'w') as f: f.write(data)
        print(f"SUCCESS! Page \"{remix_page_name}\" has been remixed from \"{remixed_page_name}\".")

selectors = ["all"]
domains = ["article", "page"]

if sys.argv[1] == "new": 
    if sys.argv[2] not in domains: fail(f"Failed. Domain \"{sys.argv[2]}\" does not exist.")
    match sys.argv[2]:
        case "page": Page.new(sys.argv[3])
        case "article": Article.new(sys.argv[3])
elif sys.argv[1] == "get": 
    if sys.argv[2] not in domains: fail(f"Failed. Domain \"{sys.argv[2]}\" does not exist.")
    match sys.argv[2]:
        case "page": Page.get(sys.argv[3])
        case "article": Article.get(sys.argv[3])
elif sys.argv[1] == "remix": 
    if sys.argv[2] not in domains: fail(f"Failed. Domain \"{sys.argv[2]}\" does not exist.")
    match sys.argv[2]:
        case "page": Page.remix(sys.argv[3], sys.argv[4])
        case "article": Article.remix(sys.argv[3], sys.argv[4])
else:
    print('''
    Usage: python3 article.py [command] [domain] [selector]
    
    * Command List:
        - get: Get information about an existing [domain] or [domain]s.
        - new: Create a new [domain].
        - remix: Remix a [domain].
        - help: Shows this message.

    * Domain List:
        - article: Article in articles directory.
        - pages: Page in pages directory.
    
    * Selector List:
        - all: Get all instances of a [domain]s.
        - (unimplemented) [key]: Fetch a [domain] indexed by [key].
        - (unimplemented) recent: Get all [domain]s created in the last 7 days.
        - (unimplemented) remixed: Get all remixed [domain]s.
        - (unimplemented) help: Get help on a specific command.
    ''')