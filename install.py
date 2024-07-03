# Imports
import os
import shutil

# Check for and install ansible-core
if not (os.system("which ansible") == 0):
    print("Ansible is not installed on the system, installing...")
    os.system("dnf install ansible-core -y")
else:
    print("Ansible Appears installed")
# Check for and install ansible.builtin collection
if not (os.system("ansible-galaxy collection install community.general") == 0):
    print("community.general is not installed on the system, installing...")
    os.system("ansible-galaxy collection install community.general")
# Copy /applyPolicyDocument.yml /destroyPolicyDocument.yml /executePolicyDocument.yml policyModules/ to /etc/ansible
shutil.copyfile('./applyPolicyDocument.yml', '/etc/ansible/applyPolicyDocument.yml')
shutil.copyfile('./destroyPolicyDocument.yml','/etc/ansible/destroyPolicyDocument.yml')
shutil.copyfile('./executePolicyDocuments.yml', '/etc/ansible/executePolicyDocuments.yml')
os.system("mkdir /etc/ansible/policyModules")
