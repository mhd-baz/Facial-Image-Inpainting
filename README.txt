$$ ATTENTION: TO USE ALL THE JUPYTIER NOTEBOOK YOU NEED TO MEET TO THE REQUIRMENTS FILE
                (The requirements file is not really accurate because there is in it libraries that are not used in the notebooks
                and this because we forgot to use a specific python environment for this project, so we used our main python environment)


#------------------------------------------------------
BRIEF DESCRIPTION OF THE JUPYTER NOTEBOOK AND PYTHON FILE

There are 2 ipynb file and 1 python file:
    - The python file is used to corupt the face images.
    - The main.ipynb is our main program that implements the proposed model in pytorch framework.
    - The baseline.ipynb is our baseline comparision model and is in tensorflow framework.


#------------------------------------------------------
EXPLICATION ON HOW TO USE main.ipynb NOTEBOOK

Both classifier have the same structure, they are divided in 8 sections:
    0) Librairies Importation: it's mandatory to import the libraris in order to correctly use the rest of the cells
    1) Custom Classes For Neural Networks: To define the custom classes that we use in our neural networks
    2) Model Architecture: The model that we will use to fit the data
    3) Loss function: The loss function that we will use to train the model
    4) Metrics: To evaluate the model  
    5) Data Importation: To import the data and pre-process it
    6) Training: To train the model (in this section there is also the part where we save and load a model)


For the 5th and 6th parts, the first cell is a cell where you can fix the hyperparamters.
This first cells are the only one where modification are allowed for a guarented running. Each hyperparamter is described and have explicit names.
Some additional comments are also there in order to give more explications on how to use the hyperparamters or the next cells.

$$ IMPORTANT:   You have to download the data linked to each classifier in order to import the data.
                You also have to corupt the images using the pythons scripts.
                You could find the links to download the data in the subfolder data.
#------------------------------------------------------
EXPLICATION ON HOW TO USE THE baseline.ipynb NOTEBOOK

Both classifier have the same structure, they are divided in 8 sections:
    0) Librairies Importation: it's mandatory to import the libraris in order to correctly use the rest of the cells
    1) Data Importation: To import the data, visualize, and pre-process it
    2) Custom Loss function: The loss function that we will use to train the model
    3) Metrics: To evaluate model performance during training
    4) Model Building: The model that we will use to fit the data
    5) Training: To train the model (in this section there is also the part where we save and load a model)
    6) Evaluation: Highlight the performance of the full model on new data
  

For the 4th and 5th part, the first cell is a cell where you can fix the hyperparamters.
This first cells are the only one where modification are allowed for a guarented running. Each hyperparamter is described and have explicit names.
Some additional comments are also there in order to give more explications on how to use the hyperparamters or the next cells.

$$ IMPORTANT:   You have to download the data linked to each classifier in order to import the data.
                You also have to corupt the images using the pythons scripts.
                You could find the links to download the data in the subfolder data.
		Use the plot_result(n) function to check the prediction of any of the 150 images in the test set (idx:0-149)

#------------------------------------------------------
EXPLINATION ON HOW TO USE THE PYTHON SCRIPT

Ensure you have the data downloaded on your local machine or have the directories manually structured as depicted below.
Ensure paths to downloaded source images and masks are valid.
Open script and set paths to you source, destinations, and mask folders
Set the dimentions of the images you would like to produce
Set the size of the training set

Run script with 
	$python fakepath/corrupt_img

$$ IMPORTANT:   The directories must be manually created in the following format:

		-rootfolder
		--------corrupt1024x1024
		---------------train
		---------------test
		--------source1024x1024
		---------------train
		---------------test
		--------masks

		Masks form data are defualt in 512x512 format (can be resized within script)
		Images used are in 1024x1024 and 512x512 format
		The image filenames are the same across masks and source images(masks and images are linked via filename)