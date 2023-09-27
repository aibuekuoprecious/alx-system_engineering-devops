# creating a file named "school" in the "/tmp" directory 
# with specific permissions, owner, group, and content

file { 'school':
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
