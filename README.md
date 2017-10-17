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
6. Run `/usr/local/sbin/clamd` or with sudo if for some reason your system asks for it.
7. Enjoy!

This part is being edited as I write the installer. So don't be too reliant on it. py2 is not supported because it has too many conflicting issues (i.e.: unicode). So.. I do not support use with py2.

### AUTHORS

* [Sifer Aseph](https://github.com/Surufel)

### TODO

1. icon for app
2. Test on a Windows and Linux machine.
3. color theme
4. Hash
5. TensorFlow
7. setuptools_scm
8. http://www.tkdocs.com/tutorial/menus.html#platformmenus (this will come much later, I need a Windows machine to develop and test this on)
9. https://www.athenic.net/posts/2017/Jan/21/preventing-sql-injection-in-python/ I'm aware. Just need time to do the other stuff first.
10. list of things I need to take care of that are foundational to SiferCore: need access to kernel APIs, watch (process, threads, image files such as DLLs, filesystems), userland protection and self protection, and the analysis engine itself
11. web-based scanner? need to discuss this because that would mean even more ambitious goal plus I have to worry about against me via web
12. LoC 200 vs 1000
13. write application log for scan activities

### Credit

1. virussignatures.strings from http://www.nlnetlabs.nl/downloads/antivirus/antivirus/virussignatures.strings
