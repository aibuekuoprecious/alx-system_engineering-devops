# Update package list
exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
}

# Install Nginx
exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  require  => Exec['update'], # Ensure 'update' is executed first
}

# Add custom header to Nginx configuration
exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "/server {/a add_header X-Served-By \"$HOST\";" /etc/nginx/sites-available/default',
  require     => Exec['install Nginx'], # Ensure 'install Nginx' is executed first
  before      => Exec['restart Nginx'],
}

# Restart Nginx to apply changes
exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  require  => Exec['add_header'], # Ensure 'add_header' is executed first
}

# Alternatively, combine all steps together
# exec { 'setup_nginx':
#   provider    => shell,
#   environment => ["HOST=${hostname}"],
#   command     => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo sed -i "/server {/a add_header X-Served-By \"$HOST\";" /etc/nginx/sites-available/default && sudo service nginx restart',
# }
