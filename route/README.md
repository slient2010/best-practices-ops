# Route

## custom policy routing table

## iptables

```bash
iptables -t nat -A POSTROUTING -s 192.168.100.0/24 -o wg0 -j MASQUERADE
# for debug, to_tg is just a label
iptables -A PREROUTING -t mangle -i eth0 -s 192.168.100.0/24 -j LOG --log-prefix='[to_tg] '
```

```bash
vim /etc/iproute2/rt_tables
```

add one line below.

```text
100     sz
```

```bash
ip route list table sz 
# or
ip route list table 100
ip route add 0/0 via 10.0.0.10 dev wg0 table 100

# DNS
ip rule add to 8.8.0.0/16 table 100
ip rule add to 91.108.0.0/16 table 100

# debug
ip rule list
```

[https://medium.com/@marthin.pasaribu_72336/linux-policy-routing-introduction-37933f8cb62e](https://medium.com/@marthin.pasaribu_72336/linux-policy-routing-introduction-37933f8cb62e) 

## how_to_get_ip.txt

The way to find all the IP addresses associated with a URL is first to find the AS Number, you can get it in http://networktools.nl/asinfo/ For YouTube get it in http://networktools.nl/asinfo/youtube.com There you get the AS Number

Primary ASN : 15169

Now, type in terminal

whois -h whois.radb.net -- '-i origin AS15169' | grep ^route

And there you will get all the IP Addresses, the list is long but you can find similar addresses that can be grouped in a subnet.

