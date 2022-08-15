Pleasant Lake worked Flopy example
-----------------------------------------------
This repository contains a worked example of the Pleasant Lake problem (Fienen et al., 2022) that demonstrates the use of the [Flopy Python Package](https://github.com/modflowpy/flopy) to assemble a [MODFLOW 6](https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model) groundwater flow model with external array input and advanced boundary conditions.

![Tests](https://github.com/aleaf/2022-gw-tech-spotlight-flopy/workflows/Test/badge.svg)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/aleaf/pleasant-lake-flopy-example/HEAD?labpath=worked_flopy_example.ipynb)
[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

## Running the example
There are two ways to run the example:

1) [online via Binder](https://mybinder.org/v2/gh/aleaf/pleasant-lake-flopy-example/HEAD?labpath=worked_flopy_example.ipynb)
2) Locally on your computer, after creating a suitable python environment

### Running the example locally

1) Download and install the 64-bit [Anaconda python distribution](https://www.anaconda.com/distribution/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

  * Anaconda comes with a larger selection of popular data science and scientific packages, making it ideal for those who use python frequently for scientific computing.
  * Miniconda is a minimal installer with a much smaller footprint, making it ideal for those who only want to run this example.
  * **Make sure to install Anaconda or Miniconda to your username** (not at the system level). 

2) Create a [Conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html)

    Open an Anaconda Command Prompt on Windows or a terminal window on OSX and point it to the location of ``environment.yml`` and enter:

        conda env create -f environment.yml

    **Note:** if the above line executes too slowly, try installing [Mamba](https://mamba.readthedocs.io/en/latest/) and using that instead, i.e.

        mamba env create -f environment.yml

3) Activate the environment
    
    Open an Anaconda Command Prompt on Windows or a terminal window on OSX and enter:

        conda activate flopy_example

4) Run the Notebook

    Make sure that the command window with the conda environment activated is pointed at this folder, or any higher location in the file system. Then enter:

        jupyter notebook

    A new browser tab should pop up with the Jupyter file browser. Navigate to ``worked_flopy_example.ipynb`` and click on it. For more information on Jupyter Notebooks, refer to the documentation: https://jupyter.org.

    **Note:** Running the model through Flopy (as in the Notebook) requires specification of the MODFLOW executable. In the example, we assume that a MODFLOW 6 executable named ``"mf6"`` is visible in the system path at the location of this folder (see the ``exe_name`` argument in Notebook cell 5). Executables for MODFLOW 6 for linux, mac and windows are included in the ``bin/`` folder.

### References
Fienen, M.N., Haserodt, M.J., Leaf, A.T., Westenbroek, S.M., 2022, Simulation of Regional Groundwater Flow and Groundwater/Lake Interactions in the Central Sands, Wisconsin: U.S. Geological Survey Scientific Investigations Report 2022-5046, in press. http://doi.org/10.3133/sir20225046

USGS Software release citation:  
Leaf, A.T. and Fienen, M.N. (2022). Pleasant Lake worked Flopy example, version 0.1, U.S. Geological Survey Software Release (IP-143803; in review), 15 Aug 2022. https://doi.org/10.5066/P9EFHF9H