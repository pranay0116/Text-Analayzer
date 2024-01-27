from flask import Flask, render_template, request


app = Flask(__name__)

@app.get("/")
def showPage():
    return render_template('index.html')

@app.post('/analyze')
def analyze():
    text= request.form['text']
    action= request.form['action']
    answer=""
    if (action == "cntchr"):
        #count no of characters
        answer=f"the number of characters are:-{len(text)}"
    if (action=="cntws"):
        #count no of white spaces
        answer=f"the number of white spaces are:-{text.count(' ')}"
    if (action=="cstuc"):
        #convert lc to uc
        answer=f"Convert string into upper case:-{text.upper()}"
    if (action=="cstlc"):
        #convert uc to lc
        answer=f"Convert string into lower case:-{text.lower()}"
    if (action=="cscol"):
        #check string contains only letter or not
        answer=f"string contains only letter:-{text.isalpha()}"
    if (action=="cscod"):
        #check string contain only digit or not
        answer=f"string contains only digit:-{text.isdigit()}"
    if (action=="csalc"):
        #check string is lower case or not
        answer=f"string contains only lower case:-{text.islower()}"
    if (action=="csauc"):
        #check string is upper case or not
        answer=f"string contains only upper case:-{text.isupper()}"
    if (action=="sts"):
        #swapcase
        answer=f"swap the given string:-{text.swapcase()}"
    return render_template('index.html', output= answer)

app.run(debug=True)