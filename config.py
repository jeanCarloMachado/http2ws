import os
named_pipe_path='/tmp/http2ws_sock'
webserver_port = int(os.getenv('HTTP2WS_WEBSERVER_PORT') or '5000')
websocket_port = int(os.getenv('HTTP2WS_WEBSOCKET_PORT') or '8765')
