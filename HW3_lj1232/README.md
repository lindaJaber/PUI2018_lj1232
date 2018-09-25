# Brief

I worked on this homework alone. A youtube video helped me download a 'json formatter' chrome extension to get a parsed view. A family member talked me through what is a parsed json file.  
I learned how to read a csv and a json file using pandas in assignment_2. In assignment_3 I learned how to get an API key and use it retrieve information form the MTA about buses. I learned how to write a python script that executes in the command line. I learned about setting arguments in sys.argv. In assignment_4 I learned how to write a python script that retrieves data from an API and outputs to a csv file.
While trying to understand read and explore the json file from the MTA API in a side notebook, I had to explicitly set the MTAKEY environment variable everytime I opened the notebook although it was set in my bashrc file. I learned later that the notebook doesn't read my bashrc file. I would like to know more about this issue.

# Assignment_1

At first I created the test.csv file in GitHub and pulled the changes lcoally. After that I tried to remove the file using `git filter-branch` but it didn't work, git wasn't able to rewrite the head. I removed the file from GitHub by a simple delete method, however the commit was still there. I used `git reset --hard HEAD` to revert to a previous commit, and then I pushed the changes to GitHub (that erased the history). After that I went the other way around, created the test.csv locally and pushed it to GitHub, and then used `git filter-branch` command and now it worked.


#### Below are screen shots showing the csv file and the folder commit history:
![image](Assignment_1/repo_csv_file_2.JPG '.csv file')

![image](Assignment_1/repo_history_2.JPG 'history')

#### Below is a screen shot showing my history cleared after `git filter-branch`:
![image](Assignment_1/cleared_history.JPG 'history cleared')
