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
- If we have a public IP address, anyone can connect to our specific port in this IP address directly (Aws Ec2 instance exposes public IP Address)
- Today everyone is behind a NAT ( Network Address Translation ), if we are connected to a Router or LAN ( Local Area Network) only our router / LAN has a public IP while we have a private IP.
#### Intuition
- If we want to connect to google at ip 4.4.4.4 at port 80 from our 8992 port and ip 10.0.0.2
- We will first do Subnet Masking to check if 4.4.4.4 is on same network as 10.0.0.2 which its not so cannot connect directly
- Then we will ask `Gateway` to help us since it might know how to connect to it 
![[Screenshot 2026-01-15 at 12.13.25 PM.png]]
- Somehow it reaches Router ( Gateway ) and it sees its destination as `4.4.4.4` so its not meant for it self but for outer world
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
- Packets to external IP:port on router always maps to internal IP:port without exceptions.
- Router does not care where the packet is coming from, it always forwards the packet to internal Ip address![[Screenshot 2026-01-20 at 9.27.28 AM.png]]
- ![[Screenshot 2026-01-20 at 9.28.42 AM.png]]
#### Address Restricted NAT
- As the name suggests
- Packets to external IP:port on router always maps to internal IP:port as long as source address from packet matches the table ( ragardless of port)
- In other words we should have already seen the ip of the packet we are receiving. If we communicated with this host before GOOOD  
- ![[Screenshot 2026-01-20 at 9.34.51 AM.png]]
#### Port Restricted NAT
- We match exactly the destination IP and destination PORT from table like 
- 3333:8080 to 5555:3333 is allowed becuase in the table we have 3333:8080 , if it was symmetric NAT it would not be allowed since table has 5555:2222 not 5555:3333 for this pakcets destination addresss:port.
![[Screenshot 2026-01-20 at 9.36.24 AM.png]]![[Screenshot 2026-01-20 at 9.37.10 AM.png]]
#### Symmetric NAT 
- Simplest words exact matching entry should be in the table its much strict and only allows symmetric packet with same destination address:port and source address:Port as in table
![[Screenshot 2026-01-20 at 9.39.32 AM.png]]
- It does not care if it saw you before or not  ![[Screenshot 2026-01-20 at 9.41.24 AM.png]]
### STUN (Session Traversal Utilities for NAT)
- lightweight why because only function is to let ourselves know what our public IP / Port trough NAT is.
- Does not work for Symmetric since we are getting packet with our own information which 
![[Screenshot 2026-01-20 at 9.54.45 AM.png]]
- We send a packet to router with our private ip/port and it enclose it in public ip/port and sends to stun. Which responds back with info ( that our public presence is 5.5.5.5:3333) and router receives it back gets rid of its public ip port adn sends back to us but since we sent it as packet its info was encrypted we can now knw our public presence i.e 5.5.5.5:3333 
![[Screenshot 2026-01-20 at 10.02.06 AM.png]]
##### Detailed breakdown
How the Information Survives the Router 
- **The IP Header (Modified):** When the STUN server sends the response, the packet's destination is your **Public IP**. Your router receives it, looks at its NAT table, and changes that destination to your **Private IP** so your computer can receive it.
- **The STUN Payload (Untouched):** The STUN server doesn't just send a raw packet; it writes your public IP/port into a specific field called the `XOR-MAPPED-ADDRESS` attribute inside the packet's data section.
- **Why the Router Ignores the Payload:** Most routers only look at the **Headers** (Layer 3/4) to decide where to send a packet. They do not typically open and rewrite the actual data (Layer 7) inside. Therefore, when the packet arrives at your machine, your application opens the data and reads the public address the server wrote there. 
###### Security Trick: XOR Mapping 

Modern STUN uses **XOR-MAPPED-ADDRESS** instead of a plain address. The server performs an "Exclusive OR" (XOR) operation on your public IP and port before sending it. This hides the IP address from some "smart" routers (called ALGs or Application Layer Gateways) that might try to "help" by scanning the data for IP addresses and rewriting them back to local ones, which would break the STUN discovery process. 

Summary of the Discovery 

1. **Server sees:** Packet coming from `Public IP: 1.2.3.4`.
2. **Server writes:** `1.2.3.4` into the **STUN message body**.
3. **Router changes:** Only the **Packet Header** from `1.2.3.4` → `192.168.1.5`.
4. **Client receives:** A packet addressed to `192.168.1.5`, but it opens the body and reads "Your public address is `1.2.3.4`".
#### STUN When it works
![[Screenshot 2026-01-20 at 10.16.52 AM.png]]
- The image shows for Full Cone example but in case of Address Restricted NAT both machines will have to establish communication prior to connecting with each other somehow so that respective Router table have entries for them and then they can connect seamlessly.
#### STUN when it does not works
- ![[Screenshot 2026-01-20 at 10.19.18 AM.png]]
- After they know their public presence they use [[#Signalling]] to send this info to each other and then they can connect directly if Full Cone or Address Restricted NAT.
 - In case of Symmetric NAT since server B ( let say one with Symmetric NAT ) sent packet to STUN and has its exact entry when it would see a packet from Server A ( Full Cone NAT ) it would panic and say Who the hell are you, i cannot allow you
- thus it cannot work with STUN, that is where [[#TURN ( Traversal Using Relays around NAT )]] comes.

### TURN ( Traversal Using Relays around NAT )
![[Screenshot 2026-01-20 at 10.42.12 AM.png]]
- ![[Screenshot 2026-01-20 at 10.43.06 AM.png]]
- TURN server allows communication even between server sitting behind Symmetric NAT since 
### ICE ( Interactive Connectivity Establishment)
- What does ICE do ?
- It finds the best path for two peers to connect with each other ? How
- It collects things like Public IP addresses, Reflexive adresses ( Stun ones ) and relayed addresses ( TURN ones )
- Each of these are called ICE Candidates.
- Finally we send details to the Peers via SDP

### SDP ( Session Description Protocol )
- SDP can be customised as well like Discord customised SDP for their use case.
- ![[Screenshot 2026-01-20 at 11.00.43 AM.png]]
- After we have the long string SDP provides us, now comes the part to send it ? Signalling 
### Signalling
- One ICE collects all the possible or available candidates for communication
- We create the SDP and send it to other peer ( no matter the protocol or the method of communication just send it ).
- ![[Screenshot 2026-01-20 at 11.05.46 AM.png]]
- once the information is sent maybe using WebSockets, http etc then we can move to WebRTC 
### WebRTC Demystified
![[Screenshot 2026-01-20 at 11.08.01 AM.png]]
- B would have Local Session Description ( one about itself ) and remote Session Descritpion ( sent by other Peer or A )
- Similarly A will have its own Session Description ( Local one it sent to B) and Remote Session Description ( from Peer B ). 
### DEMO ( WebRTC )
![[Screenshot 2026-01-22 at 10.15.32 AM.png]]
- RTCPeerConnection() -> create a local connection 
- dc => lc.createDataChannel('channel') -> we are gonna communictae through it.
- dc.onmessage -> print message
- dc.onopen -> log when connection opens
- lc.onicecandidate -> Re print SDP whenever we get a new ICE candidate i.e lc.localDescription -> Its local SDP
- lc.createOffer -> create offer, setLocalDescription() i.e set local SDP and since its promise use .then()
- We get Reprint SDP , copy the object ( ICE Candidate Details ) and paste it to another browser and assign to const offer there.
- Then similar to first browser we will rerint ICE Candiate discover using rc.onicecandidate
- for receving dataChannel we will use `rc.onDataChannel` and define rc.dc ( dc as property on rc ), with onmessage and onopen fucntions 
- rc.setRemlteDescritpion(offer).then(a => console.log("offer set"))
- rc.createAnswer().then(e => rc.setLocalDescription(a)).then(a => console.log("answer created"))
- It would response with SDP reprint
- then go back to broswer A and 
- const answer set the JSON object as answer 
- lc.setRemoteDescription(answer)
- booom Connection Opened
#### Issue 
- for my case i am seeing error: ==WebRTC: ICE Failed, add a stun server==

### WebRTC Pros and Cons
![[Screenshot 2026-01-22 at 11.11.54 AM.png]]
### Adding a new ICE Candidate after we have already sent SDP
![[Screenshot 2026-01-22 at 11.16.54 AM.png]]
- So if we discover new ICE Candidate we can copy the object and send to other part and set new ICE Candidate using `addIceCandidate` .
### Set custom TURN and STUN servers
![[Screenshot 2026-01-22 at 11.19.25 AM.png]]![[Screenshot 2026-01-22 at 11.19.55 AM.png]]
- Some public stun servers we can use 
![[Screenshot 2026-01-22 at 11.20.17 AM.png]]