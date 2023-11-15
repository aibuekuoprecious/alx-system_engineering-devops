# Ensure that the 'holberton' user exists
user { 'holberton':
  ensure => present,
}

# Set file descriptor limits for the 'holberton' user
file { '/etc/security/limits.d/holberton.conf':
  ensure  => file,
  content => "holberton hard nofile 65536\nholberton soft nofile 65536\n",
}

# Reload PAM configuration to apply the changes
exec { 'reload_pam':
  command  => 'pam-auth-update',
  provider => shell,
  require  => File['/etc/security/limits.d/holberton.conf'], # Ensure file is created before reloading PAM
}

