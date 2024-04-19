# 1-install_a_package.pp

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['uninstall_flask'],  # Ensure the uninstallation is done before attempting installation
}

exec { 'uninstall_flask':
  command => 'pip3 uninstall -y Flask==2.1.0',
  path    => '/usr/local/bin',  # Adjust the path if necessary
  onlyif  => 'pip3 show Flask | grep -q "Version: 2.1.0"',  # Check if Flask 2.1.0 is installed
}
