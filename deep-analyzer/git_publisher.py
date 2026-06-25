import os
import shutil
import git
from typing import Optional


class GitPublisher:
    def __init__(self, repo_url: str, repo_dir: str):
        self.repo_url = repo_url
        self.repo_dir = repo_dir
        self.repo: Optional[git.Repo] = None

    def ensure_repo(self):
        if os.path.isdir(os.path.join(self.repo_dir, ".git")):
            self.repo = git.Repo(self.repo_dir)
            origin = self.repo.remotes[0]
            origin.pull()
            return
        if os.path.exists(self.repo_dir):
            shutil.rmtree(self.repo_dir)
        os.makedirs(os.path.dirname(self.repo_dir), exist_ok=True)
        self.repo = git.Repo.clone_from(self.repo_url, self.repo_dir)

    def publish(self, source_dir: str, subdir: str, message: str):
        self.ensure_repo()
        target = os.path.join(self.repo_dir, subdir)
        os.makedirs(target, exist_ok=True)
        for fname in os.listdir(source_dir):
            shutil.copy2(os.path.join(source_dir, fname), os.path.join(target, fname))
        if self.repo.is_dirty() or len(self.repo.untracked_files) > 0:
            self.repo.git.add(A=True)
            self.repo.index.commit(message)
            origin = self.repo.remotes[0]
            origin.push()
            print(f"  [OK] Published to GitHub: {message}")
        else:
            print("  [OK] No changes to publish")

    def read_daily_files(self) -> str:
        self.ensure_repo()
        daily_dir = os.path.join(self.repo_dir, "daily")
        if not os.path.isdir(daily_dir):
            return ""
        files = sorted(os.listdir(daily_dir))
        texts = []
        for fname in files:
            fpath = os.path.join(daily_dir, fname)
            if os.path.isfile(fpath):
                with open(fpath, "r", encoding="utf-8") as f:
                    texts.append(f"=== {fname} ===\n{f.read()}")
        return "\n\n".join(texts)
