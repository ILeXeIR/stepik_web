#sudo apt-get update
#sudo apt full-upgrade -y python3
#sudo pip3 install --upgrade pip
#sudo pip3 install --upgrade django
#sudo pip3 install --upgrade gunicorn
sudo pip3 install django==2.0

sudo /etc/init.d/mysql start
cd /home/box/web/ask
mysql -uroot -e "create database stepic_web;"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
python3 manage.py makemigrations
python3 manage.py migrate

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#sudo gunicorn -b 0.0.0.0:8080 -w 4 hello:app &
#cd /home/box/web/ask
sudo gunicorn -b 0.0.0.0:8000 -w 4 ask.wsgi:application &

