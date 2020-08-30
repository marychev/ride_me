# RideMe game with using Kivy framework.

Use packages:
* Kivy: https://kivy.org/#home
* Buildozer: https://github.com/kivy/buildozer


### Install environment:
	
	git clone https://github.com/marychev/ride_me
	cd ride_me
	python3 -m virtualenv venv
	. venv/bin/activate
	pip install -r requirements.txt


#### Run game:
	
	cd ride_me
    . venv/bin/activate
    python main.py 


#### Deploy for android

    buildozer init

Go to the *buildozer.spec* and edit it, then type

    buildozer android debug deploy run
