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
