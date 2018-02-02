#-------------------------------------------------------------------------------------------------------------------------
#library import here
import sys
import math
import wave
import numpy as np
from scipy import signal
from PIL import Image
#-------------------------------------------------------------------------------------------------------------------------
#python environment configuration
sys.path.insert(0,'../') # to specify python code exist in another folder
np.set_printoptions(threshold=np.inf) # to forced full print of numpy array
#-------------------------------------------------------------------------------------------------------------------------
#files import here
#import adaptation_image as normal
#import load_file as wload
#import load_database as Db
#import Vcifar10 as Vcifar10
#to use a function defined into an other file do as follow: file_imported_name.function_name
#-------------------------------------------------------------------------------------------------------------------------


sound=wave.open('test','r')#open test.wav in read only mode
#get and display basic information about the files
sound.getnchannels()
sound.getsampwidth()
sound.getframerate()
sound.getnframes()
sound.getcomptype()
sound.getcompname()
sound.getparams()

sound.close()
