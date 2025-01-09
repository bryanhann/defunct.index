import sys
import getpass
import argparse

from github import Github, GithubException

assert __name__ == '__main__'

parser=argparse.ArgumentParser()
parser.add_argument( 'username', action='store', help='name of user' )
parser.add_argument( '-c', '--copy', action='store_true', help='copy output to stderr' )
args=parser.parse_args()

password = getpass.getpass('password: ')
hub = Github(args.username,password)
for repo in hub.get_user().get_repos():
    try:
        initial_commit = list(repo.get_commits())[-1]
    except GithubException:
        sys.stderr.write('Exception: %s\n' % repo.name)
        continue
    sha = initial_commit.sha
    url = 'https://github.com/bryanhann/%s' % repo.name
    line = '%s %s\n' % (sha,url)
    sys.stdout.write(line)
    if args.copy:
        sys.stderr.write(line)

