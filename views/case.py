from views import BasicView


class Case(BasicView):
  def post(self):
    with self.db.transaction():
      self.db
