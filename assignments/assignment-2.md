## SSH Practice

Note: `directory` and `folder` are interchangeable in the following tasks.

Note: Windows users, please ensure you do this assignment using WSL.

0. Follow the steps here to create your SSH keys and upload it to github - https://github.com/DS219/spark-seprep/blob/main/class-practice/ssh_key_github.md.
   
   Feel free to skip this step if you already generated your keys in class.
   
   Once your `Public and Private SSH keys` are created, they should live on your system at ~/.ssh/id_rsa.pub and ~/.ssh/id_rsa respectively.

1. Your username is your BU email address without the `@bu.edu`. Copy your public SSH key to the virtual machine at `34.138.147.23`
   **Note: Replace `YOUR_NAME` with your actual BU username**

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub YOUR_NAME@34.138.147.23
# password: YOUR_PASSWORD
```

2. SSH into the machine running at IP address `34.138.147.23`.

```bash
ssh -i ~/.ssh/id_rsa YOURNAME@34.138.147.23
```

3. Create a new directory `commandline-practice`..

4. Write the output of the `date` command into a file named `output.txt` located in the directory you created in Step 2

6. Run the following:

```bash
curl -o ./commandline-practice/joke.sh https://raw.githubusercontent.com/DS219/spark-seprep/main/joke.sh
```

6. Use chmod to make it possible to run the command `/home/YOURNAME/commandline-practice/joke.sh`

7. Run the script and append the joke to the file you created in Step 3. You can copy/paste _or_ use `>>` to redirect the output of the script to the file.

8. Complete [this](https://forms.gle/eRJZsrzJVhehTVsv6) form.

9. Exit out of the virtual machine
```bash
exit
```

**HAVE FUN and ASK QUESTIONS!!**
