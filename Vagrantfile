Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.provider "virtualbox" do |vb|
    #vb.gui = true
    # vb.memory = "2048"
    vb.name = "eagexp_2204"
  end

      config.vm.provision "shell", path: "vagrant.22.04.sh"

      config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]       
end
     

