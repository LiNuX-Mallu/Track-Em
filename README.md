<h1 align="center" width="100%">Track-Em</h1>
<img src="logo.jpeg" alt="logo" width="100%" height="auto">
<h3 background-color="black" align="center">GPS Location Tracker Using Malicious URL</h3>
<br>
<h2>ABOUT TRACK-EM</h2>
<p width="100%">This Tool can be used to Track location of an 
Android or ios or any other Devices which support 
Geolocation . We use Javascript Geolocation api along with django-framework for  
this attack . To know more about Geolocation api 
click <a href="https://www.w3.org/TR/geolocation/">here</a> .
Tool aimed on educational purpose any misuse from 
users are upto them .
<br>
<h3>Requirements</h3>
<p>active internet connection</p>
<p>linux platform</p>
<p>hotspot needed if Termux</p>
<br>
<h2>Installation</h2>
<h3>Linux/Termux</h3>
<p>$ apt install git python</p>
<p>$ git clone https://github.com/KOMIK3R/Track-Em.git</p>
<p>$ cd Track-Em</p>
<p>$ pip install -r requirements.txt</p>
<p>$ python track.py</p>
<br>
<h3>How To ?</h3>
<p>- in PORT input try a 4 digit port from range 8000 to 9000 .</p>
<p>- try different one if get "port already in use" error .</p>
<p>- wait until connect .</p>
<p>- send the public url to victim .</p>
<p>- you will get a Location red marked google map link once victim open the link .</p>
<br>
<h3>Ngrok Tips</h3>
<p>- we use pyngrok so no need to install ngrok separately .</p>
<p>- try turning on hotspot if you are using Termux .</p>
<p>- try running command <b>"$ export USER=root "</b> if facing <b>"cant find home directory" warning</b> .</p>
<p>- it is always better with authtoken . here is the command <b>"$ pyngrok authtoken your_token "</b> </p>
