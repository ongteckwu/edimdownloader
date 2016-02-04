# Edimdownloader
Terminal downloader for SUTD's 2016 [Edimension](https://www.edimension.sutd.edu.sg). 

(Created on: 1 February 2016; Last updated: 4 February 2016)

##What it does
`edimdownloader` downloads all your course-related documents and stores it in a nice folder-tree format.  

As file downloads are cached, it can be run again to download new files.
(Cache will still be saved upon script interrupt).

Can be set to run every xx seconds/minutes/hours to download new content. (Use Google to find out how to!)



##Getting Started
To install the package (From either **terminal** or **command prompt**):

  >For Python 2.x:
    
    pip install edimdownloader
    
  >For Python 3.x:
  
    pip3 install edimdownloader

  If you have no `pip`, visit [this link](https://pip.pypa.io/en/stable/installing/) on how to download `pip` for your os.
##Usage

    edimdownloader <username> <password> <dirname>

`<password>` - your edimension password.  
`<username>` - your edimension username.    
`<dirname>` &nbsp;  - the directory in which files are to be saved. (Path can be either absolute or relative)


**To see only new downloads on stdout**:

    edimdownloader <username> <password> <dirname> --quiet
    
`--quiet` - shuts the stdout up to a necessary (download-only) level of silence

**For advanced usage options**:
    
    edimdownloader --help

##License
MIT/X11

##Bugs or if you want to contribute

Send me a github message or contact me @ teckwu_ong@mymail.sutd.edu.sg


