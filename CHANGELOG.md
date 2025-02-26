# Changelog

## [0.4.12] - 2023-06-03
### Improvement
- Added forecasts for unit_prod_price and unit_load_cost.
- Improved documentation.
### Fix
- Bump skforecast from 0.8.0 to 0.8.1

## [0.4.11] - 2023-05-27
### Improvement
- Adding new constraints to limit the dynamics (kW/sec) of deferrable loads and battery power. The LP formulation works correctly and a work should be done on integrating the user input parameters to control this functionality.
- Added new constraint to avoid battery discharging to the grid.
- Added possibility to set the logging level.
### Fix
- Bumped version of skforecast from 0.6.0 to 0.8.1. Doing this mainly implies changing how the exogenous data is passed to fit and predict methods.
- Fixed wrong path for csv files when using load cost and prod price forecasts.

## [0.4.10] - 2023-05-21
### Fix
- Fixed wrong name of new cost sensor.
- Fixed units of measurements of costs to €/kWh.
- Added color sequence to plot figures, now avery line should be plotted with a different color.

## [0.4.9] - 2023-05-20
### Fix
- Updated default value for total number of days for ML model training.
- Added publish of unit_load_cost and unit_prod_price sensors.
- Improved docs intro.
- Bump myst-parser from 0.18.1 to 1.0.0

## [0.4.8] - 2023-03-17
### Fix
- Fixed to correct index length for ML forecaster prediction series.

## [0.4.7] - 2023-03-16
### Fix
- Fixed wrong column name for var_load when using predict with ML forecaster.

## [0.4.6] - 2023-03-16
### Fix
- Fixed wrong path for saved ML forecaster model.

## [0.4.5] - 2023-03-10
### Fix
- Fixed default behavior for passed data.
- Added a new graph for tune results.

## [0.4.4] - 2023-03-09
### Fix
- Added missing possibility to set the method for load forecast to 'mlforecaster'.
- Fixed logging formatting.

## [0.4.3] - 2023-03-09
### Fix
- Fixed logging.
- Fixed missing module on docker standalone mode.

## [0.4.2] - 2023-03-07
### Fix
- Fixed handling of default passed params.

## [0.4.1] - 2023-03-06
### Improvement
- Improved the documentation and the in-code docstrings.
- Added the possibility to save the optimized model after a tuning routine.
- Added the possibility to publish predict results to a Home Assistant sensor.
- Added the possibility to provide custom entity_id, unit_of_measurement and friendly_name for each published data.

## [0.4.0] - 2023-03-06
### Improvement
- A brand new load forecast module and more... The new forecast module can actually be used to foreast any Home Assistant variable. The API provides fit, predict and tune methods. By the default it provides a more efficient way to forecast the power load consumption. It is based on the skforecast module that uses scikit-learn regression models considering auto-regression lags as features. The hyperparameter optimization is proposed using bayesian optimization from the optuna module.
- A new documentation section covering the new forecast module.
### Fix
- Fixed Solar.Forecast issues with lists of parameters.
- Fixed latex equations rendering on documentation, dropped Mathjax.
- Refactored images in documentation, now using only SVG for plotly figures.
- Bumped requirements to latest non-conflicting versions.

## [0.3.36] - 2023-01-31
### Fix
- Fixed message handling from request module.

## [0.3.35] - 2023-01-31
### Fix
- Fixed access to injection_dict for the first time that emhass is used.

## [0.3.34] - 2023-01-30
### Fix
- Fixed bugs with paths again, now using the official pathlib everywhere.

## [0.3.32] - 2023-01-30
### Fix
- Fixed bugs on handling data folder name.
- Improved warning messages when passing list of values with items detected as non digits.

## [0.3.29] - 2023-01-28
### Improvement
- Implemented data storage to survive add-on restarts.

## [0.3.25] - 2023-01-27
### Fix
- Fixed dependencies, uniform working versions of Numpy, Pandas and Tables.

## [0.3.24] - 2023-01-27
### Fix
- Fixed dependencies, rolled back to older fixed Numpy and Pandas versions.

## [0.3.23] - 2023-01-26
### Fix
- Fixed missing integration of additional `set_nocharge_from_grid` in the web server.
- Improved the documentation.

## [0.3.22] - 2023-01-26
### Improvement
- Improved unittest for mock get requests.
- Improved coverage.
### Fix
- Code works even if no battery data is configured.
- Added more explicit logging error message in the case of no data retrieved from Home Assistant.

## [0.3.21] - 2022-10-21
### Fix
- Fixed docstrings
- Added github worflows for coverage and automatic package compiling.
- Fixing interpolation for Forecast.Solar data.

## [0.3.20] - 2022-10-05
### Improvement
- Added more detailed examples to the forecast module documentation.
- Improved handling of datatime indexes in DataFrames on forecast module.
- Added warning messages if passed list values contains non numeric items.
- Added missing unittests for forecast module with request.get dependencies using MagicMock.
- Added the Solar.Forecast method.

## [0.3.19] - 2022-09-14
### Fix
- Updated default values for a working LP solver.
- Removed option to provide a custom web ui url.
- Added extra runtime parameters to use solcast PV forecast.

## [0.3.18] - 2022-08-27
### Improvement
- Improving documentation, added more information on forecast page.
- Added support for SolCast PV production forecasts. 
- Added possibility to pass some optimization parameters at runtime.
- Added some unittest for passing data as list testing.
### Fix
- Fixed small bug on webserver using pandas sum function for non numeric data. This was throwing the following message: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated.

## [0.3.17] - 2022-06-12
### Fix
- Fixed wrong variables names for mixed forecasts.
- Fixed handling of load sensor name in command line setup function.

## [0.3.16] - 2022-06-10
### Improvement
- Improving documentation, added "what is this" section and added some infographics.
- Added new forecasts methods chapter in documentation.
- Added publish of sensors for p_grid_forecast & total value of cost function.
- Implemented now/current value forecast correction when using MPC.

## [0.3.15] - 2022-06-06
### Fix
- Fixed small bug with wrong DF variable name in web server.

## [0.3.14] - 2022-06-05
### Improvement
- Added one more table to the webui showing the cost totals.
### Fix
- Fixed wrong type error when serializing numpy ints. Converted ints to Python type.

## [0.3.13] - 2022-05-20
### Fix
- Fix wrong default value implementation for solver params.

## [0.3.12] - 2022-05-20
### Improvement
- Added support to provide solver name and path as parameters in the configuration file.

## [0.3.11] - 2022-05-23
### Fix
- Fixed unittests not passing.

## [0.3.10] - 2022-05-23
### Improvement
- Added data as attributes for forecasts (PV and load), deferrable loads and battery: power+SOC.
- Improved the graph in the webserver, now using subplots.
- Rearranged vertical space in index.html template.
### Fix
- Added threads option on waitress to possibly improve queue problem.

## [0.3.9] - 2022-05-19
### Improvement
- Improved publish data logging.
- Round published data.
- Attributes to forecasts published data.
- Improved centering html on small devices.
- Improved handling of closest index when publishing data.
### Fix
- Fixed problem with csv filenames, was using only filename specific to dayahead optimization.
- Fixed data list handling for load cost and prod price forecasts.
- Fixed publish data dictionary to contain only data from correct entity_id.
- May have solved double log lines.

## [0.3.8] - 2022-05-17
### Fix
- Still fixing issues when passing csv files and lists.

## [0.3.7] - 2022-05-17
### Fix
- Fixed None weather df issue when passing lists.
- Improved command line unittests.

## [0.3.6] - 2022-05-17
### Fix
- Fixed wrong handling of list values when preparing data for MPC.

## [0.3.5] - 2022-05-16
### Fix
- Fixed wrong mpc pred horizon param.

## [0.3.4] - 2022-05-16
### Fix
- Fixed unloaded json object problem.
- Added static style.css as package_data.

## [0.3.3] - 2022-05-15
### Fix
- Fixed dealing with bool and argparse module.
- Added the templates as package_data so that they can be found by jinja2 PackageLoader.

## [0.3.2] - 2022-05-13
### Fix
- Fixed command_line and utils problem when params is None.

## [0.3.1] - 2022-05-13
### Fix
- Fixed template rendering problems.

## [0.3.0] - 2022-05-12
### Improvement
- Improved the command line setup function to perform the correct amount calls as needed by each action.
- Added a new naive model predictive control function.
- Added runtime parameter option for better code order.
- Moved treatment of runtime parameters from the add-on to the core emhass module. This adds more clarity to the code and also was needed when passing runtime parameters to emhass in standalone mode.
- Added add-on paramter to command line to define if launching emhass from add-on or in standalone mode.
- Added new testing file for command_line.
- Added a webserver. Moved the webserver from the add-on to the core emhass module.
- Added a WSGI production server for flask using waitress.
- Added a Dockerfile and procedure to run emhass in standalone mode.
- Updated the documentation.

## [0.2.14] - 2022-05-05
### Improvement
- Added more info on publish data errors when not key found. This error may mean that the optimization task may need to be relaunched or it did not converged to a solution.
- Added better info to the configuration documentation when integrating PV module and inverter models from PVLib database. An underscore _ character should be added inplace of each special character.
### Fix
- Fixed missing timeStep product for correct deferrable load total energies.

## [0.2.13] - 2022-05-01
### Improvement
- Added support to pass list of PV plant parameters. This will enable to simulate mixed orientation systems, for example one east-facing array (azimuth=90) and one west-facing array (azimuth=270).
### Fix
- Fixed issue computing correct final cost values.

## [0.2.12] - 2022-04-28
### Improvement
- Added config parameter to consider that all PV power is injected to the grid.

## [0.2.11] - 2022-04-28
### Fix
- Fixed wrong handling of DateTimeIndex when dealing with forecast method for list of values and csv read.

## [0.2.10] - 2022-04-26
### Fix
- Fixed faulty forecast method for list of values and csv read.

## [0.2.9] - 2022-04-21
### Fix
- Fixed get_loc deprecation warning using now get_indexer pandas method. Improved selection of closest index.

## [0.2.8] - 2022-04-18
### Fix
- Fixed if sentence to correctly use the supervisor API for publish data.
- Fixing a error computing the nearest index of DataFrame. Using a try/catch strategy to use nearest method as a backup.

## [0.2.7] - 2022-04-18
### Fix
- Fixing a fatal error where the publish data function will never reach the savec csv file as the default filename is not equal to the expected filename in publish_data.

## [0.2.6] - 2022-04-16
### Improvement
- Improved handling of errors concerning solver issues with Pulp. Added support for `glpk` solver. For now just using a try/catch strategy but should update to solver passed as a parameter to EMHASS.

## [0.2.5] - 2022-04-12
### Fix
- Fixed missing numpy import in utils.

## [0.2.4] - 2022-04-12
### Fix
- Fixed missing command to retrieve PV power forecast when using list of values.
- Updated handling of freq definition to a pandas index.

## [0.2.3] - 2022-03-29
### Improvement
- Improved support for the new add-on and direct communication via the supervisor.
- The CLI now can return the version using the --version argument.
- Improved comments in forecast class.
### Added
- Added unittest for csv method for weather forecast.
- Added support for passing lists of values to all forecasting methods.
### Fix
- Removed dependency from PVLib Forecast class, as it has been marked as deprecated.
- Fixed failing docs builds due to uncompatible jinja2 an markupsafe versions.

## [0.2.2] - 2022-03-05
### Added
- Added a new input data file using pickle for tests.
- Added support to select if the logger should save to a file or not.
- Added CI workflow using github actions.
### Breaking changes
- Changed package usage of configuration file path, now the user must provide the complete path including the yaml file itself.
- Changed the names of the configuration and secrets yaml files. These changes will avoid compatibility issues when using hass add-ons.

## [0.2.1] - 2021-12-22
### Fixed
- Cleaned unittest implementation
### Added
- Added support to choose the methods for weather and load forecast from configuration file.
- Added new load cost and power production price forecasts, mainly allowing the user to load a CSV file with their own forecast.

## [0.2.0] - 2021-10-14
### Fixed
- Fixed tests to pass with latest changes on passing path and logger arguments.
- Updated requirements for PVLib and Protobuf.
- Removed unnecessary use of abstract classes.
- Fixed test_optimization bad setup.
- Fixed logger integration in classes
- Updated documentation
### Added
- Implemented typing for compatibility with Python4
- Implemented different types of cost functions

## [0.1.5] - 2021-09-22
### Fixed
- Fix a recurrent previous bug when using get_loc. The correct default behavior when using get_loc is changed from backfill to ffill.

## [0.1.4] - 2021-09-18
### Fixed
- Fixed a bug when publish-data and reading the CSV file, the index was not correctly defined, so there was a bug when applying pandas get_loc.
### Added
- Added a global requirements.txt file for pip install.

## [0.1.3] - 2021-09-17
### Fixed
- Fixed packaging and configuration for readthedocs.

## [0.1.2] - 2021-09-17
### Fixed
- Modified the cost function equation signs for more clarity. Now the LP is fixed to maximize a profit given by the revenues from selling PV to the grind minus the energy cost of consumed energy.
- Fixed a deprecation warning from PVLib when retrieving results from the ModelChain object. Now using modelchain.results.ac.

## [0.1.1] - 2021-09-17
### Fixed
- Fixed sign error in cost function.
- Change publish_data get_loc behavior from nearest to backfill.
- Changed and updated behavior of the logger. It is constructed and integrated directly in the main function of the command_line.py file. It now writes to a log file by default.
- Fixed some typos and errors in the documentation.

## [0.1.0] - 2021-09-12
### Added
- Added the first public repository for this project.

[0.1.0]: https://github.com/davidusb-geek/emhass/releases/tag/v0.1.0
[0.1.1]: https://github.com/davidusb-geek/emhass/releases/tag/v0.1.1
[0.1.2]: https://github.com/davidusb-geek/emhass/releases/tag/v0.1.2
[0.1.3]: https://github.com/davidusb-geek/emhass/releases/tag/v0.1.3
[0.1.4]: https://github.com/davidusb-geek/emhass/releases/tag/v0.1.4
[0.1.5]: https://github.com/davidusb-geek/emhass/releases/tag/v0.1.5
[0.2.0]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.0
[0.2.1]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.1
[0.2.2]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.2
[0.2.3]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.3
[0.2.4]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.4
[0.2.5]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.5
[0.2.6]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.6
[0.2.7]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.7
[0.2.8]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.8
[0.2.9]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.9
[0.2.10]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.10
[0.2.11]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.11
[0.2.12]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.12
[0.2.13]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.13
[0.2.14]: https://github.com/davidusb-geek/emhass/releases/tag/v0.2.14
[0.3.0]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.0
[0.3.6]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.6
[0.3.8]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.8
[0.3.9]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.9
[0.3.11]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.11
[0.3.13]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.13
[0.3.14]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.14
[0.3.15]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.15
[0.3.16]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.16
[0.3.17]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.17
[0.3.18]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.18
[0.3.19]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.19
[0.3.20]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.20
[0.3.21]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.21
[0.3.22]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.22
[0.3.23]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.23
[0.3.24]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.24
[0.3.25]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.25
[0.3.29]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.29
[0.3.32]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.32
[0.3.34]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.34
[0.3.35]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.35
[0.3.36]: https://github.com/davidusb-geek/emhass/releases/tag/v0.3.36
[0.4.0]: https://github.com/davidusb-geek/emhass/releases/tag/v0.4.0
[0.4.1]: https://github.com/davidusb-geek/emhass/releases/tag/v0.4.1
[0.4.2]: https://github.com/davidusb-geek/emhass/releases/tag/v0.4.2
[0.4.3]: https://github.com/davidusb-geek/emhass/releases/tag/v0.4.3
[0.4.4]: https://github.com/davidusb-geek/emhass/releases/tag/v0.4.4
[0.4.5]: https://github.com/davidusb-geek/emhass/releases/tag/v0.4.5
[0.4.6]: https://github.com/davidusb-geek/emhass/releases/tag/v0.4.6

# Notes
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
