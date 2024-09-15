# Format String

Mọi bài sẽ thực hiện trên file crash.c.  
2 file .py dùng để truyền input thay vì nhập echo $(python -c "print()")

Bước 1:  
````
$> docker run -it --privileged -v $HOME/Seclabs:/home/seed/seclabs img4lab

````
Bước 2: biên dịch file
````
gcc -g crash.c -o crash.o
````
Bước 3:    
````
sudo sysctl -w kernel.randomize_va_space=0 
````
Bước 4:  
chạy ctr:  
````
./crash.o
````
chạy ctr truyền sẵn input: 
````
./crash.o < badfile
````
** để biên dịch file python: python3 input.py    
** có thể dùng nano