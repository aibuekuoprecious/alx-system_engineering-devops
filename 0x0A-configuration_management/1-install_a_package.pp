# Puppet manifest for installing a Python package named "flask"
# using the "pip3" provider with a specific version requirement.

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
