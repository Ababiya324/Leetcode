import os
import time
import requests

SESSION = os.environ["LEETCODE_SESSION"]
CSRF = os.environ["LEETCODE_CSRF_TOKEN"]
DEST = os.environ.get("DESTINATION_FOLDER", "solutions")

EXT = {
    "python": "py", "python3": "py", "c": "c", "cpp": "cpp",
    "csharp": "cs", "java": "java", "javascript": "js", "typescript": "ts",
    "golang": "go", "rust": "rs", "kotlin": "kt", "swift": "swift",
    "ruby": "rb", "scala": "scala", "php": "php", "racket": "rkt",
    "erlang": "erl", "elixir": "ex", "dart": "dart", "bash": "sh",
    "mysql": "sql", "mssql": "sql", "oraclesql": "sql", "postgresql": "sql",
}

session = requests.Session()
session.cookies.set("LEETCODE_SESSION", SESSION, domain="leetcode.com")
session.cookies.set("csrftoken", CSRF, domain="leetcode.com")
session.headers.update({
    "x-csrftoken": CSRF,
    "Referer": "https://leetcode.com",
    "User-Agent": "Mozilla/5.0",
})


def fetch_submissions():
    offset, limit = 0, 20
    while True:
        url = f"https://leetcode.com/api/submissions/?offset={offset}&limit={limit}"
        for attempt in range(5):
            r = session.get(url, timeout=30)
            if r.status_code in (403, 429):
                wait = 5 * (attempt + 1)
                print(f"rate limited at offset {offset}, waiting {wait}s")
                time.sleep(wait)
                continue
            r.raise_for_status()
            break
        else:
            print(f"giving up at offset {offset} after repeated rate limits")
            return
        data = r.json()
        for sub in data.get("submissions_dump", []):
            yield sub
        if not data.get("has_next"):
            break
        offset += limit
        time.sleep(2)

def main():
    seen = set()
    updated = 0
    for sub in fetch_submissions():
        if sub.get("status_display") != "Accepted":
            continue
        slug = sub["title_slug"]
        if slug in seen:
            continue
        seen.add(slug)

        ext = EXT.get(sub.get("lang", ""), "txt")
        folder = os.path.join(DEST, slug)
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, f"solution.{ext}")
        code = sub.get("code", "")

        existing = None
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                existing = f.read()
        if existing != code:
            with open(path, "w", encoding="utf-8") as f:
                f.write(code)
            updated += 1
            print(f"synced {slug} ({sub.get('lang')})")

    print(f"done: {updated} file(s) updated, {len(seen)} problem(s) seen")


if __name__ == "__main__":
    main()
