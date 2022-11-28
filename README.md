- Run each playbook from your Windows machines using a container with Ansible configured.
	- Please set up of the CentOS SSH key on your Windows Ansible container
	- ansible.cfg is configured to use private_key_file = /home/ansible/.ssh/centos7_ansible_rsa by default. Please update this to reflect the CentOS7 RSA Key copied from your machine.

- Set the the ansible user in your ansible.cfg
	- `remote_user=ansible`

- Add your host file to ansible.cfg


- Here is an example of my ansible.cfg


```
[defaults]
 
inventory = /home/ansible/hosts.yml
 
private_key_file = /home/ansible/.ssh/centos7_ansible_rsa
 
interpreter_python = /usr/bin/python
remote_user=ansible
```


- Create Host file
```
[SM]
x.x.x.x

```

- Download `sm_metadata_info.csv`, `sm_metadata_generator.py`, `sm_metadata_add.yml` to your local computer

- Fill out the stream information in `sm_metadata_info.csv` spreadsheet

- Copy `sm_metadata_info.csv`, `sm_metadata_generator.py`, `sm_metadata_add.yml` to your ansible-control container 

    *Example*
    
    -`docker cp sm_metadata_info.csv ansible-control:/home/ansible/`


- Before proceed to run the .py script in the next step, make sure you have pandas module install

    - `sudo apt install python-pip3`
    - `sudo pip3 install pandas`

- Run `sm_metadata_generator.py`, this script will ask you to enter the path of your `sm_metadata_info.csv` file 


    -`python3 sm_metadata_generator.py`

- Once the .py script is ran, it will generates a `metadata_add_script.sh` bash script

- Run the `sm_metadata_add.yml` playbook, this playbook will move the `metadata_add_script.sh` to SM and run it there

    - `eval $(ssh-agent -s)`
    - `ssh-add ~.ssh/centos7_ansible_rsa`
    - `ansible-playbook sm_metadata_add.yml --ask-vault-pass -v`
