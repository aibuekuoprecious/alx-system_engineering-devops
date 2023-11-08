# Fix the 500 error by replacing "phpp" with "php" in wp-settings.php
exec { 'replace':
  # Use the shell provider to execute the command
  provider => shell,

  # Replace all occurrences of "phpp" with "php" in wp-settings.php
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
