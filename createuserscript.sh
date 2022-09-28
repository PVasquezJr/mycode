#!/bin/bash

#function to prompt user to 
userprompt(){

echo "What is the name of our new user?"
read USR
echo "What is the group our new user belongs to?"
read GRP

}

#functionto create new user 
createuser(){
echo "Creating new User!"
sudo useradd $USR
echo "$USR has been created!"
echo "We will now Create $GRP (if necessary) and add $USR to $GRP!"
sleep 1
sudo groupadd $GRP
echo "We will now add $USR to $GRP"
sleep 1
sudo usermod -aG $GRP $USR
echo "Finished!"
}

#function to quit
quit(){
echo "Would you like to quit afterwards? (Type exit)"
read QUT
}

echo "Welcome to the User/Group Creation Application!"
echo "This application creates users and groups."
echo "This application will also automatically add a user to a group."
echo "This application works with existing groups as well!"
sleep 1

#calling our function to do the job
while [ "$QUT" != "exit" ]
do
    userprompt
    quit
    createuser
done

#Validation check



echo "Thank you for using useradd!"
