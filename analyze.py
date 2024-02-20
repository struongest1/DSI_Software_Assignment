import pandas as pd
import logging
import argparse
import yaml
import os
import requests
import matplotlib.pyplot as plt
import requests
import matplotlib.ticker as tick



logging.basicConfig(
    handlers=(logging.StreamHandler(), logging.FileHandler('analysis.log')), 
    level=logging.INFO,
    )

# class yourteamrepo.Analysis.Analysis(analysis_config:str)
class Analysis():

    '''Load config file into an Analysis object

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
         
    
    def load_data (self):
        ''' 
        I downloaded the data from Kaggle using the API then saved the 
        file on github for the rest of the analysis Retrieve data from github using config file
        Parameters:
        link to csv file from config file
        Returns:
        pandas dataframe of csv file from github
        '''
        dataset_url = self.config['data']
        try:
            self.dataset = pd.read_csv(dataset_url)
            logging.info(f'Successfully loaded {dataset_url}')
        except Exception as e:
            logging.error('Error loading dataset', exc_info=e)
            raise e    
        
    def compute_analysis(self):
        # Get a list of the 10 counties with the leaast amount of forest cover
        '''
        This function either selects the bottom 10 forest cover trees
        Parameters
        None

        Returns
        analysis_output : df ''' 
        self.result = self.dataset.sort_values('2021', ascending=True).head(10)
        return self.result
       

    def notify_done(self, message: str) -> None:
        ''' Notify the user that analysis is complete.
        Send a notification to the user through the ntfy.sh webpush service.
        Parameters
        ----------
        Message : str
        Text of the notification to send

        Returns
        -------
        None
        '''
        requests.post(
        self.config['ntfy']['url'],
        data=message.encode('utf-8'),
        headers={'Title': self.config['ntfy']['title']})


    def plot_data(self):
        ''' Analyze and plot data

        Generates a plot, display it to screen
        Parameters
        ----------
        Returns
        -------
        fig : matplotlib.Figure

        '''
        bar_fig, bar_ax = plt.subplots()
        bar_ax.barh(self.result[self.config['plot_config']['xvar']], self.result['2021'], color="red")
        bar_ax.set_title(self.config['plot_config']['title'], fontsize='12')
        bar_ax.set_xlabel(self.config['plot_config']['ylabel'], fontsize=self.config['plot_config']['Font_size'])
        bar_ax.set_ylabel(self.config['plot_config']['xlabel'], fontsize=self.config['plot_config']['Font_size'])
        return
    






