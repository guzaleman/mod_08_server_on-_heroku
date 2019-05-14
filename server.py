from bottle import route, run, static_file, view
from datetime import datetime as dt
from random import random
import os

@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static")


@route("/")
@view("index")
def index():
    pass
  # now = dt.now()
  # x = random()
  # prophecies=['qwe', 'asd', 'zxc']
  # return {
  #   "date": f"{now.year}-{now.month}-{now.day}",
  #   "predictions": prophecies,
  #   "special_date": x > 0.5,
  #   "x": x,
  # }

###
# run(host="localhost", port=8080)
if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)