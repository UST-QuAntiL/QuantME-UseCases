from quart import Quart
import asyncio
import sys

app = Quart(__name__)
app.config["DEBUG"] = False
loop = asyncio.get_event_loop()


def generate_url(url_root, route, file_name):
    return url_root + '/static/' + route + '/' + file_name + '.txt'


@app.route('/')
async def index():
    return 'QHana Data Preparation Microservice'


if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
        loop.run_until_complete(app.run_task(host="0.0.0.0", port=port))
    except Exception as ex:
        print("Usage: {} <port>".format(sys.argv[0]))
        exit()
