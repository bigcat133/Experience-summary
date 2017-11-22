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
