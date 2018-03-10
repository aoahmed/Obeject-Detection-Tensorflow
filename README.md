# Obeject-Detection-Tensorflow
Retrain Inception Model by your own dataset and with bounding-box output.


1 - Image handling and bounding boxes :

To have bounding boxes as output during the detection process we have to make the model find bounding boxes of a given object in a set of images. So how to create the bounding box around an object ? This is a link https://github.com/tzutalin/labelImg to make BB and export them as .xml files.
 Now we have images and xml files as dataset.
 
 
 
 2 - Convert xml to csv file :
 
 We're going to convert all the xml files in [test or train] directory (which contain both of them all the classes, in my case here : Bottle , Cell Phone and Person) into one CSV file with the script "xml_to_csv.py"
 
 
 
 3 - Convert csv files to tfrecord :
 
 To generate a TFrecord (a binary file) we need both csv file and the path for the images we used in csv file. So we will use the script : "generate_tfrecord.py"
 
 
 4 - Use TFrecords to generate your model :
 
 We will not cover this in this repository because it's shown by Tensorflow tutorials in which you will use this script : https://github.com/tensorflow/models/blob/master/research/object_detection/train.py to train your model.
