<<<<<<< HEAD
# GamePlayStyle Classifier (DCML Project)

## Description
The GamePlayStyle Classifier is a Python program designed to predict whether the user is playing a video game based
on their mouse and keyboard actions. By analyzing the patterns of mouse movements and keyboard inputs, the program
employs machine learning techniques to distinguish between different play styles.

## Installation
1. Clone the repository to your local machine: git clone https://github.com/pippodima/DCML_Project/tree/master
2. navigate to the project directory
3. install the required dependencies using pip (see `requirements.txt` for full list)

## Usage
To use the GamePlayStyle Classifier, follow these steps:

1. Train the model with your own data or use the pre-trained model provided.
2. Run the program and provide input data (mouse and keyboard actions) for prediction.
3. Receive predictions indicating whether the user is playing a video game.

## How to monitor your data and use the progam (more details)
To fit the model to your own play style first you need to monitor (at least) a couple of games.
1. Go to `main.py` and set `monitor_only` variable to `True`. Now if you run main, a file will be created in your directory
   (monitored_values.csv) where there are all the information needed
2. after you have monitored a couple of games of your play style and other games of another style (another person) you can now
create the dataset. go to ML/prepareDataset and put the names of the games file(.csv) and run the script
3. go to ML/supervisedModelComparison change the paths to save the models that are trained on your dataset
4. go to main again and change the `monitor_only` variable to `False` and adjust the paths before running
5. now it should print in your console `[0]` or `[1]` if the player is normal or anomaly. If it reads anomaly for more than
2.5 seconds it will play a beep sound until it become again a `[0]`
=======
# go to master branch
>>>>>>> 8678f370659d3acfef5cbfb7b38e3b3324c21e96
