# cli-pylogin
small CLI authentification pyhon program 

The program has a hardcoded admin user inside the script (!bad practice) with credentials `root:root`

Passwords are not saved, they are instantly converted to SHA-2 hash and stored inside a file `db.txt` in a format `login::hash`
Login function is based on entries to the `db.txt`
