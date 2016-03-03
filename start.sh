description "Gunicorn application server running myproject"

#start on runlevel [2345]
#stop on runlevel [!2345]

#respawn
#ssetuid user
#setgid www-data

env PATH=/Users/anyemi/devhud/current/nsawam/venv/bin

cd /Users/anyemi/devhud/current/nsawam

source /Users/anyemi/devhud/current/nsawam/venv/bin/activate

gunicorn --workers 3 --bind unix:nsawam.sock -m 007 wsgi
