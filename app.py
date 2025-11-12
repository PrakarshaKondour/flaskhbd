from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("project(hbd).html")

@app.route("/form")
def home():
    return render_template("form.html")

@app.route("/gallery")
def home():
    return render_template("gallery.html")
if __name__=="__main__":
    app.run(debug==True)

# use of jinja is that use python here     for that put {{}}
# first thing we do is code space then upload the files cssinto static and html to templates and then whererver there is href for css add static/app.css kinda then for html we need to replace with route that is including py {{url_for('projects')}}
#then click on source control button (branch logo) click on commit ,click yes,write a msg then click smalll tick
