# Generating Configs using Ansible, YAML, & Jinja2

### Prerequisites
```
pip install ansible
```

### To Generate Templates

``` console
ANSIBLE_STDOUT_CALLBACK=debug \
ansible-playbook -i inventory generate_configs.yml
```
