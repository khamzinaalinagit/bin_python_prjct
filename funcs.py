import re
import requests

BINARY_IN_TEXT_PATTERN = re.compile(r'\b[01]+\b')
BINARY_FULL_PATTERN = re.compile(r'^[01]+$')


def is_binary_string(s):
    s = s.strip()
    return bool(BINARY_FULL_PATTERN.fullmatch(s))


def find_binaries_in_text(text):
    return BINARY_IN_TEXT_PATTERN.findall(text)


def find_binaries_in_file(path, encoding:str = "utf-8"):
    with open(path, "r", encoding=encoding) as f:
        content = f.read()
    return find_binaries_in_text(content)


def find_binaries_in_url(url, timeout):
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    text = response.text
    return find_binaries_in_text(text)
