# CA2 - Statistics and Machine Learning Analysis on the Irish Agriculture Sector

This repository contains the source code and datasets used for the CA2.

## Folder strucutre

The folder structure is organized as follows:

- jupyter

    It contains all the Jupyter files, source code and the dashboard that were implemented.
  
    - dashboard

        It contains the previously extracted HTML dashboard.

    - datasets

        It contains the original datasets and the folder with the processed datasets after EDA.
    
    - images

        It contains the images generated from the Jupyter notebooks.
    
    - modules

        It contains the following Python modules implemented specifically for this project:

        - JSON Helper
        - Twitter API
        - Text Processor
  
        All the dependencies are properly configured in the Jupyter notebooks.

- project-mngmt

    It contains the Excel file used to manage the tasks and requirements of the project.

- report

    It contains the Word report, cover sheet and images used.
  

## How to run the Statistical and ML models?

DataPrepVis generates all the processed datasets that are consumed by the other notebooks.

All dataset and image files required to run the Jupyter notebooks have already been created, so the Jupyter files can be executed in any order.

In case any file is missing, the DataPrepVis Jupyter notebook should be executed first, then any other Jupyter file can be executed.

Each Jupyter file has its own instructions with regards to dependencies or requirements.

## How to see the dashboard?

The dashboard Jupyter file is DataPrepVisDashboard, which has been previously processed using Voila tool and the extracted HTLM version is available under the dashboard folder.

The user can run the Jupyter extension or the command bellow on any Jupyter file in order to execute the Voila tool to extract the dashboard from scratch.

```
voila jupyter_file
```
