from github import Github, Auth
from datetime import datetime, timedelta
import time
import pytz


class Model:
    def __init__(self, auth_token, repo, time_zone):
        self.auth = Auth.Token(auth_token)
        self.github = Github(auth=self.auth)
        self.repo = self.github.get_repo(repo)
        self.file_path = self.github.get_user().login + ".txt"
        self.time_zone = pytz.timezone(time_zone)

    def exit(self):
        self.github.close()

    def send_message(self, message):
        content = str(time.time()).encode("utf-8")
        try:
            file = self.repo.get_contents(self.file_path)
            self.repo.update_file(file.path, message, content, file.sha)
        except:
            self.repo.create_file(self.file_path, message, content) 

    def get_messages(self):
        pull_cutoff = datetime.now() - timedelta(hours=2)
        commits = self.repo.get_commits(since=pull_cutoff)
        try:
            return [(commit.commit.author.name, commit.commit.author.date.astimezone(self.time_zone).strftime("%H:%M:%S"), commit.commit.message) for commit in commits]
        except:
            return []
