# EGM722Project - Lighting Column Upgrades and Drainage Asset Cleaning on the M20 Motorway, Ireland

In order to run the Python code, there are a number of steps that need to be followed. Please complete these in the order as set out below.

## 1. To Start

In order to run the Python code , you'll need to install both `git` and `Anaconda` on your computer. . The link and instructions for installing git can be found [here](https://git-scm.com/downloads), 
and Anaconda from [here](https://docs.anaconda.com/anaconda/install/). 

## 2. Download/Clone this repository

Once you have the two items above installed, you can __clone__ this repository to your computer:
   
   2.1 Open GitHub Desktop and select __File__ > __Clone Repository__. 
   
   2.2 Select the __URL__ tab, then enter the URL for this repository which is __https://github,com/RoyCoates/EGMProject__
   
   2.3 Open __Git Bash__ (from the __Start__ menu), then navigate to your folder.
   
   2.4 Execute the following command: __`git clone https://github.com/RoyCoates/EGM722Project.git`__. 
   You should see messages relating to downloading/unpacking files, and the repository should be set up.

## 3. Create a conda environment

Once you have successfully cloned the repository, you now must create a `conda` environment.

Select the __environment.yml__ file provided in the repository. Using Anaconda Navigator,
select __Import__ from the bottom of the __Environments__ panel. 

Otherwise, you can open a command prompt (on Windows, you may need to select an Anaconda command prompt). Navigate
to the folder where you cloned this repository and run the following command:

```
C:\Users\RoyCoates> conda env create -f environment.yml
```

This step will only have to be performed once.

## 4. Start Jupyter Lab 

From the Anaconda Navigator, you can launch Jupyter Lab. Make sure that your `EGM722Project` environment is activated.

From the command-line, first open a terminal window or an __Anaconda Prompt__, and navigate to the folder where you have
cloned the repository.

Activate your newly-created environment (`conda activate EGM722Project`). 

Next, run Jupyter Lab (`jupyter-lab`),which should launch a web browser window, which should give you an overview of the current folder. 

Navigate and select the file `EGM722Project.ipynb` under __"https://github.com/RoyCoates/EGM722Project.git"__ 

__Note:__ The files `EGM722Project.py` & `EGM722Project.ipynb`both run the same code. The `.py file` can be used with PyCharm. The `.ipynb` can be used with Jupyter Lab

## 5. PyCharm - Download & Set-Up

To view and execute the programme file `EGM722Project.py` that is in the GIT repository. I suggest you download and install PyCharm. PyCharm is an Integrated Development Environment (IDE)

You can download PyCharm [here](https://www.jetbrains.com/pycharm/download/other.html). Select the version for your current operating system (Windows, MacOS, or linux). 
When installed, open and select __Create New Project__

For __Location__, choose the folder where you cloned the EGM722Project repository

Next, set-up a python interpreter. The conda environment that you have already set-up  can be ised as the interpreter for this project. 

In the New Project pane, go to __Environment__ and select __Select Existing__

Under __Type__ select __Conda__. 

The path to the __conda__ program is `~/Anaconda3/bin/conda` or `~/Anaconda3/condabin/conda.bat`
When the path is set, click __Create__ and select __Create from Existing Sources__

## 6. Run the code
The project code will load an interactive map of the M20 motorway in Ireland. Lighting columns scheduled for LED upgrading aswell as Drainage Assets that require inspection will be available as layers on the map.

All the shapefile required to run the code are stored in the file `data_files` in the GIT repository

Use Jupyter Lab  to run the `EGM722Project.ipynb` file or PyCharm to run the `EGM722Project.py`file.
