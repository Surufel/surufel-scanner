# surufel-scanner

### Status

Still actively **developed** and **supported**.

### License

GNU General Public License v3.0

### Quick Start

This instruction works for Mac. Its equivalent should work for Linux and Windows but if there is any problem, please let me know.
There are two methods. You can install it via the installer **or** do the following:

1. Make sure you have Python (3) and pip installed.
2. Make sure you have installed [ClamAV](https://www.clamav.net).
3. `pip3 install pyclamd`
4. In /usr/local/etc/clamav, rename clamd.conf.sample to clamd.conf. Rename freshclam.conf.sample to clamd.conf.
5. In the two files, comment out "Example."
6. For clamd.conf:
    * LocalSocket /tmp/clamd.socket
    * TCPSocket 3310
7. Run `freshclam`.
8. Run `sudo /usr/local/sbin/clamd`.
9. Enjoy!

### AUTHORS

* [Sifer Aseph](https://github.com/Surufel)
* [Ayush Byat](https://github.com/AyushBhat) (for list_files.py)

### TODO

1. Develop installer.
2. Double clicking on an icon should start app.
3. Typing "surufel" should start app.
4. The files in data are tentative.
5. The license might be tentative.
6. Test on a Windows and Linux machine.
7. Write Quick Start instructions for Windows and Linux machine.
8. Turn reload into a button.
9. Turn scandirs into a button or two.
10. Hash.
11. TensorFlow.
12. PostgreSQL.
