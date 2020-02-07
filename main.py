from wtforms import Form, StringField, validators
from flask import Flask, render_template, request


import math
import operator

class InputForm(Form):
    r = StringField(validators=[validators.InputRequired()])

def compute(r):
    D = 1 + 8 * len(r)
    root = math.sqrt(D)
    if D != int(root + 0.5) ** 2 or root % 2 == 0 or root == 1:
        return False
    counts = {}
    for ch in r:
        if ch in counts:
            counts[ch] += 1
        else :
            counts[ch] = 1
    sorted_counts = sorted(counts.items(), key=operator.itemgetter(1))
    for index in range(1,len(sorted_counts)):
        if sorted_counts[index][1] != index +1 :
            return False
    return True




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    print request.method
    print form.r.data
    if request.method == 'POST' and form.validate():
        r = form.r.data
        s = compute(r)
    else:
        s = None
    print s
    return render_template("view.html", form=form, s=s)


if __name__ == '__main__':
    app.run(debug=True)