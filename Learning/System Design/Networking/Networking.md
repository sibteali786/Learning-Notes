```table-of-contents
```
# Fundamentals of Networking 
## Main Resource or Notes
![[Fundamentals+of+Networking+Engineering.pdf]]

## TCP ( Transmission Control Protocol)
### Flow Control
#### Problem
![[Screenshot 2025-12-31 at 10.39.58 AM.png]]
- Sending segments one by one is quite time consuming and is not scalable. its like a road with one lane offcourse it cannot handle large traffic. 
#### Solution 
![[Screenshot 2025-12-31 at 10.47.55 AM.png]]
- We can send multiple segments in one go and how much we can send is what we call **Flow Control**
#### How much Sender can send ?
![[Screenshot 2025-12-31 at 11.01.03 AM.png]]
- This is where Receiver Window ( RWND ) size comes into picture 
![[Screenshot 2025-12-31 at 11.02.07 AM.png]]
- The RWND is always changing its size depending on how many other Hosts its dealing with. Like in example it changes from 1 segment to 3 as shown. 
#### Sliding Window
- Sender maintains a sliding window to know how much it can send to receiver in one go.
![[Screenshot 2025-12-31 at 11.02.30 AM.png]]
- The amount of segments we move to sliding window depends on how much segments are Acknowledged by the Receiver Host B in each ACK.
- here its acknowledging 2 segments sometimes and sometimes only one.
### Still this 16kb or even 64kb is too small ? ( Window Scaling )
- This is where we get idea of Window Scaling 
- Ideally we cannot increase the bits in the segment but we can increase the window size ( sliding window size or the no of segments receiver can receive in one go)
- ![[Screenshot 2025-12-31 at 11.16.07 AM.png]]
- Remember its only decided when we are in Handshake phase after that it cannot be changed or modified.

# WebRTC ( Web Real Time Communication)
## Intuition
- Its Peer to Peer since we need low latency and transmit data as soon as possible
- Built on top of UDP ( Its fast )
### Peer to Peer
- Peer to peer means two user devices connect directly to each other instead of always sending data through a central server. 
- A peer is just an equal participant in the network like your laptop or phone acting as both client and server.
- unlike a client it can receive inbound requests unlike server it can also initiate a connection to another peer.
## Overview
- A wants to connect to. B
- A finds out all possible ways public can connect to it, means check if its publicly available to be connected to. or if it can expose its port forwarding rules 
- B also finds out all possible ways public can connect to it and so on
- A and B signal this session information or bunch of information in form of a string via some means. This way to send session information to each other is `Signalling` and after this they can now communicate without it
- This path they connect through is most optimal path.
## WebRTC Demystified
### NAT
- If we have a public IP address, anyone can connect to our specific port in this IP address directly (Aws Ec2 instance exposes public)
- Today everyone is behind a NAT ( Network Address Translation ), if we are connected to a Router or LAN ( Local Area Network) only our router / LAN has a public IP while we have a private IP.
#### Intuition
- If we want to connect to google at ip 4.4.4.4 at port 80 from our 8992 port and ip 10.0.0.2
- We will first do Subnet Masking to check if 4.4.4.4 is on same network as 10.0.0.2 which its not so cannot connect directly
- Then we will ask `Gateway` to help us since it might know how to connect to it 
![[Screenshot 2026-01-15 at 12.13.25 PM.png]]
- Somehow it reaches Router and it sees its destination as `4.4.4.4` so its not meant for it self but for outer world
- Since router has a Public IP and public presence it does not allow our local machine with private Ip to connect to outer world directly
- so it replaces the Port with one it provides using some mapping so it can trace back which machine on which port made the request 
![[Screenshot 2026-01-15 at 12.16.11 PM.png]]
- Then we use `3333` as port and `5.5.5.5` as public IP and reach server ( Google at 4.4.4.4 at port 80) 
- Sevrer then responds to Router at `5.5.5.5:3333` since it know router not local machine 
![[Screenshot 2026-01-15 at 12.24.39 PM.png]]
- ![[Screenshot 2026-01-15 at 12.25.39 PM.png]] Router checks the destination ip 5.5.5.5 and says its not for itself and checks the mapping to find it was for 10.0.0.2:8992 and sends to machine.
### NAT Translation Methods
- WebRTC does 90% communication via first 3 while last one is not used ideally and in case of `Symmetric Nat` it follows a workaround.
- It better to leave WebRTC in case of Symmetric NAT
- ![[Screenshot 2026-01-15 at 12.28.04 PM.png]]
#### One to One NAT (Full cone NAT)
