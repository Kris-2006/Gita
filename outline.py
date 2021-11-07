import requests

r = requests.get("https://bhagavad-gita.org/Gita/verse-01-01.html")

print(r.history)

"https://bhagavad-gita.org/AudioArchive/Gita/"