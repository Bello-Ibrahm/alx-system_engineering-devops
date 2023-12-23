#!/usr/bin/pup
# Using Puppet to install flask from pip3

package {'python3-pip':
  ensure  => present,
}

package {'werkzeug':
  ensure   => '2.1.1',
  provider =>'pip3',
}

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
