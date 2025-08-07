from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def login():
    result_message=""
    if request.method=="POST":
        try:
            uname=request.form.get("username")
            pasword=request.form.get("password")
            if uname=="admin" and pasword=="admin":
                print(f"login Successfully {uname}")
                result_message=f"Login Successfully {uname}"
            else:
                print("Not a valid user")
                result_message="Not a valid user"
        except Exception as e:
            print(f"invalid formate: {e}")
            result_message=f"Invalid format: {e}"
    return render_template("index.html",result_message=result_message)
if __name__=="__main__":
    app.run(debug=True)


