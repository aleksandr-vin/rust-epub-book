#
# Usage:
#   BOOK_PATH=$(rustup docs --path | sed 's|rust/html/index.html|rust/html/book|')
#   python make-epub.py < "$BOOK_PATH/print.html" > /tmp/the-rust-programming-language-pre-print.html
#   (cd "$BOOK_PATH" && pandoc /tmp/the-rust-programming-language-pre-print.html --to=epub --output="$HOME/Documents/The Rust Programming Language.epub")

import sys
from bs4 import BeautifulSoup

def sanitize(text):
  soup = BeautifulSoup(text, "html.parser")

  # unwrapping for pandoc, creds go to https://dev.to/brthanmathwoag/helping-pandoc-generate-a-correct-table-of-contents-from-html-input-27im
  current = soup.find('main')
  while current.name != 'body':
    parent = current.parent
    current.unwrap()
    current = parent

  # Following this hack: https://github.com/rust-lang/rust/issues/20866#issuecomment-495962961
  for e in [i for r in [
      soup.find_all(id="sidebar"),
      soup.find_all(id="menu-bar"),
      soup.find_all(id="sections"),
      soup.find_all("script"),
      soup.select("div.buttons"),
      soup.select("img.ferris")
    ] if r != None for i in r]:
    print(f"removing {e.name} element", file=sys.stderr)
    e.extract()

  return soup.prettify()

print(sanitize(sys.stdin.read()))
