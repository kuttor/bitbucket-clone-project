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
@option('-u', '--url', default='', help='BitBucket server')
@option('-p', '--project', default='', help='BitBucket project')
def clone_repo(url, project):
    """ Clones all BitBucket repos within a Project """
    domain = 'https://{0}'.format(url)
    username = 'andrew.kuttor'
    password = 'Sheas1731!'

    bitbucket = connect(domain, username, password)
    repos = bitbucket.projects[project].repos.list()

    for project in projects:
        for repo in repos:
            for url in repo["links"]["clone"]:
                if (url["name"] == "ssh"):
                    system("git clone {0}".format(url["href"]))


def main():
    clone_repo()


if __name__ == '__main__':
    main()
