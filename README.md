
Epic Events CLI
===========================================================


## Prerequisites

Before you begin, ensure that you have the following installed:

- Python 3.x (Python 3.3 or later)
- pip (Python package manager)

## Step 1: Create a Virtual Environment

To create a new Python virtual environment, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to create the virtual environment. You can use the `cd` command to change directories.

3. Run the following command to create a virtual environment. Replace `myenv` with your desired environment name:

   ```bash
   python -m venv myenv
   ```

   This command will create a new directory named `myenv` in your current location, containing the virtual environment.

## Step 2: Activate the Virtual Environment

After creating the virtual environment, you need to activate it to start using it. Follow these steps:

### On Windows:

1. Open a command prompt.

2. Navigate to the directory where you created your virtual environment.

3. Activate the virtual environment by running the activation script:

   ```bash
   myenv\Scripts\activate
   ```

   You will see the virtual environment's name in your command prompt, indicating that it is now active.

### On macOS and Linux:

1. Open a terminal.

2. Navigate to the directory where you created your virtual environment.

3. Activate the virtual environment by running the activation script:

   ```bash
   source myenv/bin/activate
   ```

   You will see the virtual environment's name in your terminal prompt, indicating that it is now active.

## Step 3: Using the Virtual Environment

Once your virtual environment is activated, you can install Python packages and work on your project without affecting your system-wide Python installation.

Example: Installing a package using `pip`:

```bash
pip install package_name
```

To deactivate the virtual environment and return to your system's Python environment, simply run the following command:

```bash
deactivate
```

## Step 4: Install requirements.txt

Once everything above is setup you should install the packages and librairies of the project, it will not work without them:

```bash
pip install -r requirements.txt
```

## Step 5: Run the app

### On Windows:

```bash
    main.py
```

### On Lniux/MacOS:


```bash
    python main.py
```

or 

```bash
    ./main.py
```


## Others:

1. Testing :
   
    Basic testing :
    pytest .

    Test coverage run :
    coverage run -m pytest .
    coverage report

    Test coverage gutters :
    in VSCode with extension coverage gutters you can show test coverage directly in the code
    after generating a coverage.xml file with : 
    
```bash
    python -m pytest --cov=. --cov-report=xml tests
```
   
    using this shortcut -> ctrl + shit + è