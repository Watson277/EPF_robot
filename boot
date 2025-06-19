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
ExecStart=/usr/bin/python3 /home/epf/robot/EPF_robot-Watson277-speakcommand-1/backend/main.py
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
nano ~/.config/lxsession/LXDE-pi/autostart
@chromium-browser --noerrdialogs --kiosk http://localhost:5173





# trash error code
× backend.service - My Backend Python Service
     Loaded: loaded (/etc/systemd/system/backend.service; enabled; preset: enabled)
     Active: failed (Result: exit-code) since Thu 2025-06-19 10:12:53 CEST; 11min ago
   Duration: 301ms
   Main PID: 3952 (code=exited, status=1/FAILURE)
        CPU: 292ms

Jun 19 10:12:53 raspberrypi systemd[1]: backend.service: Scheduled restart job, restart counter is at 5.
Jun 19 10:12:53 raspberrypi systemd[1]: Stopped backend.service - My Backend Python Service.
Jun 19 10:12:53 raspberrypi systemd[1]: backend.service: Start request repeated too quickly.
Jun 19 10:12:53 raspberrypi systemd[1]: backend.service: Failed with result 'exit-code'.
Jun 19 10:12:53 raspberrypi systemd[1]: Failed to start backend.service - My Backend Python Service.
