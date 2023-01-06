# CA2 - Statistics and Machine Learning Analysis on the Irish Agriculture Sector

This repository contains the source code and datasets used for the CA2.

## Folder strucutre

The folder structure is organized as follows:

- jupyter

  It contains all the Jupyter files, source code and the dashboard that were implemented.
  
  - datasets

    It also contains the original datasets and the folder with the processed datasets after EDA.
    
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

  It contains the Word report.
  
- dashboard

  It contains the Jupyter notebook used to extract the dashboard and its already extracted HTML version.

## How to run the Statistical and ML models?

DataPrepVis generates the processed datasets to be consumed by the other notebooks.

However, all files needed to run the Jupyter notebooks are already created, so the Jupyter files can be executed in any order.

In case any file is missing, the DataPrepVis Jupyter notebook should be executed first.

## How to see the dashboard?

The dashboard was already extracted using Voila tool. 

So, under jupyter/dashboard folder, just click on the DataPrepVisDashBoard.html.
