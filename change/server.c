#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <asm-generic/socket.h>


#define PORT 8080
#define BUFFER_SIZE 1024

int main(){
    int server_fd, new_socket;
    struct sockaddr_in server , client ;
    int opt =1;
    char str[10] = "BYE";
    int addrlen = sizeof(server);
    char buffer[BUFFER_SIZE] = {0};
    printf("%s",buffer);

    //create socket file descripter
    if((server_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        perror("socket creation failed ");
        exit(EXIT_FAILURE);
    }

    //forcefully attaching socket to port 8080
    if(setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT , &opt , sizeof(opt)))
    {
        perror("Setsockopt failed");
        exit(EXIT_FAILURE);
    }
    server.sin_family = AF_INET;
    server.sin_addr.s_addr =INADDR_ANY;
    server.sin_port = htons(PORT);

    //bind the socket
    if(bind(server_fd,(struct sockaddr*)&server,sizeof(server))<0)
    {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }
    if(listen(server_fd,3)<0){
        perror("listen failed");
        exit(EXIT_FAILURE);

    }
    printf("server listening on port %d...\n",PORT);

    //Accept incoming connections
    while(1)
    {
    if((new_socket=accept(server_fd,(struct sockaddr *)&client,(socklen_t*)&addrlen))<0)
    {
        perror("Accept Failed");
        exit(EXIT_FAILURE);
        //Read message from client and send it back 
        read(new_socket, buffer,BUFFER_SIZE);
        printf("Client: %s\n",buffer);
    }
        int i =1;
        while(i==0)
        {
            if(strcmp(buffer,str))
            {
                i = 0;
                close(server_fd);
            }
        }
    }

    

    send(new_socket,buffer,strlen(buffer),0);
    printf("Message sent back to client.\n");
    // close(server_fd);
    return 0;
}   
