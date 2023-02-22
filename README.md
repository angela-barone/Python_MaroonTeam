# Python_MaroonTeam

Part of the Code First Girls Python Hackathon. We had to create a Brute Force Password Cracker using Ptyhon. 

1) First, we thought it would be interesting to try to 'crack' the password on a password protected PDF file.
For an extra challenge we used Python to create our own password protected PDF from scratch! We used the 'reportlab' module to do this.
We first imported the module, then created a new PDF file called 'Crack_Me.pdf'.
We then added some text before setting the secret password.

2) Then, after installing tqdm and pikePDF we proceeded to create the Password Cracker using the Brute Force Technique.
The code iterates through all the password lists and tries to open the file with each password, bypassing the password argument with the open() method, if the password does not match it will raise a PasswordError.
The "cool" part about this code is showing the progress (see screenshots below), aka how many words are still to go, and for showing it live the code uses the tqdm module.

3) Finally, we suggest a solution: according to Hive, a 12-character password created by a password manager could take some 3,000 years to brute-force crack. Thus, our team thought of creating a code that would generate a cryptographically secure 12-character password. For this code we imported two new modules: secrets and pyOpenSSL. Everytime your run the code it generates a different password and string (that could be used as a secure username as it only contains letters). 
