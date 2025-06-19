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

# reload systemd
sudo systemctl daemon-reload
# start service
sudo systemctl start frontend.service
sudo systemctl start backend.service
# set to start automatically at boot
sudo systemctl enable frontend.service
sudo systemctl enable backend.service
# check the state of the service
sudo systemctl status frontend.service
sudo systemctl status backend.service
# disable automatically at boot
sudo systemctl disable frontend.service
sudo systemctl disable backend.service


