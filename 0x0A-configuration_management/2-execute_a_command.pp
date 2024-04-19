# 2-execute_a_command.pp

# Define an exec resource to kill the process named "killmenow"
exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  path        => '/usr/bin',
  refreshonly => true,
}

# Notify when the command has been executed
notify { 'Process killed successfully':
  subscribe => Exec['killmenow'],
}
