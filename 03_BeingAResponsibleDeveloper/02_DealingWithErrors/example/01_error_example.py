import sqlite3
from dataclasses import dataclass
from datetime import datetime
from typing import Any, List


@dataclass()
class Blog:
    id: str
    published: datetime
    title: str
    content: str
    public: bool


def blog_list_to_json(item: List[Any]) -> Blog:
    return Blog(id=item[0], published=item[1], title=item[2], content=item[3], public=item[4])


def fetch_blog(blog_id: str) -> Blog:
    # Connect to the database
    con = sqlite3.connect("application.db")
    cur = con.cursor()

    # Execute the query and fetch the data
    cur.execute("SELECT * FROM blogs where id=?", [blog_id])
    result = cur.fetchone()

    # Close the database
    con.close()

    return blog_list_to_json(result)


def main() -> None:
    first_blog = fetch_blog("first-blog")
    private_blog = fetch_blog("private-blog")
    print(first_blog)
    print(private_blog)


if __name__ == "__main__":
    main()
