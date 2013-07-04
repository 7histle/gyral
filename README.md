how to launch:
1. install apache2+mod_wsgi
2. install python3
3. in the end of apache2.conf file add a line:
WSGIScriptAlias /gyral /home/username/www/hello.wsgi
4. put hello.wsgi into /home/username/www/
5. type in the address bar of your browser:
http://localhost/gyral
6. enjoy
