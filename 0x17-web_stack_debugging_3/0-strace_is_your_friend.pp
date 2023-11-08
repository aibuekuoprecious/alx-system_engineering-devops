# Install and start Apache
class { 'apache':
  docroot => '/var/www/custom',
}

# Create the custom document root directory
file { '/var/www/custom':
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Place an index.html file in the custom document root
file { '/var/www/custom/index.html':
  ensure  => 'present',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  content => 'Hello, world!',
}

# Set up a virtual host on port 80
apache::vhost { 'example.com':
  port    => '80',
  docroot => '/var/www/custom',
}
