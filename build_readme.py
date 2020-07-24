# coding:utf-8
import feedparser


def fetch_blog_entries():
    entries = feedparser.parse("http://feed.cnblogs.com/blog/u/556338/rss/")["entries"]
    return [
        {
            "title": entry["title"].split(" - ")[0],
            "url": entry['link'],
            "published": entry["published"].split("T")[0],
        }
        for entry in entries
    ]


if __name__ == '__main__':
    with open('template.md', 'r', encoding='utf-8') as f:
        template = f.read()

    entries = fetch_blog_entries()[:7]
    entries_md = "\n".join(
        ["* <a href='{url}' target='_blank'>{title}</a> - {published}".format(**entry) for entry in entries]
    )
    readme = template.replace("$$RecentBlog$$", entries_md)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
