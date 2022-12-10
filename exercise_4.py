from flask import Flask, request

app = Flask(__name__)

HTML_START = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Gra w zgadywanie liczb 3</title>
</head>
<body>
Pick a random number in range 1 to 1000 and I will guess it in max. 10 attempts.<br>
<form action="/guessing" method="POST">
<input type="hidden" name="min" value="{}"></input>
<input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="ok">
</form>
</body>
</html>
"""

HTML_MAIN = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Gra w zgadywanie liczb 3</title>
</head>
<body>
<form action="/guessing" method="POST">
My guess is:<br>
<p> {guess} </p><br>
<input type="hidden" name="min" value="{min}">
<input type="hidden" name="max" value="{max}">
<input type="hidden" name="guess" value="{guess}">
<input name="feedback" type="submit" value="Too big"></input>
<input name="feedback" type="submit" value="Too small"></input>
<input name="feedback" type="submit" value="You win"></input>
</form>
</body>
</html>
"""

HTML_END = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>Hurray! I have guessed! Your number is {guess}</h1>

</body>
</html>
"""


@app.route("/guessing", methods=['GET', 'POST'])
def guessing_game():
    """
    This function is an algorhythm which uses users answers to find a number in range (1, 1000) imagined
    by the user.
    :param: string
    """

    if request.method == 'GET':
        return HTML_START.format(0, 1000)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        feedback = request.form.get("feedback")
        guess = int(request.form.get("guess", 500))

        if feedback == "Too big":
            max_number = guess
        if feedback == "Too small":
            min_number = guess
        if feedback == "You win":
            return HTML_END.format(guess=guess)

        guess = (max_number - min_number) // 2 + min_number
        return HTML_MAIN.format(guess=guess, min=min_number, max=max_number)


if __name__ == '__main__':
    app.run(debug=True)
