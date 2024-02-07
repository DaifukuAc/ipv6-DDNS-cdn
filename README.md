# ipv6DDNS+cdn
# 开发原因
- 国内大部分电脑仅拥有公网ipv6地址
- 使用运营商提供的公网ipv6地址时，80与443端口被屏蔽
- 如果使用公网ipv6地址建立网站时，仅能通过支持ipv6的设备并且带端口号才能访问网站（非常不优雅）
# 解决思路
国内的cdn平台支持ipv6+非标准端口回源，可以使用一个脚本每隔10s检测服务器的ipv6地址，如果发生变化，则调用腾讯云edge one的api实时更新回源的ipv6地址，若未发生变化则不做任何处理。
# 解决了什么问题？
国内cdn节点支持ipv4和ipv6，使用ipv6动态回源之后，访问由ipv6服务器创建的网站时，设备无需拥有ipv6地址即可访问，且访问域名无需携带端口号（更加优雅）
# IPv6 域名加速更新器

此 Python 脚本旨在自动更新腾讯云 TEO 平台上一组域名的 IPv6 地址。它特别适用于具有动态 IPv6 地址的环境，确保域名的加速服务始终指向正确的 IPv6 地址。

## 功能

- 检索指定网络接口的当前 IPv6 地址。
- 过滤掉本地链接地址（以 `fe80` 开头的地址）。
- 支持 Windows 和类 Unix 操作系统。
- 在腾讯云 TEO 上更新域名列表的 IPv6 地址。
- 持续运行，定期检查 IPv6 地址变化。

## 限制
- 仅支持腾讯云edge one作为cdn服务商
- 需要服务器拥有公网ipv6地址

## 系统要求

要运行此脚本，您需要：

- Python 3.x
- 腾讯云 Python SDK
- 一个名为 `config.conf` 的配置文件，其中包含您的腾讯云凭证和域名信息。

## 配置

在脚本相同目录下创建一个 `config.conf` 文件，结构如下：

```ini
[DEFAULT]
SecretId = 您的SecretId
SecretKey = 您的SecretKey
ZoneId = 您的ZoneId
DomainName = 您的域名1,您的域名2
InterfaceName = 您的网络接口名称
```

将 `您的SecretId`、`您的SecretKey`、`您的ZoneId`、`您的域名1`、`您的域名2` 和 `您的网络接口名称` 替换为您实际的腾讯云凭证、域名的区域 ID、您希望更新的域名列表和网络接口名称。

## 使用方法

要运行脚本，只需用 Python 执行它：

```bash
python ddns+edge one.py
```

脚本将启动并开始监控指定的网络接口以检测 IPv6 地址的变化。当检测到变化时，它将更新腾讯云 TEO 上列出的域名的 IPv6 地址。

## 日志记录

脚本将直接将日志输出到控制台。它将通知您当前的 IPv6 地址、检测到的任何变化以及向腾讯云 TEO 更新请求的状态。


## 免责声明

此脚本与腾讯云无关。请确保您有必要的权限使用腾讯云 API 来管理您的域名。

# 使用协议

可自由使用且二次开发此程序代码
