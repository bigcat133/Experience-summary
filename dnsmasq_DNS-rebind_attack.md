如果一个域名解析为私有ip段的地址，那么就会在日志出现下面的内容
```
possible DNS-rebind attack detected: mydomain.com
```
这里mydomain.com是解析的域名

在这里可以看到dnsmasq为了防止前向DNS解析到错误的私有地址做的安全设置
```url
https://www.netgate.com/docs/pfsense/dns/dns-rebinding-protections.html
```

解决这个问题的方法是添加以下配置声明相关域名可以rebind
```
rebind-domain-ok=/mydomain.com/
```
