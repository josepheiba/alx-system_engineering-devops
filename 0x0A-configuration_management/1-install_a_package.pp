# 1-install_a_package.pp

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'python3-pip':
  ensure => installed,
}
