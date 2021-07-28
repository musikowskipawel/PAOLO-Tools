# PAOLO-Tools
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
		
Example Command:
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
			