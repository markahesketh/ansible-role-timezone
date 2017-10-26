import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cowsay_is_installed(host):
    timezone = host.file("/etc/timezone")
    assert timezone.contains("Europe/London")
