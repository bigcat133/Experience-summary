### 安装 opkg
准备一个小u盘，格式化成ext3或ext4
执行：
```shell
entware-setup.sh
```
并按提示选择u盘安装
如果提示安装失败可以重启路由后再试

完成后执行进行更新
```shell
opkg update
opkg upgrade
```

### 安装 shadowsocks-libev
可以用一下命令查找要安装的列表
```shell
opkg list|grep shadowsocks
```
列出后一一安装即可

### dnsmasq-full 的问题
目前华硕的固件内存消耗很大如果使用opkg中的dnsmasq-full会导致内存耗尽
得要想其他的办法
另外merlin自带的dnsmasq配置是在jffs中修改
可以在jffs中增加配置文件
/jffs/configs/dnsmasq.conf.add

### ipset and iptables
目前如果要执行下面的ipset命令：
```shell
ipset -N gfwlist iphash iptables -t nat -A PREROUTING -p tcp -m set --match-set gfwlist dst -j REDIRECT --to-port 1080
```
需要加载内核模块 xt_set：
```shell
modprobe xt_set
```
作者说在382.2版本会默认加载这个内核模块


### ip地址归属检查
可以通过该命令得到中国地区ip地址的集合
```shell
wget -o http://www.ipdeny.com/ipblocks/data/countries/cn.zone
```

### iptables 设置 geoip 的脚本
```shell
#!/bin/sh

SS_SERVER_IP=118.184.29.180
REDIR_PORT=1080
NO_REDIR="$SS_SERVER_IP 10.0.0.0/8 10.42.0.0/16 127.0.0.0/8 169.254.0.0/16 172.16.0.0/12 192.168.0.0/16"

start() {
    # geoip && TPROXY module
    echo "loading modules"
    ( lsmod | grep xt_geoip ) || insmod xt_geoip
    ( lsmod | grep TPROXY ) || insmod xt_TPROXY

    echo "setup tcp redir"
    iptables -N SS -t nat
    iptables -F SS -t nat
    for n in $NO_REDIR;do
        iptables -t nat -A SS -d $n -j RETURN
    done

    iptables -t nat -A SS -p tcp -m geoip ! --destination-country CN -j REDIRECT --to-ports $REDIR_PORT
    iptables -t nat -A PREROUTING -j SS

    echo "setup udp redir"
    ip rule add fwmark 0x01/0x01 table 100
    ip route add local 0.0.0.0/0 dev lo table 100

    iptables -t mangle -N SS
    iptables -t mangle -F SS
    for n in $NO_REDIR;do
        iptables -t mangle -A SS -d $n -j RETURN
    done

    iptables -t mangle -A SS -p udp  -m geoip ! --destination-country CN -j TPROXY --on-port $REDIR_PORT --tproxy-mark 0x01/0x01
    iptables -t mangle -A PREROUTING -j SS
    echo "done"
}


del_in_table() {
    iptables -t $1 -D PREROUTING -j SS
    iptables -t $1 -F SS
    iptables -t $1 -X SS
}

stop() {
    del_in_table nat
    del_in_table mangle
}


ACTION=$1
case $ACTION in
    start)
        start
        ;;
    stop | kill )
        stop
        ;;
    *)
        echo -e "Usage: (start|stop|kill)"
        exit 1
        ;;
esac
```
