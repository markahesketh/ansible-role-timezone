# Ansible Role: Timezone

[![Build Status](https://travis-ci.org/markahesketh/ansible-role-timezone.svg?branch=master)](https://travis-ci.org/markahesketh/ansible-role-timezone)

Ansible role to manage timezones.

## Installation

```
ansible-galaxy install markahesketh.timezone
```

## Role Variables

Default values are listed below (see [`defaults/main.yml`](defaults/main.yml)):

```yml
timezone_zone: "Etc/UTC"
```

The `timezone_zone` variable will accept a [valid timezone](https://www.vmware.com/support/developer/vc-sdk/visdk400pubs/ReferenceGuide/timezone.html) such as ``"Europe/London"`.

## Dependencies

None.

## Example Playbook

```yml
- hosts: web
  roles:
    - markahesketh.timezone
  vars:
    timezone_zone: "Europe/London"
```

## Testing

    molecule test

Requires [Molecule](https://molecule.readthedocs.io/en/latest/) and [Docker](https://docs.docker.com/engine/installation/).

## License

This role is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT).

## Author

By [Mark Hesketh](https://www.markhesketh.co.uk/), a web developer from Manchester, UK.

* Blog: [markhesketh.co.uk](https://www.markhesketh.co.uk/)
* Twitter: [twitter.com/markahesketh](https://www.twitter.com/markahesketh/)
* GitHub: [github.com/markahesketh](http://www.github.com/heskethm/)
* Email: [contact@markhesketh.co.uk](mailto:contact@markhesketh.co.uk)
