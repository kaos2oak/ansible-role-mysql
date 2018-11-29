# MySQL

Install MySQL

This role is designed to install MySQL Community Edition.

## Requirements

This role is currently designed to be used with a MySQL installer downloaded
from the [MySQL web site](https://www.mysql.com).

Currently, this role has only been tested with the version set as default
(8.0.13).

If you are running Ansible 2.4 or above on macOS High Sierra or above, you may
want to learn more about an issue with "changes made in High Sierra that are
breaking lots of Python things that use fork()."
See Ansible issue [32499](https://github.com/ansible/ansible/issues/32499) for
more information.

Because of the above issue, you may want to include this line in your
`Vagrantfile` if you are using vagrant:

    ENV["VAGRANT_OLD_ENV_OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"

You may also need to run the following command prior to executing molecule
tests with vagrant:

        export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES



## Role Testing

### Pre-requisites

[Molecule](https://molecule.readthedocs.io/en/latest/) is being used for
testing this role.

You will need to install molecule and python support modules before running
the role tests:

    pip install molecule
    pip install docker-py

You also need to install the following before running the vagrant role tests:

    pip install python-vagrant

You may also need to run the following command prior to executing molecule
tests with vagrant (see [Requirements](#requirements)):

    export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

The 'verifier' for Windows is disabled as I have not yet been able to get the
testinfra verfication to work for Windows. If you have any experience or advice
in this area, please let me know.

### MySQL Versions

To run the molecule tests for a particular MySQL version, you will need to
provide the `MYSQL_VERSION` as an environment variable and ensure the installer
is located locally in the appropriate ...`INSTALLERS_PATH` location. See
examples, below.

It is also possible to edit the `molecule.yml` file for a scenario and
specify the mysql_version like this:

    provisioner:
      name: ansible
      env:
        MYSQL_VERSION: 5.7.24

### Default Tests

No default tests are currently implemented.

### Ubuntu Tests

Ubuntu 18 & 16 via vagrant:

    molecule test --scenario-name ubuntu-vagrant

or

    MYSQL_VERSION=5.7.24 molecule test --scenario-name ubuntu-vagrant

### RedHat Tests

RedHat 7 & 6 via vagrant:

    molecule test --scenario-name redhat-vagrant

### macOS Tests

macOS 10.13, 10.12, 10.11 via vagrant:

    molecule test --scenario-name macos-vagrant

### Windows Tests

Window 2012r2 via vagrant:

    molecule test --scenario-name windows-vagrant

## Docker Space Issues

If you find that your drive space is disappearing, you may want to refer to
[Docker for Mac: reducing disk space](https://djs55.github.io/jekyll/update/2017/11/27/docker-for-mac-disk-space.html).

## License

MIT

## Author Information

Justin Sako
