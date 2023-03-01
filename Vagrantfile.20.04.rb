Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.provider "virtualbox" do |vb|
    #vb.gui = true
    # vb.memory = "2048"
    vb.name = "eagexp_2004"
  end
      config.vm.provision "shell", path: "vagrant.20.04.sh"
      config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]       
end
     

