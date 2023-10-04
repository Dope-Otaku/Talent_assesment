'''
    this should be implemented in app.py 
    this will be only opened randomly or after completing certain events 
    and will get free resources exclusively
'''

@app.route("/hidden-quest")
def hidden_quest():
  if request.args.get("achievement") == "secret":
    return "You have unlocked the hidden quest!"
  else:
    return "Sorry, you haven't unlocked the hidden quest yet."




'''

    html page:-

<!DOCTYPE html>
<html>
<head>
  <title>Hidden Quest</title>
</head>
<body>
  <h1>Hidden Quest</h1>
  <p>Congratulations! You have unlocked the hidden quest by completing 100 questions.</p>
  <p>To start the quest, click the button below.</p>
  <button onclick="startQuest()">Start Quest</button>
  <script>
    function startQuest() {
      window.location.href = "/hidden-quest";
    }
  </script>
</body>
</html>

'''

