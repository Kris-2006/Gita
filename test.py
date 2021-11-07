import methods as m
import json

with open('data/verse.json', 'r', encoding="utf-8") as f:
    d = json.load(f)

    for chapter_id in d:
        if chapter_id['chapter_id'] == 1:
            print(chapter_id)
    print(m)