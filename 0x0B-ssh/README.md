# Tasks
## 0. Use a private key
Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

Requirements:

- Only use `ssh` single-character flags
- You cannot use `-l`
- You do not need to handle the case of a private key protected by a passphrase
```
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
sylvain@ubuntu$ 
```

error encounterred for task [100-puppet_ssh_config.pp](100-puppet_ssh_config.pp)
```
Error: Evaluation Error: Error while evaluating a Resource Statement, Unknown resource type: 'file_line' (file: /root/alx-system_engineering-devops/0x0B-ssh/100-puppet_ssh_config.pp, line: 3, column: 1) on node 6b7b64ccb24f.ec2.internal
```
Fixed by installing `puppetlabs/stdlib` module to use the `file_line` resource type
```
puppet module install puppetlabs-stdlib
```
