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

## After installing Docker toolbox:

I followed the same steps above, however I used emacs editor instead of nano.

![Alt text](../HW1_lj1232/images/docker_.bashrc.JPG "docker .bashrc")

![Alt text](../HW1_lj1232/images/docker_set_env.JPG "terminal")

## Set Environment Variables on a Windows Machine:

I also figures out how to set environmental variables from the terminal my windows machine.

1. Created a directory **PUI2018** on my computer 
```
mkdir PUI2018 

OR 

md PUI2018 
```
2. Created an temporary environment variable **PUI2018** that points to that directory. 
`set PUI2018 = C:\Users\linda\Documents\GitHub\PUI2018`
...To save an environment variable permanently I need to write the same line of code in a file. Since windows don't have a .bashrc ...file, I create a batch (.bat or .cmd) file that will have all the commands I want to execute upon cmd startup.

3. Create a .bat file in a location you choose. name it for example autorun.bat
To do that create a .text file and then change the extention to .bat
4. Right click your .bat file and select edit.
You can start by writing echo off so that you don't see all the commands being executed every time you open you terminal. Then write the same line of code used above to set a temporay environment variable:
set PUI2018 = C:\Users\linda\Documents\GitHub\PUI2018
5. Also in the .bat file write the code for alias as well:
doskey pui2018 = cd C:\Users\linda\Documents\GitHub\PUI2018
Note to comment in the .bat file you can use ::
6. Open Run by pressing windows key +r
7. Type regedit to open Registry Editor
8. In the left pane, navigate to HKEY_CURRENT_USER\Software\Microsoft\Command Processor
9. In the right pane, right click and select String, this adds a new key into the registry.
10. Name it AutoRun (mind caps)
11.Double click AutoRun and add the path of your .bat file in the value (to get the path open your file and copy the link to it)
Now these commands will be executed everytime you open your terminal!
Sources: https://nitin09.wordpress.com/2013/11/12/bashrc-in-windows-for-command-line-startup/
    
    
      
    
