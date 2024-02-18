import pandas as pd
import logging
import argparse
import yaml
import os
import requests



logging.basicConfig(
    handlers=(logging.StreamHandler(), logging.FileHandler('uci_iris.log')), 
    level=logging.INFO,
    )




# class yourteamrepo.Analysis.Analysis(analysis_config:str)
class Analysis:
''' Load config file into an Analysis object

Load system-wide configuration from `configs/system_config.yml`, user configuration from
`configs/user_config.yml`, and the specified analysis configuration file

Parameters
----------
analysis_config : str
    Path to the analysis/job-specific configuration file

Returns
-------
analysis_obj : Analysis
    Analysis object containing consolidated parameters from the configuration files

Notes
-----
The configuration files should include parameters for:
    * GitHub API token
    * ntfy.sh topic
    * Plot color
    * Plot title
    * Plot x and y axis titles
    * Figure size
    * Default save path

'''
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = None
    
    def analysis_obj(self):
        try:
            with open(self.config_file_path, 'r') as file:
                self.config = yaml.safe_load(file)
            configtable = {}
            configtable.update(self.config)
            logging.info(f'Successfully loaded {self.config}')
        except FileNotFoundError:
            print(f"Error: Config file '{self.config_file_path}' not found.")
            logging.error(f"Error: Config file '{self.config_file_path}' not found.")
        except yaml.YAMLError as e:
            print(f"Error: Failed to load config file. {e}")
            logging.error(f"Error: Failed to load config file. {e}")
        assert type(self.config_file_path) == str, f"Path, {self.config_file_path} must be a string"
            
config1 = Analysis('secrets.yml')
configfile = config1.analysis_obj()




def load_data()
''' Retrieve data from the GitHub API

This function makes an HTTPS request to the GitHub API and retrieves your selected data. The data is
stored in the Analysis object.

Parameters
----------
None

Returns
-------
None

'''

compute_analysis() -> Any
'''Analyze previously-loaded data.

This function runs an analytical measure of your choice (mean, median, linear regression, etc...)
and returns the data in a format of your choice.

Parameters
----------
None

Returns
-------
analysis_output : Any

'''
def profile (x)
    mean = x.mean()
    mediam = x.median()
    return 

def notify_done(message: str) -> None
''' Notify the user that analysis is complete.

Send a notification to the user through the ntfy.sh webpush service.

Parameters
----------
message : str
  Text of the notification to send

Returns
-------
None

'''


plot_data(save_path:Optional[str] = None) -> matplotlib.Figure
''' Analyze and plot data

Generates a plot, display it to screen, and save it to the path in the parameter `save_path`, or 
the path from the configuration file if not specified.

Parameters
----------
save_path : str, optional
    Save path for the generated figure

Returns
-------
fig : matplotlib.Figure

'''



