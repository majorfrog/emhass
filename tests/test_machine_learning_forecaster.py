#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch
import pathlib
import json
import yaml
import copy
import pickle
import pandas as pd

from skforecast.ForecasterAutoreg import ForecasterAutoreg

from emhass.command_line import set_input_data_dict
from emhass.retrieve_hass import retrieve_hass
from emhass.machine_learning_forecaster import mlforecaster
from emhass import utils

# the root folder
root = str(utils.get_root(__file__, num_parent=2))
# create logger
logger, ch = utils.get_logger(__name__, root, save_to_file=False)

class TestMLForecaster(unittest.TestCase):
    
    @staticmethod
    def get_test_params():
        with open(root+'/config_emhass.yaml', 'r') as file:
            params = yaml.load(file, Loader=yaml.FullLoader)
        params.update({
            'params_secrets': {
                'hass_url': 'http://supervisor/core/api',
                'long_lived_token': '${SUPERVISOR_TOKEN}',
                'time_zone': 'Europe/Paris',
                'lat': 45.83,
                'lon': 6.86,
                'alt': 8000.0
            }
            })
        return params

    def setUp(self):
        params = TestMLForecaster.get_test_params()
        params_json = json.dumps(params)
        config_path = pathlib.Path(root+'/config_emhass.yaml')
        base_path = str(config_path.parent)
        costfun = 'profit'
        action = 'forecast-model-fit' # fit, predict and tune methods
        params = copy.deepcopy(json.loads(params_json))
        runtimeparams = {
            "days_to_retrieve": 20,
            "model_type": "load_forecast",
            "var_model": "sensor.power_load_no_var_loads",
            "sklearn_model": "KNeighborsRegressor",
            "num_lags": 48
        }
        runtimeparams_json = json.dumps(runtimeparams)
        params['passed_data'] = runtimeparams
        params['optim_conf'][8]['load_forecast_method'] = 'skforecast'
        params_json = json.dumps(params)
        self.input_data_dict = set_input_data_dict(config_path, base_path, costfun, params_json, runtimeparams_json, 
                                                   action, logger, get_data_from_file=True)
        data = copy.deepcopy(self.input_data_dict['df_input_data'])
        model_type = self.input_data_dict['params']['passed_data']['model_type']
        var_model = self.input_data_dict['params']['passed_data']['var_model']
        sklearn_model = self.input_data_dict['params']['passed_data']['sklearn_model']
        num_lags = self.input_data_dict['params']['passed_data']['num_lags']
        self.mlf = mlforecaster(data, model_type, var_model, sklearn_model, num_lags, root, logger)
        
        get_data_from_file = True
        params = None
        self.retrieve_hass_conf, self.optim_conf, _ = utils.get_yaml_parse(pathlib.Path(root+'/config_emhass.yaml'), use_secrets=False)
        self.rh = retrieve_hass(self.retrieve_hass_conf['hass_url'], self.retrieve_hass_conf['long_lived_token'], 
                                self.retrieve_hass_conf['freq'], self.retrieve_hass_conf['time_zone'],
                                params, root, logger, get_data_from_file=get_data_from_file)
        with open(pathlib.Path(root+'/data/test_df_final.pkl'), 'rb') as inp:
            self.rh.df_final, self.days_list, self.var_list = pickle.load(inp)
        
    def test_fit(self):
        df_pred, df_pred_backtest = self.mlf.fit()
        self.assertIsInstance(self.mlf.forecaster, ForecasterAutoreg)
        self.assertIsInstance(df_pred, pd.DataFrame)
        self.assertTrue(df_pred_backtest == None)
        # Refit with backtest evaluation
        df_pred, df_pred_backtest = self.mlf.fit(perform_backtest=True)
        self.assertIsInstance(self.mlf.forecaster, ForecasterAutoreg)
        self.assertIsInstance(df_pred, pd.DataFrame)
        self.assertIsInstance(df_pred_backtest, pd.DataFrame)
        
    def test_predict(self):
        self.mlf.fit()
        predictions = self.mlf.predict()
        self.assertIsInstance(predictions, pd.Series)
        self.assertTrue(predictions.isnull().sum().sum() == 0)
        # Test predict in production env using last_window
        data_tmp = copy.deepcopy(self.rh.df_final)[[self.mlf.var_model]]
        data_last_window = data_tmp[data_tmp.index[-1] - pd.offsets.Day(2):]
        predictions = self.mlf.predict(data_last_window)
        self.assertIsInstance(predictions, pd.Series)
        self.assertTrue(predictions.isnull().sum().sum() == 0)
        # Emulate predict on optimized forecaster
        self.mlf.is_tuned = True
        self.mlf.lags_opt = 48
        self.mlf.fit()
        predictions = self.mlf.predict()
        self.assertIsInstance(predictions, pd.Series)
        self.assertTrue(predictions.isnull().sum().sum() == 0)
        
    def test_tune(self):
        self.mlf.fit()
        df_pred_optim = self.mlf.tune(debug=True)
        self.assertIsInstance(df_pred_optim, pd.DataFrame)
        self.assertTrue(self.mlf.is_tuned == True)
        # Test LinearRegression
        data = copy.deepcopy(self.input_data_dict['df_input_data'])
        model_type = self.input_data_dict['params']['passed_data']['model_type']
        var_model = self.input_data_dict['params']['passed_data']['var_model']
        sklearn_model = 'LinearRegression'
        num_lags = self.input_data_dict['params']['passed_data']['num_lags']
        self.mlf = mlforecaster(data, model_type, var_model, sklearn_model, num_lags, root, logger)
        self.mlf.fit()
        df_pred_optim = self.mlf.tune(debug=True)
        self.assertIsInstance(df_pred_optim, pd.DataFrame)
        self.assertTrue(self.mlf.is_tuned == True)
        # Test ElasticNet
        data = copy.deepcopy(self.input_data_dict['df_input_data'])
        model_type = self.input_data_dict['params']['passed_data']['model_type']
        var_model = self.input_data_dict['params']['passed_data']['var_model']
        sklearn_model = 'ElasticNet'
        num_lags = self.input_data_dict['params']['passed_data']['num_lags']
        self.mlf = mlforecaster(data, model_type, var_model, sklearn_model, num_lags, root, logger)
        self.mlf.fit()
        df_pred_optim = self.mlf.tune(debug=True)
        self.assertIsInstance(df_pred_optim, pd.DataFrame)
        self.assertTrue(self.mlf.is_tuned == True)
        
        
if __name__ == '__main__':
    unittest.main()
    ch.close()
    logger.removeHandler(ch)
