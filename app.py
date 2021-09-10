from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)


def create_db(debug):
  echo = False
  if debug:
    echo = True
  app.config['postgres'] = create_engine('postgres://postgres:123456@localhost:5433/todolist',
                                         echo=echo)


create_db(debug=True)

if __name__ == '__main__':
  app.run(debug=True)
