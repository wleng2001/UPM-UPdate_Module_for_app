#check and install update
#import-------------------------
from datetime import datetime
from github import Github
#from git import Repo
import git
from os import getcwd
#update check-------------------
def update_check(last_update, repo_name):
    last_date=datetime.fromisoformat(last_update)
    g=Github()
    try:
        for i in g.search_repositories(repo_name):
            repo=i
        date=repo.pushed_at
        if date.date()==last_date.date():
            return False
        else:
            return True
    except:
        return None
#download update
def download_update(url, path):
    try:
        Repo.clone_from(url, path)
        git.Git(path).clone(url)
        return True
    except:
        return False

