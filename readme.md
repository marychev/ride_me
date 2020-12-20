# RideMe game with using Kivy framework.

Use packages:
* Kivy: https://kivy.org/#home
* Buildozer: https://github.com/kivy/buildozer
* Linux packages source: https://sources.voidlinux.org/ 

### Install environment:
	
	git clone https://github.com/marychev/ride_me
	cd ride_me
	python3 -m virtualenv venv
	. venv/bin/activate
	pip install -r requirements.txt
	python main.py 


#### Run game:

	cd ride_me
    . venv/bin/activate
    python main.py 

#### Run tests

    python -m pytest tests/

#### Deploy for android

    buildozer init

Go to the *buildozer.spec* and edit it, then type, **version**

    buildozer android debug deploy run


[Packages source](https://sources.voidlinux.org/) for some broken libs: *sdl2, sdl2_image, sdl2_ttf, sdl_mixer ...* for deployment or building. 
Path local building libs `YOUR_APP/.buildozer/android/platform/build-armeabi-v7a/packages/`

-----------

# Tasks

> Tests run: failed 4, passed 300/304. - 3:06:123

1. The road state goes to the on_wait_stop state when the power limit is reached.  
   Two events `on_wait`,` on_wait__move` are constantly alternating.
   
2. Correct, flip the `right button`. It goes over the edges.

3. Correct `on_jump` distance at length. The bike is flying too far!

4. ~~Fix bike `on_landing`. The bike flies down too slowly.~~
5. ~~Fix bike `on_landing`. Impose a height limit when there is more force than needed.~~
   * _Tests run: passed 303 - 1:20:821_

6. After the `on_jump` and `on_landing`, the bike stays on the `on_landing` event.
   The `on_relax` event should be if `speed` > 0.

7. Fix `restart game` action.

8. ~~Fix the tests of project.~~ 
   * _Tests run: passed 303 - 1:48:798_   
   -[x] `landing` - 1
   -[x] `relax` - 2 
   -[x] `stop` - 1
   
    
9. The game began to slow down noticeably. Find out and fix.
 