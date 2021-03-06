
all:
	python3 coin/coin.py &

install:
	sudo apt-get install python3-gi python3-requests python3-yaml python3-notify2
	dconf reset -f /org/nil/coinprice/
	sudo cp resources/org.nil.indicator.coinprice.gschema.xml /usr/share/glib-2.0/schemas/
	sudo glib-compile-schemas --strict /usr/share/glib-2.0/schemas/
	sudo chmod u+x coin/coin.py

many:
	python3 coin/coin.py file=startmany.yaml &