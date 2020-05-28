import os
import json

import responder
import neologdn


env = os.environ
DEBUG = env['DEBUG'] in ['1', 'True', 'true']

api = responder.API(debug=DEBUG)


@api.route("/")
async def normalize(req, resp):
    body = await req.text
    texts = json.loads(body)
    result = [neologdn.normalize(text) for text in texts]
    resp.media = dict(data=result)


if __name__ == "__main__":
    api.run()