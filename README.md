# MySQL

Install MySQL

This role is designed to install MySQL Community Edition. The role works with
version 8 and 5.7 and may work with 5.6, but has not been extensively tested
on all possible versions.

## Requirements

This role is currently designed to be used with a MySQL installer downloaded
from the [MySQL web site](https://www.mysql.com) and placed locally on your
"controller" (the machine from which you are running the Ansible playbook).

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

## Environment Variables

| Option                                | Default | Example                                  |
| :------------------------------------ | :------ | :--------------------------------------- |
| `MYSQL_LINUX_LOCAL_INSTALLERS_PATH`   | none    | `/Users/Shared/Installers/Linux/MySQL`   |
| `MYSQL_MAC_LOCAL_INSTALLERS_PATH`     | none    | `/Users/Shared/Installers/macOS/MySQL`   |
| `MYSQL_WINDOWS_LOCAL_INSTALLERS_PATH` | none    | `/Users/Shared/Installers/Windows/MySQL` |
| `MYSQL_LOCAL_INSTALLERS_PATH`         | none    | `/Users/Shared/Installers/MySQL`         |
| `MYSQL_VERSION`                       | none    | `8.0.13` or `5.7.24    `                 |

## Role Variables

| Option                        | Default                    | Example                                                                                     |
| :---------------------------- | :------------------------- | :------------------------------------------------------------------------------------------ |
| `mysql_version`               | `8.0.13`                   | `5.7.24`                                                                                    |
| `mysql_installers_path`       | `/Users/Shared/Installers` | `/Users/Shared/Installers/MySQL`                                                            |
| `mysql_root_password`         | `root`                     | `rootp@ssW0rd`                                                                              |
| `mysql_authentication_plugin` | `mysql_native_password`    | `caching_sha2_password`                                                                     |
| `mysql_databases`             | none                       | `testdb`                                                                                    |
| `mysql_users`                 | none                       | `- { name: 'testuser', host: 'localhost', password: 'testpass' }`                           |
| `mysql_user_access`           | none                       | `- { name: 'testuser', host: 'localhost', access: 'ALL', database: 'testdb', tables: '*' }` |

## Dependencies

Installation of MySQL on Windows requires the appropriate Visual C++
Redistributable for Visual Studio.  MySQL 5.7 requires 2013, while MySQL 8
requires 2015.

## Role Use

Use of this role consists of the following:

* Create a playbook
* Obtain and have the desired installer available locally on the ansible
  controller
* Provide the location of the installer on the controller as an environment
  variable, in the playbook or as an extra-var
* Provide the version of MySQL (must match the installer) as an environment
  variable, in the playbook or as an extra-var
* Run the playbook

### Example Playbooks

``` yaml
- name: Install MySQL
    hosts: servers
    roles:
        - { role: kaos2oak.mysql }
```

``` yaml
- name: Install MySQL 5.7.24
    hosts: servers
    vars:
        mysql_version: '5.7.24'
    roles:
        - { role: kaos2oak.mysql }
```

``` yaml
- name: Install MySQL 5.7.24 and create mydb
    hosts: servers
    vars:
        mysql_version: '5.7.24'
        mysql_root_password: W7HgBBja*ELuiGRrnuJ
        mysql_databases:
            - mydb
        mysql_users:
            - { name: 'myuser', host: 'localhost', password: 'TGhXAgWTK*yGHd2' }
        mysql_user_access:
            - { name: 'myuser', host: 'localhost', access: 'ALL', database: 'mydb', tables: '*' }
    roles:
        - { role: kaos2oak.mysql }
```

### Example Installer Locations

If you really want it to be quick and easy:

    export MYSQL_LOCAL_INSTALLERS_PATH="$HOME/Downloads"

Or, you could always move the installers to the default location after
downloading them:

    /Users/Shared/Installers/MySQL

If you like to keep things neat and organized, you might organize the installers
into folders, create a file named something like `setup` in a directory named
`my` in this repository (the `my` directory is part of the .gitignore, so it
will not be part of any commit) and then `source` the file:

``` shell
# File: setup
export MYSQL_MAC_LOCAL_INSTALLERS_PATH="$HOME/Installers/Mac/MySQL"
export MYSQL_LINUX_LOCAL_INSTALLERS_PATH="$HOME/Installers/Linux/MySQL"
export MYSQL_WINDOWS_LOCAL_INSTALLERS_PATH="$HOME/Installers/Windows/MySQL"
```

    source my/setup

### Example MySQL Version

Since the MySQL version may be something that you want to change on the fly,
you probably don't want to include it in the `setup` file, but you can always
provide it on the command line before the ansible-playbook run:

    export MYSQL_VERSION=5.7.24

Or, provide as part of the ansible-playbook run (see below).

### Example Playbook Runs

Assuming you have created a playbook named `k2o-mysql.yml`:

    ansible-playbook k2o-mysql.yml

    MYSQL_VERSION=5.7.24 ansible-playbook k2o-mysql.yml

    ansible-playbook k2o-mysql.yml -e "mysql_version=5.7.24"

If the playbook itself contains the version of Java:

    ansible-playbook k2o-mysql-5.7.24.yml

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
