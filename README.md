# EGM722Project
Repository for EGM722 Assignment Project

1. Getting started
To get started with the exercises, you'll need to install both git and conda on your computer. Please follow the instructions for installing git from here, and Anaconda from here.

2. Download/clone this repository
Once you have these installed, clone this repository to your computer by doing one of the following things:

Open GitHub Desktop and select File > Clone Repository. Select the URL tab, then enter the URL for this repository.
Open Git Bash (from the Start menu), then navigate to your folder for this module. Now, execute the following command: git clone https://github.com/iamdonovan/egm722.git. You should see some messages about downloading/unpacking files, and the repository should be set up.
You can also clone this repository by clicking the green "clone or download" button above, and select "download ZIP" at the bottom of the menu. Once it's downloaded, unzip the file and move on to the next step. I don't recommend this step, however, as it will be more difficult for you to download the material for each week.
3. Create a conda environment
Once you have successfully cloned the repository, you can then create a conda environment to work through the exercises.

To do this, use the environment.yml file provided in the repository. If you have Anaconda Navigator installed, you can do this by selecting Import from the bottom of the Environments panel.

Otherwise, you can open a command prompt (on Windows, you may need to select an Anaconda command prompt). Navigate to the folder where you cloned this repository and run the following command:

C:\Users\iamdonovan> conda env create -f environment.yml
This will probably take some time (so feel free to catch up on Facebook or whatever kids do nowadays), but fortunately you will only have to do this once. If you

4. Start Jupyter Lab
From Anaconda Navigator, you can launch Jupyter Lab, and navigate to the folder where the first week's practical material is located. Make sure that your egm722 environment is activated.

From the command-line, first open a terminal window or an Anaconda Prompt, and navigate to the folder where you have cloned the repository.

Activate your newly-created environment (conda activate egm722). Next, run Jupyter Lab (jupyter-lab), which should launch a web browser window, which should give you an overview of the current folder.
