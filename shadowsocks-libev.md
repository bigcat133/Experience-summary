## shadowsocks-libev 在ubuntu环境下的安装

### For Ubuntu 14.04 and 16.04
```shell
sudo add-apt-repository ppa:max-c-lv/shadowsocks-libev -y
sudo apt-get update
sudo apt install shadowsocks-libev
```

### 安装后的有效命令为：
```shell
ss-local
ss-redir
ss-server
ss-tunnel
ss-manager
```

### 启动命令一般为：
```
ss-local -c config.conf -b 0.0.0.0
ss-redir -c config.conf -b 0.0.0.0 -u
ss-tunnel -c config.conf -b 0.0.0.0 -l 5353 -u -v
```

### config 配置：
```json
{
"server":["serv ip"],
"server_port":8956,
"local_address":"127.0.0.1",
"local_port":1080,
"password":"password",
"timeout":600,
"method":"aes-256-cfb",
"workers":"2",
"shareOverLan" : true
}
```

### iptables 配置：
```shell
# Create new chain
iptables -t nat -N SHADOWSOCKS
iptables -t mangle -N SHADOWSOCKS

# Ignore your shadowsocks server's addresses
iptables -t nat -A SHADOWSOCKS -d 123.123.123.123 -j RETURN

# Ignore LANs and any other addresses you'd like to bypass the proxy
iptables -t nat -A SHADOWSOCKS -d 0.0.0.0/8 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 10.0.0.0/8 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 127.0.0.0/8 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 169.254.0.0/16 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 172.16.0.0/12 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 192.168.0.0/16 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 224.0.0.0/4 -j RETURN
iptables -t nat -A SHADOWSOCKS -d 240.0.0.0/4 -j RETURN

# Anything else should be redirected to shadowsocks's local port
iptables -t nat -A SHADOWSOCKS -p tcp -j REDIRECT --to-ports 12345

# Add any UDP rules
ip route add local default dev lo table 100
ip rule add fwmark 1 lookup 100
iptables -t mangle -A SHADOWSOCKS -p udp --dport 53 -j TPROXY --on-port 12345 --tproxy-mark 0x01

# Apply the rules
iptables -t nat -A PREROUTING -p tcp -j SHADOWSOCKS
iptables -t mangle -A PREROUTING -j SHADOWSOCKS

# Start the shadowsocks-redir
ss-redir -u -c /etc/config/shadowsocks.json -f /var/run/shadowsocks.pid
```
