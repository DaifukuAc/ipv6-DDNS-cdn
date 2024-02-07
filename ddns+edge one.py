import time
import json
import configparser
import socket
import os
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.teo.v20220901 import teo_client, models

def get_ipv6_address(interface_name):
    # 获取所有网络接口的地址信息
    addr_info = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET6)
    # 过滤出指定接口的IPv6地址
    for addr in addr_info:
        if addr[4][0].startswith('fe80'):
            # 忽略本地链接地址
            continue
        # 检查地址是否属于指定的接口
        if os.name == 'nt':  # Windows
            # 在Windows上，我们无法直接通过接口名来过滤
            return addr[4][0]
        else:  # Unix-like
            # 在Unix-like系统上，我们可以通过接口名来过滤
            if interface_name == addr[4][-1]:
                return addr[4][0]
    return None

def modify_acceleration_domain(ipv6_address, secret_id, secret_key, zone_id, domain_names):
    cred = credential.Credential(secret_id, secret_key)
    httpProfile = HttpProfile()
    httpProfile.endpoint = "teo.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = teo_client.TeoClient(cred, "", clientProfile)

    for domain_name in domain_names:
        try:
            req = models.ModifyAccelerationDomainRequest()
            params = {
                "ZoneId": zone_id,
                "DomainName": domain_name,
                "OriginInfo": {
                    "OriginType": "IP_DOMAIN",
                    "Origin": ipv6_address
                }
            }
            req.from_json_string(json.dumps(params))

            resp = client.ModifyAccelerationDomain(req)
            print(f"Modified the IPv6 address of domain {domain_name} to {ipv6_address}. Response: {resp.to_json_string()}")
        except Exception as e:
            print(f"Failed to modify the IPv6 address for domain {domain_name}. Error: {e}")

def main():
    config = configparser.ConfigParser()
    config.read('config.conf', encoding='utf-8')
    secret_id = config.get('DEFAULT', 'SecretId')
    secret_key = config.get('DEFAULT', 'SecretKey')
    zone_id = config.get('DEFAULT', 'ZoneId')
    domain_names = config.get('DEFAULT', 'DomainName').split(',')
    interface_name = config.get('DEFAULT', 'InterfaceName')  # 添加这一行

    print(f"Starting the program with the following configuration: SecretId={secret_id}, ZoneId={zone_id}, DomainNames={domain_names}, InterfaceName={interface_name}")  # 修改这一行

    last_ipv6_address = "::1"  # Initialize to an unlikely IPv6 address
    print(f"Initial IPv6 address: {last_ipv6_address}")

    while True:
        current_ipv6_address = get_ipv6_address(interface_name)  # 修改这一行
        if current_ipv6_address != last_ipv6_address:
            print(f"IPv6 address changed from {last_ipv6_address} to {current_ipv6_address}")
            modify_acceleration_domain(current_ipv6_address, secret_id, secret_key, zone_id, domain_names)
            last_ipv6_address = current_ipv6_address
        time.sleep(10)

if __name__ == "__main__":
    main()