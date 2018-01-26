import os

named_pipe_path='/tmp/http2ws_sock'
webserver_port = int(os.getenv('HTTP2WS_WEBSERVER_PORT') or '5001')
websocket_port = int(os.getenv('HTTP2WS_WEBSOCKET_PORT') or '8765')
websocket_host = os.getenv('HTTP2WS_WEBSOCKET_HOST') or '0.0.0.0'
debug_mode = (os.getenv('DEBUG') is not None) or False
use_ssl = ((os.getenv('HTTP2WS_SSL_CERT') is not None) and (os.getenv('HTTP2WS_SSL_KEY') is not None)) or False
cert_file = str(os.getenv('HTTP2WS_SSL_CERT'))
key_file = str(os.getenv('HTTP2WS_SSL_KEY'))
refresh_rate=0.9


