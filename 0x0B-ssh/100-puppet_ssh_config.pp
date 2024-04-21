file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path  => '/home/ubuntu/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
  ensure => present,
}
