# What is this
A dictionary creater/ web scraper to fixup input for other projects

# Data sources
Whatever newline-separated list of words you wish

on Mac, `/etc/dict/words` is pretty good ~235k words
```
cp /usr/share/dict/words macWords.txt
```

on Github, [this guy](https://github.com/dwyl/english-words) made a 466k word list which can be downloaded like
```
curl -L https://github.com/dwyl/english-words/raw/master/words.txt -o words.txt
```


project gutenberg cleaned
  http://www.mso.anu.edu.au/~ralph/OPTED/

wordnet
  https://sourceforge.net/projects/wnsql/files/wnsql3/mysql/3.1/

wordnik API
  https://developer.wordnik.com/gettingstarted


  to look into:
  princeton wordnet dump: https://wordnet.princeton.edu/download
  wikipedia/wikimedia dumps: https://dumps.wikimedia.org/backup-index.html
  some guy's dictionary: https://github.com/adambom/dictionary
  
