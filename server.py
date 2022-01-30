from flask import Flask, render_template, request, redirect

app = Flask( __name__ )

listContacts = []

@app.route( '/', methods=['GET'])
def despliegaRegistroLogin():
    return render_template( "index.html" )

@app.route( '/result', methods=['GET'])
def displayResult():
    return render_template( "result.html", contacts=listContacts )

@app.route( '/dataContact', methods=['POST'])
def registrarUsuario():
    newContact = {
        "name" : request.form["name"],
        "location" :request.form["location"],
        "language" :request.form["language"],
        "comment" :request.form["comment"]
    }
    listContacts.append( newContact )
    return redirect( '/result' )

@app.route( '/returnMean', methods=['POST'] )
def goBack():
    return redirect( '/' )

if __name__ == "__main__":
    app.run( debug = True )

