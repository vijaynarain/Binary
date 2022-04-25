import os
import subprocess
import time
import getpass

os.system("clear")

from termcolor import colored, cprint

#main screen
while True:
    #cprint("""\n\n\t\t\t\t\t  
    #                                    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗    ████████╗░█████╗░  
    #                                    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝    ╚══██╔══╝██╔══██╗  
    #                                    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░    ░░░██║░░░██║░░██║  
    #                                    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░    ░░░██║░░░██║░░██║  
    #                                    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗    ░░░██║░░░╚█████╔╝  
    #                                    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝    ░░░╚═╝░░░░╚════╝░  

    #                                    ██████╗░██╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗    ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
    #                                    ██╔══██╗██║████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝    ████╗░████║██╔════╝████╗░██║██║░░░██║
    #                                    ██████╦╝██║██╔██╗██║███████║██████╔╝░╚████╔╝░    ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
    #                                   ██╔══██╗██║██║╚████║██╔══██║██╔══██╗░░╚██╔╝░░    ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
    #                                    ██████╦╝██║██║░╚███║██║░░██║██║░░██║░░░██║░░░    ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
    #                                    ╚═════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░    ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░""", 'red',attrs=['blink'])
    print('\n\n')

    #cprint('\t\t\t\t\t\t\t\t\t Services', 'green')

    #print('\n 1.Docker \n 2.AWS \n 3.LVM \n 4.Hadoop \n 5.Networking \n 6.Ansible \n 7.Webserver')
    cprint("""
                                                 Welcome To Binary Menu
           
              -------------------------------------------   
              | OPTIONS |            SERVICES           |  
              -------------------------------------------  
              |    1    |             DOCKER            |       
              -------------------------------------------       
              |    2    |               AWS             |       
              -------------------------------------------       
              |    3    |               LVM             |   
              -------------------------------------------       
              |    4    |              HADOOP           |   
              -------------------------------------------   
           """, 'yellow')

    cprint("\n\t\t\t for example if you want to choose LVM than type 3 (same as options)", "yellow")
    cprint("\n choose your service..... = ", "red", end=' ')
    service= input()

    os.system("clear")

    cprint('\n\n\t\t\t\t\t you choosed {} as a service'.format(service), 'red')

    #   .................................................Docker.................................................

    if service=='1':
        
        while True:
        
            cprint("\n\t\t\t Here you can manage your Docker services like Docker image pull, start, stop, info", 'yellow')
            cprint("\n\t\t Docker Services", 'green')
            
            #print("\n 1.Docker Start/Enable \n 2.Docker Status \n 3.Docker Info \n 4.Docker Images \n 5.Download Docker OS Images \n 6.Run Docker \n 7.Stop Docker \n 8.Configure WebServer \n 9.Back to Main Menu")
            cprint("""
                  ----------------------------------------------------------
                  | OPTIONS |                SERVICES                      |
                  ----------------------------------------------------------
                  |    1    |             Docker Start/Enable              |
                  ----------------------------------------------------------
                  |    2    |             Docker Status                    |
                  ----------------------------------------------------------
                  |    3    |             Docker Info                      |
                  ----------------------------------------------------------
                  |    4    |             Docker Images                    |
                  ----------------------------------------------------------
                  |    5    |             Download Docker OS Images        |
                  ----------------------------------------------------------
                  |    6    |             Run Docker                       |
                  ----------------------------------------------------------
                  |    7    |             Stop Docker                      |
                  ----------------------------------------------------------
                  |    8    |             Configure WebServer              |
                  ----------------------------------------------------------
                  |    9    |             Back to Main Menu                |
                  ----------------------------------------------------------
                   """, 'yellow')
            cprint("\n for example if you want to choose 'Docker Info' than type 3 (same as options)", "yellow")
            cprint("\n choose your service..... = ", "red", end=' ')
            docker_service = input()
            
            #third screen of sub services
            os.system("clear")
            cprint('\n\n\t\t\t\t\t you choosed {} as a service'.format(docker_service), 'red')

            if docker_service== '1': #start docker
                
                cprint("\n\n\t...................................DOCKER IS STARTING.....................................", 'green')
                print("\n\n")
                os.system("systemctl enable docker")
                print("\n")
                os.system("systemctl start docker")
                
            elif docker_service=='2': #status
                
                cprint("\n\n\t..................................DOCKER STATUS...........................................", 'green')
                print("\n\n")
                os.system("systemctl status docker")
                
            elif docker_service=='3': #info
            
                cprint("\n\n\t..................................DOCKER INFO.............................................", 'green')
                print("\n\n")
                os.system("docker info")
                print("\n")
                os.system("docker ps -a")
                
            elif docker_service=='4': #images
                
                cprint("\n\n\t..................................DOCKER IMAGES...........................................", 'green')
                print("\n\n")
                os.system("docker images")
                
            elif docker_service=='5': #pull images
                
                cprint("\n\n\t................................DOCKER PULL IMAGES......................................", 'green')
                print('\n\n')
                cprint("Enter Your Image Name = ", 'red', end='')
                image_name = input()
                cprint("\n\n Enter Your Image Version (To Download Latest Version Left This Empty) = ", 'red', end='')
                image_version = input()
                print("\n\n")
                os.system("docker pull {}:{}".format(image_name, image_version))
                
            elif docker_service=='6': #run docker
            
                cprint("\n\n\t....................................Run Docker.............................................", 'green')
                print("\n\n")
                cprint("Enter Your OS Name = ", 'red', end='')
                os_name = input()
                cprint("\n\n Enter Your Image Version = ", 'red', end='')
                os_version = input()
                print("\n\n")
                os.system("docker run -it {}:{}".format(os_name, os_version))
                
            elif docker_service=='7': #stop docker
                
                cprint("\n\n\t......................................STOP Docker.............................................", 'green')
                print("\n\n")
                cprint("Enter Your OS Name = ", 'red', end='')
                os_name = input()
                os.system("docker stop {}".format(os_name))
            
            elif docker_service=='8': #configure webserver
            
                cprint("\n\n\t.....................CONFIGURING WEBSERVER ON DOCKER......................", 'green')
                print("\n\n")
                cprint("Enter Your OS Name (example vijayos, shivanios, marvel0s i.e.) = ", 'red', end='')
                os_name = input()
                cprint("Enter your OS Image Name (example centos, ubuntu i.e.) = ", 'red', end='')
                os_image_name = input()
                cprint("Enter Your OS Version = ", 'red', end='')
                os_version = input()
                print("\n\n")
                os.system("docker run -it --name {} {}:{}".format(os_name, os_image_name, os_version))
                print("\n\n")
                os.system("yum install httpd")
                print("\n\n")
                os.system("/usr/sbin/httpd")
                
            elif docker_service=='9':
            
                break
                
                
    #second screen of services of LVM
    
    #......................................................AWS..................................
    
    if service=='2':
        
        while True:
            cprint("\n Here you can use your AWS service Like Instance Start, Stop and also to Lauch Instance and create volume")
            cprint("\n\t\t\t\t\t AWS Service", 'green')
            
            cprint("""
                  ----------------------------------------------------------
                  | OPTIONS |                SERVICES                      |
                  ----------------------------------------------------------
                  |    1    |             Login into AWS CLI               |
                  ----------------------------------------------------------
                  |    2    |              Launch a instance               |
                  ----------------------------------------------------------
                  |    3    |              Start a Instance                |
                  ----------------------------------------------------------
                  |    4    |              Stop a Instance                 |
                  ----------------------------------------------------------
                  |    5    |           Describe All Instances             |
                  ----------------------------------------------------------
                  |    6    |              Create a Volume                 |
                  ----------------------------------------------------------
                  |    7    |         Attach volume with instance          |
                  ----------------------------------------------------------
                  |    8    |       Partitioning the attached volume       |
                  ----------------------------------------------------------
                  |    9    |           configure Web Server               |
                  ----------------------------------------------------------
                  |   10    |             Format Partition                 |
                  ----------------------------------------------------------
                  |   11    |        Mount the Web Server to Volume        |
                  ----------------------------------------------------------
                  |   12    |          Install And Download AWS CLI        |
                  ----------------------------------------------------------
                  |   13    |             Back to Main Menu                |
                  ----------------------------------------------------------
                   """, 'yellow')

            print("Enter Your Choice : ",end="")

            ch=input()


            if int(ch) == 1:

                os.system("aws configure")

            elif int(ch) == 2:
                print("""
                        Press 1:AWS Linux
                        Press 2:Redhat Linux
                        """)
                print("Enter your Choice :  ",end="")
                img=input()
                if int(img) ==1:
                    print("Enter Your Key name: ",end ="")
                    key = input()
                    os.system("aws ec2 run-instances --image-id ami-0d2986f2e8c0f7d01 --subnet-id  subnet-0eb6a430b8c1d1842 --instance-type t2.micro --key-name {} --security-group-ids sg-031cdd4669bea4884 --count 1".format(key))
                elif int(img) == 2:
                    print("Enter Your Key name: ",end ="")
                    key = input()
                    os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --subnet-id subnet-ba5b5cd2 --instance-type t2.micro --key-name {} --security-group-ids sg-0c111e5b44f074df9 --count 1".format(key))


            elif int(ch) == 3:

                print("Enter Instance Id : ",end = "")
                uid = input()
                os.system(" aws ec2 start-instances --instance-id {}".format(uid))


            elif int(ch) == 4:
                
                print("Enter Instance Id : ",end = "")
                uid = input()
                os.system(" aws ec2 stop-instances --instance-id {}".format(uid))


            elif int(ch) == 5:

                os.system("aws ec2 describe-instances")

                
            elif int(ch) == 6:

                
                print("Enter Size : ",end = "")
                size = input()
                print("Enter availability zone : ",end = "")
                zone = input()
                print("Enter volume type : ",end= "")
                vtype = input()
                os.system(" aws ec2 create-volume  --availability-zone {} --size {} --volume-type {}".format(zone,size,vtype))


            elif int(ch) == 7:


                os.system("tput setaf 3")
                print("\t\t\tVolume Zone & Instance Zone Must be same !!!")
                print("\t\t\t--------------------------------------------")
                os.system("tput setaf 7")
                print("Enter volume-id : ",end = "")
                vid = input()
                print("Enter instance-id : ",end = "")
                iid = input()
                print("Enter device : /dev/",end= "")
                device = input()
                os.system(" aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/{} ".format(vid,iid,device))


            elif int(ch) == 8:

                print("Enter IP : ",end = "")
                ip = input()
                print("Enter key : ",end = "")
                key = input()
                print("Enter device : /dev/",end= "")
                device = input()
                os.system(" ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/{} ".format(ip,key,device))



            elif int(ch) == 9:

                os.system("tput setaf 3")
                print("\t\t\tHTTPD must be installed...")
                print("\t\t\t--------------------------")
                os.system("tput setaf 7")
                print("Enter IP : ",end = "")
                ip = input()
                print("Enter key : ",end = "")
                key = input()
                os.system(" ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd ".format(ip,key))


            elif int(ch) == 10:

                print("Enter IP : ",end = "")
                ip = input()
                print("Enter key : ",end = "")
                key = input()
                print("Enter Device : /dev/",end="")
                device = input()
                os.system(" ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{} ".format(ip,key,device))


            elif int(ch) == 11:

                print("Enter IP : ",end = "")
                ip = input()
                print("Enter key : ",end = "")
                key = input()
                print("Enter Device : /dev/",end="")
                device = input()
                os.system(" ssh -l ec2-user {} -i {}.pem sudo mount /dev/{} /var/www/html/ ".format(ip,key,device))


            elif int(ch) == 12:
                
                cprint("\n\n\t...................................AWS CLI IS DOWNLOADING.....................................", 'green')
                print("\n\n")
                os.system('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"')
                print("\n\n")
                
                cprint("\n\n\t...................................YUM INSTALLING UNZIP.....................................", 'green')
                print("\n\n")
                os.system('yum install unzip')
                print("\n\n")
                
                cprint("\n\n\t.....................................AWS UNZIPING FILES.....................................", 'green')
                print("\n\n")
                os.system('unzip awscliv2.zip')
                print("\n\n")
                
                cprint("\n\n\t.......................................AWS INSTALLING.....................................", 'green')
                print("\n\n")
                os.system('sudo ./aws/install')
                print("\n\n")
                os.system("aws --version")
                print("\n\n")
            
            elif int(ch) == 13:
                break
                
            else:
                print("You Entered Wrong Choice ...")

    #......................................................LVM..................................

    if service=='3':
        
        while True:
            
            cprint("\n Here you can create manage and create your LVM, VG, LV and Pysical disk", 'yellow')
            cprint("\n\t\t\t\t\t LVM Services", "green")
            
            #print("\n 1.Create New LV \n 2.All LV Info \n 3.Particular LV Info \n 4.Create PV \n 5.All VG Info \n 6.Create VG \n 7.Extend LV \n 8.Back to Main Menu")
            cprint("""
                  ----------------------------------------------------------
                  | OPTIONS |                SERVICES                      |
                  ----------------------------------------------------------
                  |    1    |             Create New LV                    |
                  ----------------------------------------------------------
                  |    2    |             All LV Info                      |
                  ----------------------------------------------------------
                  |    3    |             Particular LV Info               |
                  ----------------------------------------------------------
                  |    4    |             Create PV                        |
                  ----------------------------------------------------------
                  |    5    |             All VG Info                      | 
                  ----------------------------------------------------------
                  |    6    |             Create VG                        |
                  ----------------------------------------------------------
                  |    7    |             Extend LV                        |
                  ----------------------------------------------------------
                  |    8    |             Back to Main Menu                |
                  ----------------------------------------------------------
                 """, 'yellow')
            cprint("\n for example if you want to choose 'Create New LVM' than type 1 (same as options)", "yellow")
            cprint("\n choose your service..... = ", "red", end=' ')
            lvm_service = input()
            
            #third screen of sub services
            os.system("clear")
            cprint('\n\n\t\t\t\t\t you choosed {} as a service'.format(lvm_service), 'red')

            if lvm_service== '1':
                
                cprint("\n\t\t\t\t .......................these are your drive and disk.........................", "green")
                time.sleep(4)
                os.system('fdisk -l')
                
                #Physical Volume
                cprint("\n\n Enter your drive which you want to create PV = ", 'red',end='')
                pv= input()
                pvcmd = os.system("pvcreate {}".format(pv))
                #subprocess.getoutput(pvcmd)
                print("\n\n")
                os.system("pvdisplay {}".format(pv))

                #Volume Group
                print("\n Now Create VG (Volume Group)")
                cprint("\n\n Enter your VG name = ", 'red',end='')
                vg_name= input()
                cprint("\n\n Enter your PV name = ", 'red',end='')
                pv_name = input()
                vgcmd = os.system("vgcreate {} {}".format(vg_name, pv_name))
                #subprocess.getoutput(vgcmd)
                print("\n\n")
                os.system("vgdisplay {}".format(vg_name))
                
                #LV
                print("\n\n Now Create LV (Logical Volume)")
                cprint("\n\n Enter your LV name = ", 'red',end='')
                lv_name= input()
                print("\n\n your VG name is {}".format(vg_name))
                cprint("\n\n Enter your LV Size = ", 'red',end='')
                lv_size = input()
                lvcmd = os.system("lvcreate --size {} --name {} {}".format(lv_size, lv_name, vg_name))
                #subprocess.getoutput(lvcmd)
                print("\n\n")
                os.system("lvdisplay {}/{}".format(vg_name, lv_name))
                
                #format for LV
                cprint("\n\n Now time to format and mount the LV to your folder", "yellow")
                cprint("\n Enter your format type (Example mkfs.ext4) = ", 'red',end='')
                format_name= input()
                cprint("\n\n Enter your mount folder name = ", 'red',end='')
                mount_folder = input()
                #format
                format_cmd = os.system("{} /dev/{}/{}".format(format_name, vg_name, lv_name))
                print("\n\n")
                #subprocess.getoutput(format_cmd)
                mount_cmd = os.system("mount /dev/{}/{} {}".format(vg_name,lv_name,mount_folder))
                print("\n\n")
                #subprocess.getoutput(mount_folder)
                
            elif lvm_service=='2': #get info of all LV
            
                lv_all_cmd = os.system("lvdisplay")
                #sub_lv_cmd = subprocess.getoutput(lv_all_cmd)
                #print(sub_lv_cmd)    
                
            elif lvm_service=='3': #get perticular LV info
                
                cprint("\n\n Enter your Volume Group name = ", 'red',end='')
                vg_name = input()
                cprint("\n Eneter your Logical Volume name = ", 'red', end='')
                lv_name = input()
                pvcmd = os.system("lvdisplay {}/{}".format(vg_name, lv_name))   
                
            elif lvm_service=='4': #create PV
                
                cprint("\n these are your drive and disk", "green")
                time.sleep(4)
                os.system('fdisk -l')
                
                #Physical Volume
                cprint("\n\n Enter your drive which you want to create PV = ", 'red',end='')
                pv= input()
                pvcmd = os.system("pvcreate {}".format(pv))
                
            elif lvm_service=='5': #all VG info
                
                lv_all_cmd = os.system("vgdisplay")
                
            elif lvm_service=='6':  #create VG
                
                os.system("pvdisplay")

                #Volume Group
                print("\n Now Create VG (Volume Group)")
                cprint("\n\n Enter your VG name = ", 'red',end='')
                vg_name= input()
                cprint("\n\n Enter your PV name = ", 'red',end='')
                pv_name = input()
                vgcmd = os.system("vgcreate {} {}".format(vg_name, pv_name))
                #subprocess.getoutput(vgcmd)
                print("\n\n")
                os.system("vgdisplay {}".format(vg_name)) 
                
            elif lvm_service=='7': #Extend LV
                
                os.system("lvdisplay")
                os.system("vgdisplay")
                print("\n\n Now Resize LV (Logical Volume)")
                cprint("\n\n Enter your LV name = ", 'red',end='')
                lv_name= input()
                cprint("\n\n Enter your VG name = ", 'red',end='')
                vg_name= input()
                cprint("\n\n Enter your LV ReSize(+G/-G) = ", 'red',end='')
                lv_size = input()
                lvcmd = os.system("lvextend --size {} /dev/{}/{}".format(lv_size, vg_name, lv_name))
                os.system("resize2fs /dev/{}/{}".format(vg_name, lv_name))
                
            elif lvm_service=='8':
                
                break                

    #................................................HADOOP.........................................

    if service=='4': #HADOOP
        
        while True:
            
            cprint("\n Here you can configure your Hadoop cluster, namenode, datanod and many more", 'yellow')
            cprint("\n\t\t Hadoop Services", "green")
            
            #print("\n 1.Install Hadoop Setup \n 2.Format Namenode \n 3.Start Namenode \n 4.Start Datanode \n 5.Hadoop Cluster Report \n 6.Back to Main Menu")
            cprint("""
                  ----------------------------------------------------------
                  | OPTIONS |                SERVICES                      |
                  ----------------------------------------------------------
                  |    1    |             Install Hadoop Setup             |
                  ----------------------------------------------------------
                  |    2    |             Format Namenode                  |
                  ----------------------------------------------------------
                  |    3    |             Start Namenode                   |
                  ----------------------------------------------------------
                  |    4    |             Start Datanode                   |
                  ----------------------------------------------------------
                  |    5    |             Hadoop Cluster Report            | 
                  ----------------------------------------------------------
                  |    6    |             Back to Main Menu                |
                  ----------------------------------------------------------
                  """, 'yellow')
            cprint("\n for example if you want to choose 'Install Hadoop Setup' than type 1 (same as options)", "yellow")
            cprint("\n choose your service..... = ", "red", end=' ')
            hadoop_service = input()
            
            #third screen of sub services
            os.system("clear")
            cprint('\n\n\t\t\t\t\t you choosed {} as a service'.format(hadoop_service), 'red')

            if hadoop_service== '1': #install hadoop
                
                cprint("\n\n................................Downloading Hadoop And JDK Best For Your Device........................", 'green')
                print("\n\n")
                os.system("pip3 install gdown")
                print("\n\n")
                cprint("\n\n................................Downloading Hadoop Best For Your Device........................", 'green')
                print("\n\n")
                os.system("gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5")
                print("\n\n")
                cprint("\n\n................................Downloading JDK Best For Your Device........................", 'green')
                print("\n\n")
                os.system("gdown --id 17UWQNVdBdGlyualwWX4Cc96KyZhD-lxz")
                print("\n\n")
                cprint("\n\n................................Installing JDK Best For Your Device........................", 'green')
                print("\n\n")
                os.system("rpm -i -v jdk-8u171-linux-x64.rpm")
                print("\n\n")
                cprint("\n\n................................Installing Hadoop Best For Your Device........................", 'green')
                print("\n\n")
                os.system("rpm -i -v -h hadoop-1.2.1-1.x86_64.rpm --force")
                print("\n\n")
                cprint("\n\n................................Succesfuly Installed Hadoop Best For Your Device........................", 'green')
                print("\n\n")
                os.system("hadoop version")
                print("\n\n")
                
            elif hadoop_service=='2': #format namenode
                
                cprint("\n\n................................FORMATING NAMENODE FOR HADOOP........................", 'green')
                print("\n\n")
                os.system("hadoop namenode -format")
                    
            elif hadoop_service=='3': #start namenode
                
                cprint("\n\n................................STARTING NAMENODE........................", 'green')
                print("\n\n")
                os.system("hadoop-daemon.sh start namenode")
                print("\n\n")
                os.system("systemctl stop firewalld")    
                
            elif hadoop_service=='4': #start datanode
                
                cprint("\n\n................................STARTING DATANODE........................", 'green')
                print("\n\n")
                os.system("hadoop-daemon.sh start datanode")    
                
            elif hadoop_service=='5': #hadoop report
                
                cprint("\n\n................................HADOOP CLUSTER REPORT........................", 'green')
                print("\n\n")
                os.system("hadoop dfsadmin -report") 
                
            elif hadoop_service=='6':
                
                break       
            
    else:
        print("try again 😉😉")
