'''
    from this code the usercan review and analyze  their 
    test results and can work hard on it

'''

@app.route("/analyze-review")
def analyze_review():
  user_id = request.args.get("user_id")
  quiz_id = request.args.get("quiz_id")

  # Get the user's quiz performance data.
  performance_data = get_user_quiz_performance_data(user_id, quiz_id)

  # Analyze the performance data.
  strengths = analyze_strengths(performance_data)
  weaknesses = analyze_weaknesses(performance_data)

  # Render the analysis and review page.
  return render_template("analyze_review.html", strengths=strengths, weaknesses=weaknesses)