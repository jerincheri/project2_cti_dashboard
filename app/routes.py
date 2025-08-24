from flask import Blueprint, render_template, request
from cti.feeds import query_virustotal, query_abuseipdb
from cti.processor import analyze_ip

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def dashboard():
    result = None
    if request.method == "POST":
        ip = request.form.get("ip")
        vt = query_virustotal(ip)
        abuse = query_abuseipdb(ip)
        result = analyze_ip(ip, vt, abuse)
    return render_template("dashboard.html", result=result)
