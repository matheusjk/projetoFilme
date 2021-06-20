# from app import api
#
# if __name__ == "__main__":
#     api.run(host='192.168.0.7', port=58000, debug=True)
from gevent.pywsgi import WSGIServer
from app import api

http_server = WSGIServer(('192.168.0.8', 5000), api)
http_server.serve_forever()
