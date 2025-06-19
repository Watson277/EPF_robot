# frontend service 
sudo nano /etc/systemd/system/frontend.service

[Unit]
Description=Vue Frontend Dev Server
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/my_project/frontend
ExecStart=/bin/bash -c 'npm run dev'
Restart=always

[Install]
WantedBy=multi-user.target

# backend service 
sudo nano /etc/systemd/system/backend.service

[Unit]
Description=My Backend Python Service
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/my_project/backend
ExecStart=/usr/bin/python3 /home/pi/my_project/backend/main.py
Restart=always

[Install]
WantedBy=multi-user.target

