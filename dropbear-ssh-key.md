在OpenWrt中使用ssh的私钥登陆时会遇到下面的错误提示：
```
ssh: Exited: String too long
```
这个问题是由于DropBear SSH使用的SSH Keys的格式不是PEM格式（由ssh-keygen生成），在DropBear中通常是使用dropbearkey来生成
```
dropbearkey -f id_rsa -t rsa -b 2048
```
如果需要转换现有的keys到DropBear格式需要使用dropbearconvert
```
dropbearconvert openssh dropbear ~/.ssh/id_rsa ~/.ssh/id_dropbear
```
