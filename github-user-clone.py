#! /usr/bin/env python3

import argparse
import os
from github import Github
import git

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
            description='Clone all of a users repos to the given path',
            epilog="Repos will be stored in ${target-path}/${user}/${repo}/")
    parser.add_argument('--user',nargs='+',type=str,required=True)
    parser.add_argument('--target-path',type=str,required=True)

    args = parser.parse_args()
    g = Github()

    for user in args.user:
        print("User: " + user)

        for repo in g.get_user(user).get_repos():
            clone_path = os.path.join(args.target_path, user, repo.name)

            if os.path.isdir(clone_path):
                print("Updating: " + repo.name)
                git.Repo(clone_path).remotes.origin.pull()
            else:
                print("Cloning: " + repo.name)
                git.Repo.clone_from(repo.clone_url, clone_path)
