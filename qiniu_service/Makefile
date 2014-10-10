port:=6855

debug:
	./manage.py runserver $(port)

start-uwsgi:
	uwsgi --socket 127.0.0.1:$(port) \
		--chdir $(shell pwd) \
		--wsgi-file qiniu_service/wsgi.py  \
		--master \
		--process 4 \
		--daemonize $(shell pwd)/logs/uwsgi.log \
		--pidfile $(shell pwd)/uwsgi.pid

stop-uwsgi:
	uwsgi --stop uwsgi.pid

reload-uwsgi:
	uwsgi --reload uwsgi.pid
