#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: project-cloner

Usage: This python-based CLI utility is used to clone all repos within a BitBucket project.

Options:
    -d --domain      Domain of the BitBucket server.
    -p --project      Name of the BitBucket project.
    -U --username  Username for BitBucket server.
    -P --password   Password for BitBucket server.
    -h --help     Help info.
"""

from os import system
from click import command, option
from stashy import connect, projects

__author__ = "Andrew Kuttor"
__credits__ = "Andrew Kuttor"
__version__ = "1.0"
__maintainer__ = "Andrew Kuttor"
__email__ = "andrew.kuttor@gmail.com"


@command()
@option('-d', '--domain', help='BitBucket server')
@option('-p', '--project', help='BitBucket project')
@option('-U', '--username', help='BitBucket username')
@option('-P', '--password', prompt=True, hide_input=True, help='BitBucket password')
def clone_repo(domain, project, username, password):
    """ Clones all BitBucket repos within a Project """
    domain = 'https://{0}'.format(domain)

    bitbucket = connect(domain, username, password)
    repos = bitbucket.projects[project].repos.list()

    for repo in repos:
         for url in repo["links"]["clone"]:
              if (url["name"] == "ssh"):
                   system("git clone {0}".format(url["href"]))


def main():
    clone_repo()


if __name__ == '__main__':
    main()
