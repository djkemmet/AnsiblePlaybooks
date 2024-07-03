# Imports
import click

# CREATE COMMAND: Export a Policy Module Template
@click.command()
@click.option('--export-policy-module-template', help="Provides Policy Module Template ready for use.")
def export_policy_module_template():
    """
    this function is responsible for exporting a ready to use
    policy module for the requestor.
    """
    print("This is the Export Policy Function")

# Import a Policy Module Template, Confirm
@click.command()
@click.option('--export-policy-module-template', help="Provides Policy Module Template ready for use.")
def import_policy_module():
    """
    This function is responsible for importing a policy module, as 
    a .zip file, and 'installing' it upon validation
    """
    print("This command Imports a policy module")
# Create Code to open these YML Files as objects.
