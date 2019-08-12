#! /usr/local/bin/python3

from os import system
from click import command, option
from stashy import connect, projects


@command()
@option('-u', '--url', default='', help='Domain of the BitBucket server')
@option('-p', '--project', default='', help='Name of BitBucket project.')
def clone_repo(url, project):
    domain = 'https://{0}'.format(url)
    username = ''
    password = ''

    bitbucket = connect(domain, username, password)
    projects = bitbucket.projects.list()

    for project in projects:
        for repo in bitbucket.projects["%s" % (project["key"])].repos.list():
            for url in repo["links"]["clone"]:
                if (url["name"] == "ssh"):
                    system("git clone %s" % (url["href"]))


def main():
    clone_repo()

if __name__ == '__main__':
    main()
