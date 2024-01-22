#Steps in setting port forwarding on ufw

1. Allow Traffic to Port 8080(Open port 8080 for incoming traffic):
```
sudo ufw allow 8080
```
2. Enabling IP Forwarding in `/etc/sysctl.conf`
  - Enable IP forwarding to allow the system to forward packets between network interfaces by uncomment the line(`sudo vi /etc/sysctl.conf`) and remove the preceded `#`:
```
net.ipv4.ip_forward=1
```
3. Save the file and apply changes with:
```
sudo sysctl -p
```
4. Set Up NAT (Network Address Translation):
  - Using `iptables` to set up NAT rules for port forwarding with the following command:
```
# forwards traffic from port 8080 to port 80
sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
```
5. Save the iptables rules to make them persistent across reboots:
```
sudo sh -c 'iptables-save > /etc/iptables.rules'
```
6. Configure UFW to Load `IPTABLES Rules`, open the `/etc/ufw/before.rules` file:
```
sudo vi /etc/ufw/before.rules
```
  - Add the following lines at the beginning of the file:
```
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
```
7. Save the file, and reload `UFW` to apply the changes:
```
sudo ufw reload
```

Now, incoming traffic on port 8080 should be redirected to port 80.
