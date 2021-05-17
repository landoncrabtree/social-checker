# social-checker
Bulk check popular social media sites for username avaibility. 

Supports Instagram, Steam Community, Instagram, Minecraft, and GitHub.
All available names are output to "available.txt". 

1. Download `social-checker-master.zip` from the releases page.
2. Run `pip install requests` or `python3 -m pip install requests` in terminal.
3. Unzip the `social-checker-master.zip`.
4. Make the unzipped folder your current/active directory.
5. Add HTTPS proxies into "proxies.txt". 
6. Start the program by running `python3 <script>`. For example, `python3 instagram.py`
  
It'll then ask for the wordlist, so just enter that. All wordlists are found in the `wordlists/` directory. You can create your own wordlists. When entering the wordlist, you do **not** need to specify a path/, just enter the file name alone: ie, enter `3char.txt`.


I recommend https://proxy.webshare.io for HTTP(S) proxies. I've used them personally, and the speeds are great and entirely exclusive to oyu.
