# ipv6DDNS+cdn
# Development Reasons
- Most computers in China only have a public IPv6 address.
- When using the public IPv6 address provided by ISPs, ports 80 and 443 are blocked.
- If a website is established using a public IPv6 address, it can only be accessed by IPv6-supported devices and with a port number, which is not user-friendly.

# Solution Approach
Domestic CDN platforms support IPv6 + non-standard port back-to-origin. A script can be used to check the server's IPv6 address every 10 seconds, and if there is a change, call the Tencent Cloud Edge One API to update the back-to-origin IPv6 address in real-time. If there is no change, no action is taken.

# What Problem Does This Solve?
Domestic CDN nodes support both IPv4 and IPv6. After using dynamic IPv6 back-to-origin, when accessing a website created by an IPv6 server, devices do not need to have an IPv6 address to access it, and the domain name does not need to carry a port number (more elegant).

# IPv6 Domain Name Acceleration Updater

This Python script is designed to automatically update a set of domain names' IPv6 addresses on the Tencent Cloud TEO platform. It is particularly suitable for environments with dynamic IPv6 addresses, ensuring that the domain name's acceleration service always points to the correct IPv6 address.

## Features

- Retrieve the current IPv6 address of a specified network interface.
- Filter out local link addresses (addresses starting with `fe80`).
- Support for Windows and Unix-like operating systems.
- Update the list of domain names' IPv6 addresses on Tencent Cloud TEO.
- Continuously run, periodically checking for changes in the IPv6 address.

## Limitations
- Only supports Tencent Cloud Edge One as the CDN service provider.
- Requires the server to have a public IPv6 address.
- This code only provides a solution on how to build a website with a dynamic public IPv6 address and can be dynamically modified according to needs.

## System Requirements

To run this script, you need:

- Python 3.x
- Tencent Cloud Python SDK
- A configuration file named `config.conf` containing your Tencent Cloud credentials and domain information.

## Configuration

Create a `config.conf` file in the same directory as the script with the following structure:

```ini
[DEFAULT]
SecretId = YourSecretId
SecretKey = YourSecretKey
ZoneId = YourZoneId
DomainName = YourDomain1,YourDomain2
InterfaceName = YourNetworkInterfaceName
```

Replace `YourSecretId`, `YourSecretKey`, `YourZoneId`, `YourDomain1`, `YourDomain2`, and `YourNetworkInterfaceName` with your actual Tencent Cloud credentials, the zone ID of your domain, the list of domain names you wish to update, and the network interface name.

## Usage

To run the script, simply execute it with Python:

```bash
pip install -r requirements.txt
```

```bash
python ddns+edge one.py
```

The script will start and begin monitoring the specified network interface for changes in the IPv6 address. When a change is detected, it will update the IPv6 address of the domain names listed on Tencent Cloud TEO.

## Logging

The script will output logs directly to the console. It will inform you of the current IPv6 address, any detected changes, and the status of the update requests to Tencent Cloud TEO.

## Disclaimer

This script is not affiliated with Tencent Cloud. Please ensure you have the necessary permissions to use the Tencent Cloud API to manage your domain names.

## License

You are free to use and develop this program code further.
