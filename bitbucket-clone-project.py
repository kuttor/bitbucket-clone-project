#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: bitbucket-clone-project

Usage: This python-based CLI utility is used to clone all repos within a BitBucket project.

Options:
    -u --url      Domain of the BitBucket server.
    -p --project  Name of the BitBucket project.
    -h --help     Help info.
"""

from os import system
from click import command, option
from stashy import connect, projects

__author__ = "Andrew Kuttor"
__credits__ = "Andrew Kuttor"
__version__ = "1.0"
__maintainer__ = "Andrew Kuttor"
__email__ = "andrew.kuttor@cis.ntt.com"


@command()
@option('-u', '--url', default='', help='Domain of the BitBucket server')
@option('-p', '--project', default='', help='Name of BitBucket project.')
def clone_repo(url, project):
    """ Clones all BitBucket repos within a Project """
    domain = 'https://{0}'.format(url)
    username = ''
    password = ''

    bitbucket = connect(domain, username, password)
    projects = bitbucket.projects.list()

    for project in projects:
        for repo in bitbucket.projects[project["key"]].repos.list():
            for url in repo["links"]["clone"]:
                if (url["name"] == "ssh"):
                    system("git clone {0}".format(url["href"]))


def main():
    clone_repo()

if __name__ == '__main__':
    main()
