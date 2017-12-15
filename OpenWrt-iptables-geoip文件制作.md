从这里下载 http://sourceforge.net/projects/xtables-addons/files/Xtables-addons/ Xtables-addons

```
./configure
make
```
进入 geoip
```
./xt_geoip_dl
./xt_geoip_build GeoIPCountryWhois.csv
```

如果遇到 Can't locate Text/CSV_XS.pm in @INC 可以按如下方法解决
```
sudo perl -MCPAN -e 'install Text::CSV_XS'
```

将目录BE(LE)下生成的*.iv4 *.iv6 文件复制到/usr/share/xt_geoip/BE(LE)/

以上文件生成完成
