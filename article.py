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

selectors = ["all"]

if sys.argv[1] == "new":
    article_name = sys.argv[2]
    if article_name in selectors: fail(f"Failed. Can not use special selectors in this context.")
    elif article_name in os.listdir("articles"): fail(f"Failed. Article \"{article_name}\" already exists.")
    name = f"articles/{article_name}"
    os.mkdir(f"{name}")
    os.mkdir(f"{name}/assets")
    os.close(os.open(f"{name}/config.yaml", os.O_CREAT))
    os.close(os.open(f"{name}/contents.md", os.O_CREAT))
    print(f"Created new article \"{article_name}\".")
elif sys.argv[1] == "get":
    selector = sys.argv[2]
    if os.path.isdir(os.path.join("articles", selector)) is True or selector in selectors: print(f"{color.FAINT}=========================={color.END}")
    if selector in selectors:
        if selector == "all":
            for dir in os.listdir("articles"):
                if str(dir).startswith("."): continue 
                else: _list(dir)
    else:
        if os.path.isdir(os.path.join("articles", selector)): _list(selector)
        else: fail("Failed. Article does not exist.")
elif sys.argv[1] == "remix":
    remixed_article_name = sys.argv[2]
    remix_article_name = sys.argv[3]
    if remixed_article_name in selectors: fail(f"Failed. Can not use special selectors in this context.")
    elif remixed_article_name not in os.listdir("articles"): fail(f"Failed. Article \"{remixed_article_name}\" does not exist.")
    elif remix_article_name in os.listdir("articles"): fail(f"Failed. Article \"{remixed_article_name}\" already exists.")
    shutil.copytree(os.path.join("articles", remixed_article_name), os.path.join("articles", remix_article_name))
    print(f"SUCCESS! Article \"{remix_article_name}\" has been remixed from \"{remixed_article_name}\".")
    pass
else:
    print("Usage: python3 article.py [command] [selector]")
    print("\n* Command List:")
    print("\t- get: Get information about an article.")
    print("\t- new: Create a new article.")
    print("\t- remix: Remix an article.")
    print("\n* Selector List:")
    print("\t- all: Get all articles.\t\t\t\t(special selector)")
    print("\t- recent: Get all articles created in the last 7 days.\t(special selector)")
    print("\t- remixed: Get all remixed articles.\t\t\t(special selector)")
    print("\t- help: Get help on a specific command.\t\t\t(special selector)")
    print("\t- [article]: Get a specific article.")