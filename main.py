from nni.experiment import Experiment
import sys

if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        hpo=sys.argv[1]
        config = sys.argv[2]
        search_space = {
            'features1': {'_type': 'choice', '_value': [300, 400, 500, 600]},
            'features2': {'_type': 'choice', '_value': [10, 20, 30, 40]},
            'lr': {'_type': 'loguniform', '_value': [0.0001, 0.1]},
            'epsilon': {'_type': 'choice', '_value': [1e-06, 1e-07]},
        }

        experiment = Experiment('local')

        experiment.config.trial_command = 'python3 model.py'
        experiment.config.trial_code_directory = '.'

        experiment.config.search_space = search_space
        
        if hpo == 'tpe' and config == 1:

            experiment.config.tuner.name = 'TPE'
            experiment.config.tuner.class_args={
                'optimize_mode': 'minimize'
            }
        if hpo == 'tpe' and config == 2:
    
            experiment.config.tuner.name = 'TPE'
            experiment.config.tuner.class_args ={
                'optimize_mode': 'minimize',
                'tpe_args':{ 
                    'n_startup_jobs': 3
                }
            }
        elif hpo == 'hyperband' and config == 1:
    
            experiment.config.tuner.name = 'Hyperband'
            experiment.config.tuner.class_args = {
                'optimize_mode': 'maximize',
                'R': 60,
                'eta': 3
            }
        elif hpo == 'hyperband' and config == 2:
    
            experiment.config.tuner.name = 'Hyperband'
            experiment.config.tuner.class_args = {
                'optimize_mode': 'maximize',
                'R': 100,
                'eta': 5,
                'exec_mode' : 'parallelism'
                
            }   
        elif hpo == 'random' and config == 1:
    
            experiment.config.tuner.name = 'Random'
            experiment.config.tuner.class_args={
                'optimize_mode': 'minimize',
                'seed' : 100
            }
        
        elif hpo == 'random' and config == 2:
        
            experiment.config.tuner.name = 'Random'
            experiment.config.tuner.class_args={
                'optimize_mode': 'minimize',
                'seed' : 500
            }
        
        experiment.config.max_trial_number = 10
        experiment.config.trial_concurrency = 1

        experiment.run(8091)

        experiment.stop()
                                                                                                                                                                                                    
                                                                                                                                                                                                    