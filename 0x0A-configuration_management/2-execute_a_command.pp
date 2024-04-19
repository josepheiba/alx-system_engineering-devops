# 2-execute_a_command.pp

exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  path        => ['/usr/bin'],
  onlyif      => '/usr/bin/pgrep -f killmenow',
  refreshonly => true,
}

notify { 'Process killed successfully':
  subscribe => Exec['killmenow'],
}
