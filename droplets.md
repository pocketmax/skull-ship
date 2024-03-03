## to add a new user

```shell
adduser ubuntu \
--system \
--shell /bin/bash \
--group \
--disabled-password \
--home /home/ubuntu
usermod -aG sudo ubuntu
```

## install node
```shell
curl -fsSL https://deb.nodesource.com/setup_15.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## to login as the user
```shell
su - ubuntu
```

## generate ssh key
```shell
ssh-keygen -q -t rsa -N ''
```

docker run --name db -e MYSQL_ROOT_PASSWORD=secret -v /home/ubuntu/dbdata:/var/lib/mysql
--restart=yes -d mariadb

docker exec -i db sh -c 'exec mysql -uroot -psecret' < ./analytics.sql