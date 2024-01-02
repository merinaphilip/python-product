''' application to display hello world '''
from flask_wtf import CSRFProtect             #fix
from flask import Flask,render_template
import socket
from flask_sslify import SSLify

app = Flask(__name__)
csrf = CSRFProtect(app)                        #fix
sslify = SSLify(app)


@app.route("/sensitive",methods=["GET", "POST"])        #
#@csrf.exempt
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
