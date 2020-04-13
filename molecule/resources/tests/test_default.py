import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_sudoers_file_valid(host, sudoers_d_path="/etc/sudoers.d", visudo_path="/usr/sbin/visudo"):
    sudoers_files = host.run("ls -1 -q -- {sudoers_d_path}".format(sudoers_d_path=sudoers_d_path))
    sudoers_files = sudoers_files.stdout.splitlines()
    for sudoers_file in sudoers_files:
        command = "{visudo_path} -cf {sudoers_file}".format(visudo_path=visudo_path, sudoers_file=sudoers_file)
        output = host.check_output()

        assert f.exists
        assert f.user == "root"
        assert f.group == "wheel"
