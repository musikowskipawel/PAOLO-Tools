# PAOLO-Tools
It's for [Okuma-Reader](https://github.com/DrMint/Okuma-Reader)<br><br>
This tool should make all-ready volume, from just collection of randomly downloaded manga folders
99% of the code is copied from [Okuma-Tools](https://github.com/DrMint/Okuma-Tools)

### Example Directory:
	- some folder/
		- ULTRAAWESOMEMANGA/
			- 001 CHAPTER of this awesome manga and stuff/
				- 00001.jpg
			- 002 CHAPTER of this awesome manga and stuff/
				- 00001.jpg
			- 002.5 CHAPTER some ultra special chapter /
				- 00001.jpg
		- PAOLO-Tools.py
		
### Example Command:
	- PAOLO-Tools.py ULTRAAWESOMEMANGA 1
	
### What it creates in Example Directory:
	- some folder/
		- etc.
		- etc.
		- 1/
			- 1/
				- 1.webm
				- 2.webm
				- etc.
			- 2/
				- 1.webm
				- 2.webm
				- etc.
			- config.json
		- PAOLO-Tools.py
			
____________________________________________________________________________________

# maker.py

It adds manga/book to the library.

### Args:
LIBRARY_FOLDER, SLUG, TITLE, BOOKTYPE, VOLUMES, EXTENSION, --jp

### Example Command:
maker.py library awesome-manga "Awesome Manga" manga 1 .webm --jp


