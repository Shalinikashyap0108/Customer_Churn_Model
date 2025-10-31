import os


def test_files_exist():
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
required_files = [
"churn_analysis.py",
"app.py",
"requirements.txt",
os.path.join("templates", "index.html")
]
for file in required_files:
assert os.path.exists(os.path.join(repo_root, file)), f"{file} is missing!"
