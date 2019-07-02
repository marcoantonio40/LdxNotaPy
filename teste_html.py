#!/usr/bin/python
import cgi

# obtem referencia as variaveis passadas pelo cliente
fields = cgi.FieldStorage()

# cabecalho que informa o browser para renderizar como HTML
print("Content-Type: text/html\n\n")

nome = fields.getvalue('nome')
print("<strong>Hello, %s!</strong>" % (nome))
