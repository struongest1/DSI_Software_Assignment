import pandas as pd
import logging
import argparse
import yaml
import os
import requests
import matplotlib.pyplot as plt
import requests



logging.basicConfig(
    handlers=(logging.StreamHandler(), logging.FileHandler('uci_iris.log')), 
    level=logging.INFO,
    )



# class yourteamrepo.Analysis.Analysis(analysis_config:str)
class Analysis:
''' Load config file into an Analysis object

Load system-wide configuration from `config.yml`, user configuration from
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
        #     configtable = {}
        #     configtable.update(self.config)
        #     logging.info(f'Successfully loaded {self.config}')
        except FileNotFoundError:
            print(f"Error: Config file '{self.config_file_path}' not found.")
            logging.error(f"Error: Config file '{self.config_file_path}' not found.")
        except yaml.YAMLError as e:
            print(f"Error: Failed to load config file. {e}")
            logging.error(f"Error: Failed to load config file. {e}")
        assert type(self.config_file_path) == str, f"Path, {self.config_file_path} must be a string"
        return self.config    
config1 = Analysis('user_config.yml')
configfile = config1.analysis_obj()



''' 
Retrieve data from github using config file

Parameters:
link to csv file from config file


Returns:
pandas dataframe of csv file from github
'''
dataset_url = configfile['data']

try:
    dataset = pd.read_csv(dataset_url)
    logging.info(f'Successfully loaded {dataset_url}')
except Exception as e:
    logging.error('Error loading dataset', exc_info=e)
    raise e


load_data(configfile['data'])



#compute_analysis() -> Any
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


#send notification for completed analysis
def notify_done(message: str) -> None:
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
    requests.post(
    configfile['ntfy']['url'],
    data=message.encode('utf-8'),
    headers={'Title': configfile['ntfy']['title']})
    

notify_done('Jimmy Assignment Complete')


#Plot data analysis
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

