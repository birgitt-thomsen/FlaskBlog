import json

FILE_PATH = '../data/data.json'

initial_data = [
    {
        "id": 1,
        "author": "John Doe",
        "title": "First Post",
        "content": "This is my first post.",
        "likes": 0
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Second Post",
        "content": "This is another post.",
        "likes": 0
    },
]

try:
    with open(FILE_PATH, "x") as f:  # "x" = create, fail if exists
        json.dump(initial_data, f, indent=4)
except FileExistsError:
    pass  # if file already exists, do nothing