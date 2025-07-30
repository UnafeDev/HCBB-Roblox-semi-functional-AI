\\ Files and their uses :

best.pt -- pre trained AI file

Trainer.py -- Used to train the ai and output the .pt file (PreTrained)
YOLO.py -- The actual AI
screenshot.py -- takes screenshots every few milleseconds that can be used for annotation

RAWINPUTS.cpp -- A C++ file that reads off of coords.txt to dynamically move the cursor

dataset.yaml -- used to direct "trainer.py" over to the dataset
	note : in the dataset.yaml file, make sure to change the dataset directory to your own

coords.txt -- a special text file that has the coordinates to the object (baseball in this case) which ïs read by “RAWINPUTS.cpp”

\\ What are the .pt files?

these are files that have the AI model, basically the file that holds the AI together

\\ How does training work?

to properly train the AI you will need to annotate the images saved in the folder "screenshots"
	- I'd reccommend using a website like roboflow to annotate the images

when you have your annotated images, go into the folder and copy both “images” and “labels” folder then you can paste them into the
	\dataset\train folder and the
	\dataset\val folder

\\ Note
DO NOT CHANGE THE LAYOUT OF THE DATASET FOLDER!!!


