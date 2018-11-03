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

## License

MIT

## Author Information

Justin Sako
