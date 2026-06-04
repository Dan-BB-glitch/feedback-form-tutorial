import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime as dt

@anvil.server.callable
def add_feedback(name, email, feedback):
  app_tables.feedback.add_row(
    name = name,
    email = email,
    feedback=feedback,
    created= dt.datetime.now()
  )
