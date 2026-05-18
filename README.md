# codespaces

nc host3.dreamhack.games 14894


ssh chall@host8.dreamhack.games -p 8729


sudo tee /etc/nginx/sites-available/wargame << 'EOF'
server {
    listen 80;
    location / {
        proxy_pass http://host8.dreamhack.games:12218;
        proxy_http_version 1.1;
        proxy_set_header Host $proxy_host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
EOF