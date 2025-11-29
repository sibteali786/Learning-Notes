 ## Linux Basics

![[Pasted image 20251011215108.png]]
### Resources

![[DevOps-Pre-Requisites-v2-1.pdf]]

## Web Servers
### Apache Web Server 
- Document root  is at `/var/www/html` that is where html lives and is shown to us when we run Apache server and visit localhost ( running at port 80 )
- We can use a custom domain name like www.houses.com in Apache bit for it to work we need to specify the entry configured in the networks DNS server which is usually at /etc/resolv.conf
- Or for the workaround you can simply add entry in /etc/hosts.
-   main conf file is `http.conf` while individual conf files can be made with prefix of website name followed by `.conf`
- Then we can `Include` command to add these conf in main `httpd.conf` file.
```plaintext
Include conf/houses.conf
Include conf/oranges.conf
```
### Apache Tomcat
- Runs on port 8080, used to deploy Java based web applications
### IP and PORTS
- By default every system has a Virtual IP Address which is called loopback address ( 127.0.0.1 )![[Pasted image 20251019151300.png]]
 - This IP means i, me and myself that is to refer our own self for testing purposes ( localhost )
 - This also means this host ( IP ) can onl be accessed by this machine itself and none other from external world
### Database
- We are mostly choosing between mysql and no sql at most.
#### SQL
- for our case example is mysql 
- /var/log/mysqld.log
- using `%` sign we denote that user can connect from any ip address whatsoever.
- ![[Pasted image 20251020165710.png]] while in case of specific values that restricts user to only connect from those systems specified by IP addresses.
##### Permissions
![[Pasted image 20251020172102.png]]
- These are the different permissions that can be associated with a user of a particular user on speific general ip.
- 
#### Networking Basics 
![[Networking-Basics.pdf]]
- **Switch** helps connect two machines on same network using a **Switch**
- **Router** helps connect two networks together
- When a device in one network tries to send something to a device in another network, because the router can be any other device on the network, That is where **Gateways** come into picture.
	- If network is a room , **gateway** is a door to out world. That is why systems in a given network need to know this gateway to visit out world
- When we use **ping**, **ssh**, **curl** command and and use a **name** / **host-name** as its argument.
- The process of translating the host-name is `Name Resolution`
#### Additional Resources 
![[Additional-Resources.pdf]]
### General Pre-requisites 
#### JSON & JSON-PATH
- $ sign used to represent root of json element 
- dictionaries can be used with dot ( . ) notation 
- [JSON Path Notes](https://notes.kodekloud.com/docs/DevOps-Pre-Requisite-Course/General-Pre-Requisites/JSON-JSON-Path)
- ![[Pasted image 20251023143200.png]]

