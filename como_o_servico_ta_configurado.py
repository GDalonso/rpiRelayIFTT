dentro da pasta (essa pasta precisa ser criada, não existe por padrão)
	``/home/pi/.config/autostart``

todos os arquivos .desktop são rodados na inicialização
Criei o arquivo
	``relaycontrol.desktop``

que roda o serviço na inicialização

conteúdo do arquivo:
	[Desktop Entry]
	Type=Application
	Name=RelayControl
	Exec=/usr/bin/python3 /home/pi/github_repos/rpiRelayIFTT/adafruit.py