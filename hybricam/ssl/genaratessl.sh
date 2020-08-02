openssl req -newkey rsa:4096 \
            -x509 \
            -sha256 \
            -days 3650 \
            -nodes \
            -out /home/jonnydoyle/Code/clients/fabrizio/hybricam/ssl/example.crt \
            -keyout /home/jonnydoyle/Code/clients/fabrizio/hybricam/ssl/example.key