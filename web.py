from http.server import HTTPServer,BaseHTTPRequestHandler

content= '''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>
<h1>Top 5 Revenue from Companies</h1>
<table border=2>
<tr>
<th> Company Name </th>
<th> Revenue </th>
<th> Financial Year </th>
</tr>

<tr>
<td> Microsoft </td>
<td> 86$ </td>
<td> 2014 </td>
</tr>

<tr>
<td> Oracle </td>
<td> 37$ </td>
<td> 2013 </td>
</tr>

<tr>
<td> SAP </td>
<td> 20$ </td>
<td> 2013 </td>
</tr>

<tr>
<td> VMware </td>
<td> 5.2$ </td>
<td> 2013 </td>
</tr>

<tr>
<td> CA Technologies </td>
<td> 4.7$ </td>
<td> 2013 </td>
</tr>

</body>
</html>
'''

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())


server_address =('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...") 
httpd.serve_forever()
