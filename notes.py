from flask import Flask, request, g, send_from_directory
import json, os, urllib, atexit
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()
app = Flask(__name__)

def validate(text):
  return \
      text is not None and \
      len(text) > 0 and \
      len(text) < 10000

@app.route("/notes", methods=['GET','POST'])
def notes():
  if request.method == "GET":
    return cache.get('notes')
  if request.method == "POST":
    try:
      data = json.loads(request.data)
      if validate(data['data']):
        cache.set('notes',str(data['data']))
      return data['data']
    except ValueError as e:
      print 'ValueError'
      return 'failed'

def exit_handler():
  file = open('/home/notes/notes.txt','w')
  text = urllib.unquote(cache.get('notes')).decode('utf8') 
  file.write(text)
  file.close()

def main():
  cache.set('notes','cache invalid')
  atexit.register(exit_handler)
  app.run(debug=False)

if __name__ == '__main__':
  main()
