# singlecabac
This code is used to analyse the data of the singleCABAC test bench.
The original data are written in xml format (this format was chosen because it was simpler in my Labview code).
The files are saved in the following structure: /chipnumber/signalnumber/nameoffile.xml


When the data are analysed for the first time, one needs to run a script to add a line at the beginning and the end of the xml files.
To do so a script in /utils/ called tempfilemodif.py can be run over a chip folder.
Don't use this script several times.. this is not very clean and will have to be fixed but it is like this for the moment.

Once the data files have been modified, one can the basic plotting scripts like comparechip.py or comparesignal.py
