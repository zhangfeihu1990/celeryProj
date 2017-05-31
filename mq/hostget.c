#include<sys/utsname.h>
#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>

int main()
{
    char computer[256];
    struct utsname uts;
 
    if(gethostname(computer, 255) != 0 || uname(&uts) < 0){
        fprintf(stderr, "Couldnot get host infomation\n");
        exit(1);
     }
     
     printf("Computer hostname is %s\n", computer);
     exit(0);
}
