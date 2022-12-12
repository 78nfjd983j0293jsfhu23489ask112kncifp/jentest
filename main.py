import sys

sys.path.append(".")

from source.DatabaseUtility import *
from flask import Flask,render_template,redirect,request,make_response,url_for
import os
import uuid


app=Flask("main_app",static_folder="static",template_folder="templates")
initDB()



@app.route("/",methods=["GET"])
@app.route('/index',methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if(request.method=="GET"):
        # check if user is logged in
        if(checkLoginState(request)):
            return redirect("/addsamples")

        return render_template("login.html")
    else:

        username,password=request.form.get("username"),request.form.get("password")
        
        user=checkLogin(username,password)
        if(user!=None):
            resp = make_response(redirect("/addsamples"))
            resp.set_cookie('uid', user[0])
            return resp
    return redirect("/login")




@app.route("/register",methods=["GET","POST"])
def register():
    if(request.method=="GET"):
        return render_template("register.html")
    else:
        username,password,badgeID=request.form.get("username"),request.form.get("password"),request.form.get("badgeID")
        addUser(username,badgeID,password)
        return redirect("/")
        


@app.route("/addsamples",methods=["GET","POST"])
def addSamples():
    if(request.method=="GET" and checkLoginState(request)):
        return render_template("upload.html")
    else:
        # provide ID for each and every image uploaded
        dID=str(uuid.uuid4().hex)
        file=request.files.get("file")
        selection=request.form.get("radio_select")
        nameSurname=request.form.get("nameSurname")  

        return redirect(url_for('.checkResults', dID=dID))



@app.route("/checkresults",methods=["GET"])
def checkResults():
    dID=request.args.get("dID")
    result=request.args.get("result")
    return render_template("image.html",image_ID=dID+".png",result=result)

# make gallery for previously uploaded images and their outputs
@app.route("/gallery",methods=["GET"])
def gallery():
    if(checkLoginState(request)):
        return render_template("gallery.html",gallery=make_gallery())
    return redirect("/login")

if __name__=="__main__":
    app.run("0.0.0.0",80)