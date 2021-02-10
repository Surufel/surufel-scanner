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
* Ayush Bhat

### TODO

3. Hash
4. TensorFlow
5. setuptools_scm
6. http://www.tkdocs.com/tutorial/menus.html#platformmenus (this will come much later, I need a Windows machine to develop and test this on)
7. https://www.athenic.net/posts/2017/Jan/21/preventing-sql-injection-in-python/ I'm aware. Just need time to do the other stuff first.
8. list of things I need to take care of that are foundational to SiferCore: need access to kernel APIs, watch (process, threads, image files such as DLLs, filesystems), userland protection and self protection, and the analysis engine itself
9. write application log for scan activities
10. https://udacity.github.io/git-styleguide/

### Credit

1. Bombermania.exe.zip from http://www.tekdefense.com/downloads/malware-samples/
2. virussignatures.strings from http://www.nlnetlabs.nl/downloads/antivirus/antivirus/virussignatures.strings
