从这里下载 http://sourceforge.net/projects/xtables-addons/files/Xtables-addons/ Xtables-addons
下载的版本需要与iptables的版本一致，iptables的版本可以通过下面的命令查看：
```
iptables -V
```

```
./configure
make
```
进入 geoip可以看到xt_geoip_build和xt_geoip_dl
xt_geoip_dl 可以用来下载和生成GeoIPCountryWhois.csv文件
```
./xt_geoip_dl
```
如果不能正常下载的话可以从这里下载最新的GeoLite2-Country-CSV包，然后通过geo_build_sh包中的geoip_build_cvs.py来生成
https://dev.maxmind.com/geoip/legacy/geolite/

xt_geoip_build 用来生成过滤文件
```
./xt_geoip_build GeoIPCountryWhois.csv
```

执行时如果遇到 Can't locate Text/CSV_XS.pm in @INC 可以按如下方法解决
```
sudo perl -MCPAN -e 'install Text::CSV_XS'
```

将目录BE(LE)下生成的*.iv4 *.iv6 文件复制到/usr/share/xt_geoip/BE(LE)/
（高版本的xtables-addons生成的文件有可能不会再区分BE和LE）

以上文件生成完成
