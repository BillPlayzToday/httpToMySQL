import mysql.connector
import flask
import jsonpickle


def json(object):
    return jsonpickle.encode(object)


app = flask.Flask(__name__)
# Basic Functions
@app.route("/query",methods = ["POST"])
def onRequestQuery():
    currentRequest = flask.request
    requestBody = currentRequest.get_json()
    details = requestBody["Details"]
    
    mysqlConnection = mysql.connector.connect(
        user = details["Username"],
        password = details["Password"],
        host = details["Host"],
        port = details["Port"],
        database = requestBody["Database"]
    )

    mysqlCursor = mysqlConnection.cursor()
    mysqlCursor.execute(requestBody["Query"])

    queryReturn = mysqlCursor.fetchall()

    mysqlConnection.close()

    return json(queryReturn)
# Create Functions
@app.route("/create/database",methods = ["POST"])
def onRequestCreateDatabase():
    currentRequest = flask.request
    requestBody = currentRequest.get_json()
    details = requestBody["Details"]
    
    mysqlConnection = mysql.connector.connect(
        user = details["Username"],
        password = details["Password"],
        host = details["Host"],
        port = details["Port"]
    )

    mysqlCursor = mysqlConnection.cursor(raw = True)
    mysqlCursor.execute("CREATE DATABASE " + requestBody["Database"])

    mysqlConnection.close()

    return "OK"

@app.route("/create/table",methods = ["POST"])
def onRequestCreateTable():
    currentRequest = flask.request
    requestBody = currentRequest.get_json()
    details = requestBody["Details"]
    
    mysqlConnection = mysql.connector.connect(
        user = details["Username"],
        password = details["Password"],
        host = details["Host"],
        port = details["Port"],
        database = requestBody["Database"]
    )

    mysqlCursor = mysqlConnection.cursor(raw = True)
    mysqlCursor.execute("CREATE TABLE " + requestBody["Table"] + "(V TEXT)")

    mysqlConnection.close()

    return "OK"
# Delete Functions
@app.route("/delete/table",methods = ["POST"])
def onRequestDelete():
    currentRequest = flask.request
    requestBody = currentRequest.get_json()
    details = requestBody["Details"]
    
    mysqlConnection = mysql.connector.connect(
        user = details["Username"],
        password = details["Password"],
        host = details["Host"],
        port = details["Port"],
        database = requestBody["Database"]
    )

    mysqlCursor = mysqlConnection.cursor(raw = True)
    mysqlCursor.execute("DROP TABLE " + requestBody["Table"])

    mysqlConnection.close()

    return "OK"
# Check Functions
@app.route("/check/database",methods = ["POST"])
def onRequestCheckDatabase():
    currentRequest = flask.request
    requestBody = currentRequest.get_json()
    details = requestBody["Details"]
    
    mysqlConnection = mysql.connector.connect(
        user = details["Username"],
        password = details["Password"],
        host = details["Host"],
        port = details["Port"]
    )

    mysqlCursor = mysqlConnection.cursor()
    mysqlCursor.execute("SHOW DATABASES")

    queryReturn = str(any((x[0] == requestBody["Database"]) for x in mysqlCursor.fetchall()))

    mysqlConnection.close()

    return json(queryReturn)

@app.route("/check/table",methods = ["POST"])
def onRequestCheckTable():
    currentRequest = flask.request
    requestBody = currentRequest.get_json()
    details = requestBody["Details"]
    
    mysqlConnection = mysql.connector.connect(
        user = details["Username"],
        password = details["Password"],
        host = details["Host"],
        port = details["Port"],
        database = requestBody["Database"]
    )

    mysqlCursor = mysqlConnection.cursor()
    mysqlCursor.execute("SHOW TABLES")

    queryReturn = str(any((x[0] == requestBody["Table"]) for x in mysqlCursor.fetchall()))

    mysqlConnection.close()

    return json(queryReturn)
# Get Functions
@app.route("/get/table",methods = ["POST"])
def onRequestGetTable():
    currentRequest = flask.request
    requestBody = currentRequest.get_json()
    details = requestBody["Details"]

    mysqlConnection = mysql.connector.connect(
        user = details["Username"],
        password = details["Password"],
        host = details["Host"],
        port = details["Port"],
        database = requestBody["Database"]
    )

    mysqlCursor = mysqlConnection.cursor(dictionary = True)
    mysqlCursor.execute("SELECT * FROM " + requestBody["Table"])

    queryReturn = mysqlCursor.fetchall()

    mysqlConnection.close()

    return json(queryReturn)