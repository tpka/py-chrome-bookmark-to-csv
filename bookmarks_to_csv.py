import csv
from datetime import datetime
from bs4 import BeautifulSoup

input_file = "bookmarks_5_6_23.html"
output_file = "bookmarks_5_6_23.csv"

def html_bookmarks_to_csv(input_file, output_file):
    # Load the HTML file into BeautifulSoup
    with open(input_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # Find all <a> tags in the bookmarks bar and extract their URL, title, and add_date attributes
    bookmarks = []
    for a in soup.find_all("a"):
        if "href" in a.attrs and "add_date" in a.attrs:
            title = a.string
            add_date = datetime.fromtimestamp(int(a["add_date"])).strftime("%Y-%m-%d %H:%M:%S")
            url = a["href"]
            bookmarks.append({"title": title, "add_date": add_date, "url": url})

    # Write the bookmarks to a CSV file
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "add_date", "url"])
        writer.writeheader()
        for bookmark in bookmarks:
            writer.writerow(bookmark)

if __name__ == "__main__":
    html_bookmarks_to_csv(input_file, output_file)
