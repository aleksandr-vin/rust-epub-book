# Compiling epub format of The Rust Programming Language book

## Setup

```shell
python3 -m venv .venv
. .venv/bin/activate
pip install --require-virtualenv -r requirements.txt
```

Plus you need to have a `rustup` installed

## Compile the EPUB format

```shell
BOOK_PATH=$(rustup docs --path | sed 's|rust/html/index.html|rust/html/book|')
python make-epub.py < "$BOOK_PATH/print.html" > /tmp/the-rust-programming-language-pre-print.html
(cd "$BOOK_PATH" && pandoc /tmp/the-rust-programming-language-pre-print.html --to=epub --output="$HOME/Documents/The Rust Programming Language.epub")
```
