import requests

from flask import Flask, render_template

app = Flask(__name__)


def get_info(url):
    try:
        info = requests.get(url,
                            headers={'Metadata-Flavor': 'Google'}).text
        return info
    except:
        return "XXX"


@app.route("/")
def index():
    try:
        id = get_info("http://metadata/computeMetadata/v1/instance/id")
        name = get_info("http://metadata/computeMetadata/v1/instance/name")
        zone = get_info("http://metadata/computeMetadata/v1/instance/zone")
        hostname = get_info("http://metadata/computeMetadata/v1/instance/hostname")
        machine = get_info("http://metadata/computeMetadata/v1/instance/machine-type")
        image = get_info("http://metadata/computeMetadata/v1/instance/image")

        return render_template('index.html',
                               infos={'id': id,
                                      'zone': zone,
                                      'hostname': hostname,
                                      'machine': machine,
                                      'image': image
                                      })
    except Exception as e:
        return render_template('error.html', error=e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
