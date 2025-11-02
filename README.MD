
<p align="center" width="100%">
<video src="https://youtu.be/zzbJi6_FMxc" width="80%" controls></video>
</p>

## Python README File Generator 

## Description 
As a developer, I want to automatically generate a professional README file for my GitHub projects, so that I can save time and ensure my repositories are well-documented.

## Installation Instructions 
Follow instruction in the readme.md file to install Virtual Environment. Managing Python dependencies using library to os, InquirerPy, Rich pip install -r requirements.txt Run the program: python main.py
Clone the project onto your computer with: 
git clone https://github.com/piotrowskaannamilena-blip/readme-generator

### 1. Install Python

1. Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/)
2. Verify installation by running the following command in the terminal:
   ```sh
   python --version
   ```
   or on MacOS
   ```sh
   python3 --version
   ```
### 2. Set Up VSCode for Python
1. Install VSCode if you haven't already: VSCode Download
2. Open VSCode and install the Python extension from the Extensions Marketplace.
3. Open the terminal in VSCode (Ctrl + ~ on Windows/Linux, Cmd + ~ on Mac) and check if Python is detected:
```sh
python --version
```
### 3. Setting Up the Environment
1. Navigate to your project folder:
```sh
mkdir my_python_project
cd my_python_project
```
2. Create a virtual environment:
```sh
python -m venv venv
```
3. Activate the virtual environment
- Windows:
```sh
venv\Scripts\activate
```
- MacOS:
```sh
source venv/bin/activate
```
4. Verify that your virtual environment is active by running:
```sh
python --version
```
### 4. Set Python Path Variables (if necessary)
- If python is not recognized, you may need to add Python to your system’s PATH variable.
- Check Python’s installation location
```sh
where python  # Windows
which python  # Mac/Linux
```
- Add this path to your system’s environment variables if needed.
### 5. Create and Run Your First Python Program

### 6. Install dependencies

Since two libraries are required (`InquirerPy` and `Rich`), a `requirements.txt` file is provided to manage dependencies.
pip install -r requirements.txt

In a terminal of VSCode, in the project directory: 
pip install -r requirements.txt
Run the program: 
python3 main.py 
python main.py

## Usage Information 
The user is prompted for project details including title, description, installation, usage, license, author, and contact info. A `README.md` file is generated using GitHub markdown format based on the user's input.

## License 
This project is licensed under the MIT

## Author name: 
Anna Piotrowska

## Please feel free to contact me for further information 
Anna Piotrowska www.linkedin.com/in/anna-piotrowska-4588a49b 


