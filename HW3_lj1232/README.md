# Assignment_1

At first I created the test.csv file in GitHub and pulled the changes lcoally. After that I tried to remove the file but it didn't work. I used the commands provided, yet git wasn't able to rewrite the head. I removed the file from GitHub by a simple delete method, however the commit was still there. I used git reset --hard HEAD to revert to a previous commit, and then I pushed the changes to GitHub (that erased the history). After that I went the other way around, created the test.csv locally and pushed it to GitHub, and then used `git filter-branch` command and now it worked.

![image](Assignment_1/repo_csv_file_2.JPG '.csv file')
![image](Assignment_1/repo_history_2.JPG 'history cleared')

