### 执行脚本下载来源
从这里下载 http://sourceforge.net/projects/xtables-addons/files/Xtables-addons/ Xtables-addons
下载的版本需要与iptables的版本一致，iptables的版本可以通过下面的命令查看：
```
iptables -V
```

### 执行脚本位置
执行以下解包命令
```shell
xz -d xtables-addons-x.x.tar.xz 
tar -xvf xtables-addons-x.x.tar
```

### 生成文件
进入 xtables-addons-x.x/geoip/ 目录可以看到xt_geoip_build和xt_geoip_dl
xt_geoip_dl 可以用来下载和生成GeoIPCountryWhois.csv文件
```
./xt_geoip_dl
```
xt_geoip_build 用来生成过滤文件
```
./xt_geoip_build GeoLite2-Country-CSV_DIRCTORY
```

### iptables 1.6.x以下兼容脚本
由于openwrt生成1.6.x版本一下的geoip文件，可以用以下办法
1. 通过geo_build_sh包中的geoip_build_cvs.py来生成GeoIPCountryWhois.csv文件
```bash
python geoip_build_cvs.py
```
2. 再用低于1.6.x版的xt_geoip_build来生成ipv4版本, 不过由于旧版不支持ipv6所以生成的iv6文件将是空文件。
```bash
./xt_geoip_build GeoIPCountryWhois.csv
```

### 未验证方法
1. 直接通过geo_build_sh包中的xt_geoip_build脚本来生成，执行命令为：
```sh
./xt_geoip_build -S GeoLite2-Country-CSV-Directory/
```
但这个脚本没有经过完整验证，目前不推荐

### PS

执行时如果遇到 Can't locate Text/CSV_XS.pm in @INC 可以按如下方法解决
```
sudo perl -MCPAN -e 'install Text::CSV_XS'
```

### 安装部署
将目录BE(LE)下生成的*.iv4 *.iv6 文件复制到/usr/share/xt_geoip/BE(LE)/
（高版本的xtables-addons生成的文件有可能不会再区分BE和LE）

以上文件生成完成
