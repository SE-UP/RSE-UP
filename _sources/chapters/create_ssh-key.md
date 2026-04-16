# Using SSH on Gitlab and Github

Since both Gitlab and and Github require either passkeys or ssh keys to use in full, we have included the instructions to add ssh keys below. 
Passkeys are great as well, but ssh keys work on Windows, Mac, and Linux the same way. This is especially useful in the future when you will have to remote login into a computer or server. This is done using a ssh connection about 98% of the time.


In general, in general it is advised to use the `ed25519` encryption standard and if you have multiple Github, Gitlab accounts it is advised to name the key differently. I.e., when the prompt asks for a path and name instead of the default use something like this: `.ssh/github_work` or `.ssh/gitup_temp`. This may be good practice in general, so that you can easily identify what ssh key is for what purpose. 

## Github

The instruction on how to add an SSH key on Github can be found [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

## Gitlab

For Gitlab (works on GitUP as well) the instructions can be found [here](https://docs.gitlab.com/ee/user/ssh.html), BUT it is advised to look at the SSH key generation instruction on the Github documentation instead. They have complete instruction for Windows, Mac, and Linux. Generating a ssh-key is the same for both Github and Gitlab.
