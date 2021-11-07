from flask import Flask

from methods import *

app = Flask("myapp")


@app.route('/')
def show():
    return "replae number\n" \
           "For List Go Here :-------> <a href ='/api/chapters'>here</a> \n" \
           "For Verses In A Chapters:-------> <a href ='/api/chapters/number/verses'>here</a>'\n" \
           " For a Specified Chapters :-----------> <a href = '/api/chapters/number'>here</a>\n" \
           "For a Specified Verse :----------> <a href ='/api/chapter/n/verse/num'>here</a> \n" \
           ""


@app.route('/api/chapters/')  # all haps
def chapters():
    with open('data/chapters.json', 'r', encoding="utf-8") as f:
        response = json.load(f)
        return jsonify(response)


@app.route('/api/chapters/<int:number>')  # get hap
def chaptersbyno(number):
    with open('data/chapters.json', 'r', encoding="utf-8") as f:
        d = json.load(f)
        hap = d[number - 1]
        return jsonify(hap)


@app.route('/api/chapters/<int:n>/verses')  # all verses in hap
def versesofchap(n):
    with open('data/verse.json', 'r', encoding="utf-8") as f:
        d = json.load(f)
        hapverse = []
        for chapter_id in d:
            if chapter_id['chapter_id'] == n:
                hapverse.append(chapter_id)
        return jsonify(hapverse)


@app.route('/api/chapter/<int:n>/verse/<int:num>')  # part verse
def verseby(n, num):
    with open('data/verse.json', 'r', encoding="utf-8") as f:
        d = json.load(f)
    for chapter_id in d:
        if chapter_id['chapter_id'] == n:
            if chapter_id['verse_number'] == num:
                return jsonify(chapter_id)


@app.route('/api/audio/<string:lang>/chapter/<int:n>/verse/<int:num>')  # audio of verse
def verseaudio(lang, n, num):
    langs = ['Sanskrit', 'Hindi', 'Bengali', 'English', 'Dutch', 'German', 'Greek', 'Chinese', 'Japanese', 'French',
             'Spanish', 'Italian', 'Portuguese', 'Hebrew', 'Arabic', 'Serbian', 'Russian']
    base_url = 'https://bhagavad-gita.org/AudioArchive/Gita/'
    if lang in langs:
        if n & num < 10:
            request_url = base_url + lang + '/verses/' + f'0{n}-0{num}.mp3'
            return jsonify(request_url)
        elif n & num >= 10:
            request_url = base_url + lang + '/verses/' + f'{n}-{num}.mp3'
            return jsonify(request_url)
        elif num > 10:
            request_url = base_url + lang + '/verses/' + f'0{n}-{num}.mp3'
            return jsonify(request_url)
        elif n >10 :
            request_url = base_url + lang + '/verses/' + f'{n}-0{num}.mp3'
            return jsonify(request_url)
        else:
            return f"Your Chapter is out of INdex"
    else:
        return f'We ''Do Not Have Ur Looking for '"" \
               f"List of Languages:{langs} "


if __name__ == '__main__':
    app.debug = True
    app.run()  # go to http://localhost:5000/ to view the page.
