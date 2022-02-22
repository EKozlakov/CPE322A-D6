
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
For this section of the lab, I used a the microphone of a USB webcam as my acting microphone and a pair of ordinary earbuds for playback through the Raspberry Pi 4B's 3.5 mm audio jack. I used the "arecord" service to record audio and "aplay" service to play back the produced .wav files. Below are screenshots of the commands and the subsequent audio files.

I first checked if my Raspberry Pi registered any of my audio inputs and outputs by typing `arecord -l` in the commandline. This lists any recording devices available to the Pi in a simple format. In this case, my webcam was the available recording device, listed as such. 
![arecord-l]()  

I then checked if my Pi successfully registered my audio output (earbuds) by typing `aplay -l` in the commandline. Again, this is the same as `arecord -l` but for output devices. 
![aplay-l]()  

Now that I knew my inputs and outputs were recognized, I started recording my audio files.

### "test.wav" - First Audio file
For this audio file, I simply typed `arecord test.wav` to get started. This is the simplest way to get started recording. By default, `arecord` records in Unsigned 8-bit, 8kHz sample rate in Mono audio. 
![test1wav.jpg]()
[test.wav]()

### "test2.wav" - Second Audio file
For this audio file, I followed assignment parameters and typed the following in my commandline: `arecord --device=hw:2,0 --format S16_LE --rate 44100 -c1 test2.wav`. The breakdown is as follows: 
 - the `device` field specifies which device I'm using to record, in this case device 2; 
 - the `format` field indicates the file is being recorded in S16_LE format; 
 - the `rate` field indicates the sampling rate for the file, in this case it's 44.1 kHz (defaulted to 48 kHz);
 - and the `c1` indicates the number of channels for the recording, in this case, 1 channel was used. 
The screenshots and resulting audio files are below.  
![test2wav.jpg]()
[test2.wav]()
