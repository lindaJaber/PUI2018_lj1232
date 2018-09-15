# Steps I took to set my environment:

## On the CUSP|ADRF terminal:

1. Created a directory called PUI2018
```
mkdir PUI2018
```
2. Opened my .bashrc file
```
nano .bashrc
```
3. Added the following to end of the file:

export PUI2018="~/PUI2018"

alias pui2018="cd $PUI2018"

![Alt text](../HW1_lj1232/images/ADRF_ljaber_.bashrc.JPG ".bashrc file")

4. Reload the .bashrc file to read and execute the new commands

```
source .bashrc
```
5. Check if my environment is set

![Alt text](../HW1_lj1232/images/ADRF_set%20_env.JPG "terminal")

## On the Docker terminal:

I followed the same steps above, however I used emcs editor instead of nano.

![Alt text](../HW1_lj1232/images/docker_.bashrc.JPG "docker .bashrc")

![Alt text](../HW1_lj1232/images/docker_set_env.JPG "terminal")
    
    
      
    
