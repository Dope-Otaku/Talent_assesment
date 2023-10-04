'''
    this code submits feedback from users and send it to admin for improvements
'''

@app.route("/feedback")
def feedback():
  return render_template("feedback.html")

@app.route("/submit-feedback")
def submit_feedback():
  feedback = request.form.get("feedback")

  # Save the feedback to the database.
  save_feedback(feedback)

  # Redirect the user to the feedback page.
  return redirect("/feedback")