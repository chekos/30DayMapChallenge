# Using gh cli automatically create 30 issues one for each day

import subprocess
import pandas as pd
from rich import print

days = pd.read_csv("30_day_map_challenge_2021.csv")

for idx, row in days[["Theme", "Details"]].iterrows():
    _theme = row["Theme"]
    _details = row["Details"]
    _command = [
        "gh",
        "issue",
        "create",
        "--title",
        f"{_theme}",
        "--body",
        f"{_details}",
        "--assignee",
        "chekos",
        "--project",
        '"30 day map challenge (2021)"',
    ]
    print(f"Running issue for {_theme}")
    subprocess.run(_command)
