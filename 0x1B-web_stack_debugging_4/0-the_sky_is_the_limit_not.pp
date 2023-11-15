# Update NGINX configuration based on requests input
exec { 'update_nginx_config':
  command  => 'sed -i s/15/5000/g /etc/default/nginx',
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
}

# Restart NGINX to apply the updated configuration
exec { 'restart_nginx':
  command  => 'sudo service nginx restart',
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
}

