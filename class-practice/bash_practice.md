## Bash Practice for DS219

This exercise includes basic file and directory management, viewing and manipulating file content, using a text editor, and understanding process management in the Bash shell.

### Part 1: Working with Directories and Files

1. **Create a New Directory**:  
   Create a new directory called `ds219`.
   ```bash
   mkdir ~/Desktop/ds219
   ```

2. **Change Directory and Verify Location**:  
   Navigate to the `ds219` directory and print the current directory path.
   ```bash
   cd ~/Desktop/ds219/
   ```
   ```bash
   pwd
   ```

3. **List Directory Contents**:  
   Display the contents of the current directory.
   ```bash
   ls -l
   ```

### Part 2: File Creation and Editing with `vi`

4. **Create and Edit Files using `vi`**:  
   Use `vi` to create and edit `file1.txt` and `file2.md`.
   - Open `file1.txt` in `vi`, type some text, save, and exit:
     ```bash
     vi file1.txt
     ```
     (In `vi`, type `i` to enter insert mode, type your text, press `Esc` to exit insert mode, type `:wq` to save and quit.)
   - Repeat the process for `file2.md`.

5. **View File Contents with `cat`**:  
   Display the contents of `file1.txt` and `file2.md`.
   ```bash
   cat file1.txt
   cat file2.md
   ```

### Part 3: Script Writing and Execution

6. **Create a Script File**:  
   Use `touch` to create a new file called `myscript.sh` and make it executable.
   ```bash
   touch myscript.sh
   chmod +x myscript.sh
   ```

7. **Edit Script with `vi`**:  
   Write a Bash script into `myscript.sh` using `vi` that performs an HTTP header check.
   ```bash
   vi myscript.sh
   # Add the following lines in vi:
   # #!/bin/sh
   # curl --head --silent https://github.com/DS219/resources/blob/main/LICENSE
   ```

8. **Execute the Script**:  
   Run the script and understand file permissions.
   ```bash
   ./myscript.sh
   ```

### Part 4: Advanced File Manipulation

9. **Using `less` to View Files**:  
   View the contents of `myscript.sh` using `less`.
   ```bash
   less myscript.sh
   ```

10. **Searching Within Files Using `grep`**:  
   Use `grep` to search for 'curl' in `myscript.sh`.
   ```bash
   grep 'curl' myscript.sh
   ```

### Part 5: Safe File Removal

11. **Demonstrate Safe Removal with `rm`**:  
    Explain the dangers of `rm` and practice safe removal techniques.
    - Remove `file1.txt` with confirmation:
      ```bash
      rm -i file1.txt
      ```
    - List and remove Markdown files safely:
      ```bash
      ls *.md
      rm -i *.md
      ```

### Part 6: Redirecting Output and Managing Processes

12. **Redirect Output and Append**:  
    Use commands to manage output files.
    ```bash
    date > ~/today.txt
    ls ~ >> ~/today.txt
    ```

13. **List Processes by CPU Usage**:  
    List non-root user processes sorted by CPU usage using `ps`.
    ```bash
    ps -u $USER --sort=-pcpu
    ```

### Part 7: Clean Up

14. **Remove Temporary Files**:  
    Carefully delete the `today.txt` file.
    ```bash
    rm ~/today.txt
    ```
