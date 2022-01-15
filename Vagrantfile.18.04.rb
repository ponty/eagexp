Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.provider "virtualbox" do |vb|
    #   vb.gui = true
    #   vb.memory = "1024"
    vb.name = "eagexp_1804"
  end

  config.vm.provision "shell", path: "vagrant.18.04.sh"

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end

# export VAGRANT_VAGRANTFILE=Vagrantfile.18.04.rb;export VAGRANT_DOTFILE_PATH=.vagrant_${VAGRANT_VAGRANTFILE}
# vagrant up && vagrant ssh
