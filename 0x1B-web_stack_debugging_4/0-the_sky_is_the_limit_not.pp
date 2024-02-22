# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'set-limit-to-2000':
  command => 'sed -i "s/15/2000/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin']
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}