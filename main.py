#This program creates a `README.md` file using GitHub-flavored markdown.


from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from rich.console import Console
from rich.panel import Panel
import os

# Initializing Rich console
console = Console()

# Select License-Expression As of Metadata 2.4, License and License-Expression are mutually exclusive. If both are specified, tools which parse metadata will disregard License and PyPI will reject uploads. 
license = [
    Choice("None", name="None."),
    Choice("MIT", name="MIT License – Permissive, allows modification and distribution with attribution."),
    Choice("BSD-3-Clause", name="BSD-3-Clause."),
    Choice("MIT AND (Apache-2.0 OR BSD-2-Clause)", name="GNU General Public License (GPL v3) – Strong copyleft, modifications must remain open-source."),
    Choice("MIT OR GPL-2.0-or-later OR (FSFUL AND BSD-2-Clause)", name="GNU Lesser General Public License (LGPL v3) – Weak copyleft, allows use in proprietary software."),
    Choice("GPL-3.0-only WITH Classpath-Exception-2.0 OR BSD-3-Clause", name="This software may only be obtained by sending the author a postcard, and then the user promises not to redistribute it."),
    Choice("LicenseRef-Special-License OR CC0-1.0 OR Unlicense", name="Creative Commons Licenses (CC0, CC BY, etc.) – For non-code assets like documentation."),
    Choice("LicenseRef-Proprietary", name="Unlicense – Public domain dedication, no restrictions.")
]

# Input and processing
name = input("Welcome to Readme.md GitHub Creator. What is your name? ")
print(f"Hello, {name}, you look great today!, let's create readme.md for your repository together today:")

#Main for user input
def main():
    console.print(Panel("GitHub README.md Generator in Markdown format", style="italic white"))

    # Prompt user for project details
    project_title = inquirer.text(message="## Project Title: ").execute()
    project_description = inquirer.text(message="## Description: ").execute()
    installation_instructions = inquirer.text(message="## Installation Instructions, (Requires-Python: >=3.6):  ").execute()
    usage_instructions = inquirer.text(message="## Usage Information:  ").execute()
    license_choice = inquirer.select(
        message = "##License (choose from a dropdown list use up and down buttons on your keyboard )",
        choices = license,
        default ="MIT License"
    ).execute()
    contact_info = inquirer.text(message="## Contact Information: ").execute()

    # Generate README.md content
    readme_content = f"""# {project_title} 

## Description 
{project_description}

## Installation Instructions 
{installation_instructions}

### 1. Install Python

1. Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/)
1. Setting Up the Environment

```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# Install dependencies

Since two libraries are required (`InquirerPy` and `Rich`), a `requirements.txt` file is provided to manage dependencies.
pip install -r requirements.txt
s
## Usage Information 
{usage_instructions}

## License 
This project is licensed under the {license_choice}

## Author name: 
{name}

## Please feel free to contact me for further information 
{contact_info}

"""

    # Write and save README.md file as Markdown - checks if file already exists
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)
        if os.path.exists("README.md"):
            overwrite = inquirer.confirm(message="README.md already exists. Overwrite?", default=False).execute()
            if not overwrite:
                console.print("Creating README.MD cancelled.")
                return
    console.print(Panel(f"[green]README.md successfully created![/green]", style="bold green"))
    console.print(f"Please save your README file in the root of your project, in the same directory as your .py file.")
    
    again()

def again():
    option_again = input(f"Hello, {name}, do you want to start over again to correct some details? Please type Y for YES or N for NO ")
    if option_again.strip().lower() == 'y':
        main()
    elif option_again.strip().lower() == 'n':
        print(f"Awesome {name} , I hope I helped, see you later on creating new readme.md for your next project. ")
    else:
        again()

if __name__ == "__main__":
    main()