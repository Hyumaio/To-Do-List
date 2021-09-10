from flask.views import MethodView
from sqlalchemy.engine import Engine

from app import app


class BasicView(MethodView):
  @property
  def db(self) -> Engine:
    return app.config['postgres']

  @property
  def db(self) -> Engine:
    return app.config['postgres']
