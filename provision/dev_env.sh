# log dir
sudo mkdir -p /var/log/uwsgi
sudo chown -R nginx:nginx /var/log/uwsgi
sudo mkdir -p /var/log/bento
sudo chown -R nginx:nginx /var/log/bento

# for dev environments!
# be responsible, please oh please don't deploy to prod with these options
usermod -a -G vagrant nginx
setenforce 0
systemctl stop firewalld
systemctl disable firewalld