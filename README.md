# Code Snippets

```bash

sudo apt update && sudo apt install netcat-openbsd nginx -y

----------------------------------------------------------------------------------

nc host3.dreamhack.games 14894

----------------------------------------------------------------------------------

ssh chall@host8.dreamhack.games -p 8729

----------------------------------------------------------------------------------

sudo tee /etc/nginx/sites-available/wargame << 'EOF'
server {
    listen 80;
    location / {
        proxy_pass http://host8.dreamhack.games:8689/;
        proxy_http_version 1.1;
        proxy_set_header Host "localhost";
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
EOF

sudo ln -s /etc/nginx/sites-available/wargame /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo service nginx start

----------------------------------------------------------------------------------

docker build .

docker images -a

docker run -it 0e760fdfbc48 /bin/bash

```