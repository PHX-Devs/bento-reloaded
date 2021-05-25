# install goodies
dnf update -y
dnf install -y python3-sqlalchemy python36 python3-flask nginx python3-devel python3-requests
dnf install -y gcc
pip3 install uwsgi
pip3 install migra[pg]
pip3 install flask-restful

dnf install -y python38
pip3.8 install fastapi
pip3.8 install hypercorn
pip3.8 install sqlalchemy
pip3.8 install psycopg2-binary
pip3.8 install jinja2

dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
dnf -qy module disable postgresql
dnf install -y postgresql13-server
dnf install -y epel-release
dnf install -y postgis30_13 --enablerepo=powertools