# kill_process.pp

exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/usr/bin',
  refreshonly => true,
}
