def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	return ["<h1 style='color:wine'>Hello There!</h1>"]