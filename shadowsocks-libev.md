## shadowsocks-libev 在ubuntu环境下的安装

### For Ubuntu 14.04 and 16.04
```shell
sudo add-apt-repository ppa:max-c-lv/shadowsocks-libev -y
sudo apt-get update
sudo apt install shadowsocks-libev
```

安装后的有效命令为：
```shell
ss-local
ss-redir
ss-server
ss-tunnel
ss-manager
```

启动命令一般为：
```
ss-local -c config.conf -b 0.0.0.0
ss-redir -c config.conf -b 0.0.0.0 -u
ss-tunnel -c config.conf -b 0.0.0.0 -l 5353 -u -v
```

config 配置：
```json
{
"server":["serv ip"],
"server_port":serv port,
"local_address":"127.0.0.1",
"local_port":1080,
"password":"password",
"timeout":600,
"method":"aes-256-cfb",
"workers":"2",
"shareOverLan" : true
}
```
