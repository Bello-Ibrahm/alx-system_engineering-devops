# Tasks
## 0. World wide web



# Certbot installation [Here](https://eff-certbot.readthedocs.io/en/latest/install.html) and [Here](https://certbot.eff.org/instructions?ws=haproxy&os=ubuntufocal)

## Run Certbot with -v:
Rerun Certbot with the -v option to get more verbose output and additional details about the issue:
``` sudo certbot certonly --standalone -d belloibrahim.tech -v ```

# Review Certbot Log:
Check the Certbot log file for more detailed information:
``` sudo cat /var/log/letsencrypt/letsencrypt.log ```

## Certificate is saved at:
```/etc/letsencrypt/live/www.belloibrahim.tech/fullchain.pem```

Key is saved at:
```/etc/letsencrypt/live/www.belloibrahim.tech/privkey.pem```
