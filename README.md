# Hyperparameter Model Optimizaiton using NNI

### Requirments
- torch 
- nni
- torchvision

### How to run the code

Running on different configuaration and hyperparameter optimizer technique

- python main.py tpe 1
- python main.py tpe 2
- python main.py random 1
- python main.py random 2
- python main.py hyperband 1
- python main.py hyperband 2

The results will be stored in nni-experiments folder.

### Project Learnings

Optimal Loss Comparison Table

<img width="683" alt="Screen Shot 2022-10-22 at 3 09 35 PM" src="https://user-images.githubusercontent.com/22122136/197358391-8c217b82-a473-404f-af18-97c738b188b9.png">

- As we can see that the experiment execution time varies with each tuner-configuration combination. It is generally observed that the configuration 2 is faster than configuration 1 for all tuners because we have set advanced configurations in configuration 2 which help decrease execution time for the experiments.
- Another important factor to be considered while HPO is the test set loss for the model. We can generally see a similar test set loss observed in most of the experiments and this can conclude that with the given set training, testing data set and model complexity, all HPO Tuners perform almost the same. This can change when the complexity of the model increases or the dataset changes.
- We can also notice slight increases in the loss encountered in the experiments with configuration 2 which decrease the execution time used by experiments which is a valid tradeoff which can be considered in many real life situations. This tradeoff is quite significant in the Hyperband Tuner.
- Finally, we observe that the least loss is encountered with the TPE Tuner with configuration 1 which can be chosen as optimal if loss optimization is extremely important to the use case. Alternatively, TPE Tuner with configuration 2 can be considered optimal as it gives a good tradeoff between test loss and time taken.
