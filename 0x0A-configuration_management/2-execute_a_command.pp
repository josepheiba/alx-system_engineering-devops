# kill_process.pp

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin',
  refreshonly => true,
}
