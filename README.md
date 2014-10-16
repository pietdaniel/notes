# Simple persistent note board for piet.us

An [example](piet.us/note) can be seen [here](piet.us/note)

## But why?

I built this because it's a easy way to transfer small amounts of text to either myself or other individuals over the network. Sometimes I post titles to books or movies, sometimes links to youtube videos, et cetera. There is no built in mechanisms for control so it is a totally free environment. This has caused unexpected yet pleasurable outcomes when notes are left on the board that I did not write.

## Improvements

I was considering doing a similiar project but with HTML5 canvas to allow for doodles. Markdown formatting support would be intersting to implement as well.

## Install

You will need python 2.7 with flask.

To install flask try one of the following:
```
$ pip install flask
$ apt-get install python-flask
$ pacman -S python2-flask
```

Running python notes.py will start an instance on localhost:5000

```
$ python notes.py
* Running on http://127.0.0.1:5000/
```

With nginx this port can be proxy to

```
server {
  ...
  location /notes {
    proxy_pass http://127.0.0.1:5000
  }
}
```

Ensure the index.html and notes.js are in there appropriate directories.

## Usage

The webpage is just a single textarea. Notes are posted on mouse leave, focus out, and a interval of 3000. This may be overkill.

*Enjoy


