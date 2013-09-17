**how to launch**:
- 1. install apache2+mod_wsgi (for debian install a package libapache2-mod-wsgi-py3)
- 2. install python3 and python-webob
- 3. install jinja2 (for debian install a package python3-jinja2)
- 4. in the end of apache2.conf file add a line:  
WSGIScriptAlias /gyral /home/username/www/index.wsgi
- 5. put index.wsgi into /home/username/www/
- 6. type in the address bar of your browser:  
http://localhost/gyral
- 7. enjoy
