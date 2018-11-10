- shell 调用python
```
#! /usr/bin/bash
echo "hello world"

python <<-EOF
print ("hello world!")
EOF

echo "hello world"                   
```
```
hello world
hello world!
hello world
```
