
Vagrant.configure("2") do |config|

  config.vm.define :pyconomy do |pyconomy|
    pyconomy.vm.box = 'heroku/trusty64'
    pyconomy.vm.hostname = 'pyconomy.box'
    pyconomy.vm.network 'private_network', ip: '192.168.0.42'
    pyconomy.vm.boot_timeout = 500
    pyconomy.vm.network 'forwarded_port', guest: 8000, host: 8000, auto_correct: true
    pyconomy.vm.network 'forwarded_port', guest: 5432, host: 5432, auto_correct: true
    pyconomy.vm.provision 'ansible' do |ansible|
      ansible.sudo = true
      ansible.playbook = 'playbook.yml'
    end
  end

end
