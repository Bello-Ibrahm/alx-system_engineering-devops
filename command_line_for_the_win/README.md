# CMD CHALLENGE 

## Practising the command line challenge with SFTP to push image screenshot on the remote machine
SFTP, which stands for Secure File Transfer Protocol, is a network protocol that provides file access, file transfer, and file management over any reliable data stream. It was designed by the Internet Engineering Task Force (IETF) as an extension of the Secure Shell protocol (SSH) version 2.0 to provide secure file transfer capabilities, and is seen as a replacement of File Transfer Protocol (FTP) due to superior security. [Read more](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol)

### STEPS:
Using the command prompt/terminal on my local machine:
- connecting to the remote server with the command `sftp myUsername@hostname` then applied password to gain access.
- Navigating to the local machine directory where screenshots were saved with the command `lcd Desktop/alx/cmd-proj`
- Navigating to the remote machine directory where screeshots were to be uploaded with the command `cd root/alx-system_engineering-devops`
- Create a directory with the command `mkdir command_line_for_the_win`
- Navigating to the created dir with the command `cd command_line_for_the_win`
- Printing the local machine working directory with the command `lpwd`
- Viewing the content of the local machine directory with the command `lls` before uploading to the remote machine
- Uploading the screenshots (.jpg and .png files) usinge the command `put filename`
- Uploading the files from local machine to the remote machine all at once with the command `put *.jpg` and `put *.png`
- Got a success message that everything has been uploaded
- Confirm the uploaded file on remote machine with the command `ls`
- Everything confirmed.

`l` -> stands for local `lpwd`=> local print working directory

[CMD CHALLENGE](https://cmdchallenge.com/)

[SFTP Tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server)

[SFTP Guides](https://man.openbsd.org/sftp)
