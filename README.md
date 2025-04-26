# EGM722Project
Repository for EGM722 Assignment Project

## 1. Getting started

To get started with the exercises, you'll need to install both `git` and `conda` on your computer. You can follow the instructions for installing git from [here](https://git-scm.com/downloads), 
and Anaconda from [here](https://docs.anaconda.com/anaconda/install/). 

## 2. Download/clone this repository

Once you have these installed, __clone__ this repository to your computer by doing one of the following things:

1. Open GitHub Desktop and select __File__ > __Clone Repository__. Select the __URL__ tab, then enter the URL for this 
   repository.
2. Open __Git Bash__ (from the __Start__ menu), then navigate to your folder for this module.
   Now, execute the following command: `git clone https://github.com/RoyCoates/EGM722Project.git`. You should see some messages
   about downloading/unpacking files, and the repository should be set up.

## 3. Create a conda environment

Once you have successfully cloned the repository, you now have to create a `conda` environment.

To do this, use the environment.yml file provided in the repository. If you have Anaconda Navigator installed,
you can do this by selecting __Import__ from the bottom of the __Environments__ panel. 

Otherwise, you can open a command prompt (on Windows, you may need to select an Anaconda command prompt). Navigate
to the folder where you cloned this repository and run the following command:

```
C:\Users\RoyCoates> conda env create -f environment.yml
```

This will take some time but fortunately you only have to do this once.

## 4. Start Jupyter Lab

From Anaconda Navigator, you can launch Jupyter Lab. Make sure that your `EGM722Project` environment is activated.

From the command-line, first open a terminal window or an __Anaconda Prompt__, and navigate to the folder where you have
cloned the repository.

Activate your newly-created environment (`conda activate EGM722Project`). 

Next, run Jupyter Lab (`jupyter-lab`),which should launch a web browser window, which should give you an overview of the current folder. 

Navigate and select the file `EGM722Project.ipynb` under __"https://github.com/RoyCoates/EGM722Project.git"__ 

## 5. PyCharm - Download & Set-Up

To view and execute the programme file `EGM722Project.py` that is in the GIT repository. I suggest you download and install PyCharm. PyCharm is an Integrated Development Environment (IDE)

__Note:__ The files `EGM722Project.py` & `EGM722Project.ipynb`both run the same code. The `.py file` can be used with PyCharm. The `.ipynb` can be used with Jupyter Lab

You can download PyCharm [here](https://www.jetbrains.com/pycharm/download/other.html). Select the version for your current operating system (Windows, MacOS, or linux). 
When installed, open and select __Create New Project__

For __Location__, choose the folder where you cloned the EGN722Project repository

Next, set-up a python interpreter. The conda environment that you have already set-up  can be ised as the interpreter for this project. 

In the New Project pane, go to __Environment__ and select __Select Existing__

Under __Type__ select __Conda__. 

The path to the __conda__ program is `~/Anaconda3/bin/conda` or `~/Anaconda3/condabin/conda.bat`
When the path is set, click __Create__ and select __Create from Existing Sources__

## 6. Run the code
The project code will load an interactive map of the M20 motorway in Ireland. Lighting columns scheduled for LED upgrading aswell as Drainage Assets that require inspection will be available as layers on the map.

All the shapefile required to run the code are stored in the file `data_files` in the GIT repository

Use Jupyter Lab  to run the `EGM722Project.ipynb` file or PyCharm to run the `EGM722Project.py`file.
