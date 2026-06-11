import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def add_feedback(name, email, feedback):
  app_tables.feedback.add_row(
    name = name,
    email = email,
    feedback = feedback,
    created= datetime.now()
  )
  anvil.email.send(to="boyeded5@hwbcymru.net",
                   subject=f"Feedback from {name}",
                   text = f"""
                   A new person has filled out the form.

                   Name: {name}
                   Email Address: {email}
                   Feedback: {feedback}
                  """)
