## setup a user-defined bridge
```shell
docker network create mynet
docker run --name mynode1 --network mynet -d alpine top
docker run --name mynode2 --network mynet -d alpine top
docker run --name mynode3 -d alpine top
docker network connect mynet mynode3
docker exec mynode1 ping mynode2
docker exec mynode2 ping mynode1
docker network disconnect mynet mynode1
```

## to remove a user-defined bridge
```shell
docker network rm mynet
```

## enable packet forwarding to the outside world
```shell
sysctl net.ipv4.conf.all.forwarding=1
sudo iptables -P FORWARD ACCEPT
```

### https://docs.docker.com/network/bridge/#differences-between-user-defined-bridges-and-the-default-bridge
