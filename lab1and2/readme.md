
# LAB 1: Basic Linux Terminal commands.  

## $ hostname - name of device on network  
![hostname](lab1_images/hostname.jpg)  

## $ git clone - clones git repository to whatever directory you're in  
![git clone](lab1_images/gitclone.jpg)  

## $ cd - moves you to root directory.
- $ cd [directory name] - moves you to named directory.  
- $ cd .. - moves you to parent directory. 
 
![cd](lab1_images/cd..ls.jpg)  

## $ ls - lists all files and folders in a directory.  
![ls](lab1_images/ls_and_mv.jpg)  

## $ ping localhost - pings your own machine.
![pinglocalhost.jpg](lab1_images/pinglocalhost.jpg)  

## $ df - displays avilable disk space.  
![df](lab1_images/df.jpg)  

## $ ifconfig - displays ip, mac address, etc. 
I have not posted this because ifconfig can contain sensitive information that should not be on a public repository.  

## $ mkdir [directory name] - creates a new folder/directory in the current directory. 
![mkdir](lab1_images/mkdir.jpg)  

## $ uname - displays machine details.
![uname](lab1_images/uname.jpg)  

## $ man [service] - displays manual for called service. Below is an example for the service "uname".
![man](lab1_images/man.jpg)  

---  
# LAB 2G and 2H: Audio and Image Recording  
## LAB 2G: Audio Recording 
For this section of the lab, I used a the microphone of a USB webcam as my acting microphone and a pair of ordinary earbuds for playback through the Raspberry Pi 4B's 3.5 mm  
audio jack. I used the "arecord" service to record audio and "aplay" service to play back the produced .wav files. Below are screenshots of the commands and the subsequent  
audio files.   

### "test.wav" - First Audio file
For this audio file, I simply typed 'arecord test.wav' to get started.
