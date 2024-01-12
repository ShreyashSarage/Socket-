# Socket Creation in c

![!](https://static.javatpoint.com/cpp/images/socket-programming-in-c-or-cpp.png "Socket Creation")

```
int socket = socket(family,type,proto);
```
## socket:
socket discriptor, an integer(like a file handle)

#### family
integer, commmon domain eq
function return  -1 upon failure

#### type
##### communication types
1. SOCK_STREAM
2. SOCK_DGRAM

#### Proto
1. IPPROTO_TCP, IPPROTO_UDP


Socket calls doesnot specify where data will be coming from, nor where it will be going to, it just creates the interface

### specifying addresses (Sockaddr)
2.
 ```Struct sockaddr_in{
    unsigned short sin_family;
    //interrupt protocol(AP_INET)
    unsigned short sin_port;
    //address port is 16 bit
    struct in_addr sin_addr;
    //internet address 32 bits
}
Struct in_addr{
    unsigned long s_addr;
    //internet address of 32 bits
}
```

### bind();
associates and reserves port for use by the socket

```
int status = bind(sockid,&addrport,size);
```
#### addrport 
ip address of port of machine

#### size 
The size in (bytes) of the addrport structure

upon failure it will return **-1**

#### Bind can be skipped for both type of sockets

#### DGRAM
if only sending no need to bind <br>
-> the os finds a port each time a socket sends a packet<br>
-> if receiving you need to bind 

#### Stream(Flow)
-> Destination is determined during connection setup <br>
-> Don't need to know port sending from <br> **(because during connection setup receiving end is informed about port)**

## Listen();
```
int status = listen(sockid,queuelimit);
```
#### queue limit
1. queue limit -> no. of active participants that can wait for a connection
2. status -> 0,if listning
          -> -1,if error
3. listen() is non-blocking(returns immediately)

## listning
-> is never used for sending and receiving
-> used by the server only as a way to get new sockets


## Connect():
-> The client establishes a connection with the server by calling "connect()"

```
int status = connect(sockid,&foreignAddr,addrlen);
```
1. foreignAddr => (struct sockAddr) means address of the passive participant 
2. addrlen => interger, sizeof(name) <br>
**_If status 0 = success, <br>1 = failure_** 

## Accept():
```
int status = accept(sockid, &clientaddr,&addrlen);
```
#### clientaddr
-> addresss of active participant
-> accept call is blocking

#### addrlen
-> sizeof(client_addr)


## Send and Receive(STREAM)
```
int count = send(sockid,msg,msgLen,flags);
```
-> **msg** : const void[], meddage to be transmitted
-> **msgLen** : int, length of message(in bytes) to transmit.
-> **flags** : special options (**normally zero**)

**_return -1,if error_**

```
int const = recv(sockid,recvBuffer,buflen,flags);
```

-> **recvbuf** : void[], stores receiving bytes
-> **buflen** : bytes received
-> **flags** : special options (**normally zero**)

### DGRAM
```
int const = sendto(sockid,msg,msgLen,flags,&foreignAddr,addrlen);
```
```
int count = recfrom(sockid,recvBuf,buflen,flags,&clientAddr,adrlen);
```
## close()
```
int status = close(sockid);
```

