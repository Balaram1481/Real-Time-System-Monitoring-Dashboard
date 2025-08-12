from flask import Flask,render_template,jsonify
import psutil

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/stats')
def stats():
    cpu=psutil.cpu_percent(interval=0.5)
    memory=psutil.virtual_memory().percent
    disk=psutil.disk_usage('/').percent
    net=psutil.net_io_counters()
    network={"sent":net.bytes_sent,"recv":net.bytes_recv}

    return jsonify(cpu=cpu,memory=memory,disk=disk,network=network,net=net)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)