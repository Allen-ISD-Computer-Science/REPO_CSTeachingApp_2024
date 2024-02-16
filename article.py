#!/opt/homebrew/bin python3

# this is a script

import os
import sys
import yaml
import time

# FIXME: Do not serve if YAML File is not finished. 

assert ((len(sys.argv)) > 1 + 1) == 1
assert ((len(sys.argv)) < 3 + 1) == 1

if sys.argv[1] == "new":
    name = f"articles/{sys.argv[2]}"
    os.mkdir(f"{name}")
    os.mkdir(f"{name}/assets")
    os.close(os.open(f"{name}/config.yaml", os.O_CREAT))
    os.close(os.open(f"{name}/contents.md", os.O_CREAT))
elif sys.argv[1] == "get":
    selector = sys.argv[2]
    if selector == "all":
        print("==========================")
        for dir in os.listdir("articles"):
            if str(dir).startswith("."): continue
            with open(f"articles/{dir}/config.yaml", 'r') as f: article = yaml.dump(yaml.safe_load(f))
            article = yaml.load(article, Loader=yaml.SafeLoader)
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            article_title = article["title"]
            article_author = article["author"]
            article_time = time.localtime(article['published'])
            article_time = f"{months[article_time.tm_mon - 1]} {article_time.tm_mday} {article_time.tm_year}"
            print(f"Title: {article_title}")
            print(f"Author: {article_author}") 
            print(f"Published: {article_time}")
            print(f"Directory Key: {dir}")
            print("==========================")
    # with open(f"articles/{selector}/config.yaml", 'r') as f: article = yaml.dump(yaml.safe_load(f))
elif sys.argv[1] == "remix":
    print("Failed. Support has not yet been added.")
