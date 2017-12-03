#!/usr/bin/env python3

from gsmls import get_listing_detail_preview

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "GSMLS"

@app.route("/properties/<int:mlsid>")
def get_property(mlsid):
    return get_listing_detail_preview(mlsid)

if __name__ == "__main__":
    app.run(debug=True)
