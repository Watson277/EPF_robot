# frontend service 
sudo nano /etc/systemd/system/frontend.service

[Unit]
Description=Vue Frontend Dev Server
After=network.target

[Service]
Type=simple
User=epf
WorkingDirectory=/home/epf/robot/EPF_robot-Watson277-speakcommand-1/frontend
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
User=epf
WorkingDirectory=/home/epf/robot/EPF_robot-Watson277-speakcommand-1/backend
ExecStart=/home/epf/anaconda3/envs/robot/bin/python  /home/epf/robot/EPF_robot-Watson277-speakcommand-1/backend/main.py
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

# open the browser
mkdir -p /home/epf/.config/lxsession/LXDE-pi
nano /home/epf/.config/lxsession/LXDE-pi/autostart

@chromium-browser --noerrdialogs --disable-infobars --kiosk http://localhost:5173






