# Tasks
0. Double the number of webservers






### Command to uninstall haproxy
1. Stop th HAProxy service: `sudo service haproxy stop`
2. Uninstall HAProxy Package: `sudo apt-get remove --purge haproxy`
3. Remove HAProxy Configuration: `sudo rm -r /etc/haproxy/`
4. Clean Up Dependencies: `sudo apt-get autoremove`
5. Verify Removal: 
```
dpkg -l | grep haproxy
ls /etc/haproxy/
```
If the package is successfully removed, and the configuration directory is no longer present, you have successfully reversed the HAProxy installation.
