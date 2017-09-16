# surufel-scanner

### Status

Still actively **developed** and **supported**.

### License

GNU General Public License v3.0

### Quick Start

This instruction works for Mac. Its equivalent should work for Linux and Windows but if there is any problem, please let me know.
There are two methods. You can install it via the installer **or** do the following:

1. Make sure you have installed [ClamAV](https://www.clamav.net).
2. In /usr/local/etc/clamav, rename clamd.conf.sample to clamd.conf. Rename freshclam.conf.sample to clamd.conf.
3. In the two files, comment out "Example."
4. For clamd.conf:
    * LocalSocket /tmp/clamd.socket
    * TCPSocket 3310
5. Run `freshclam`.
6. Run `sudo /usr/local/sbin/clamd`.
7. Enjoy!

This part is being edited as I write the installer. So don't be too reliant on it.

### AUTHORS

* [Sifer Aseph](https://github.com/Surufel)

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
10. Hash
11. TensorFlow
12. PostgreSQL
13. setuptools_scm
14. http://www.tkdocs.com/tutorial/menus.html#platformmenus (this will come much later, I need a Windows machine to develop and test this on)

### Credit

1. virussignatures.strings from http://www.nlnetlabs.nl/downloads/antivirus/antivirus/virussignatures.strings
