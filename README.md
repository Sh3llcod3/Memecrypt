# Memecrypt
Memecrypt is a recreational encryption tool for encrypting and sending messages and memes between your friends.
It features a substitution cipher that is capable of encrypting and decrypting text based data from a string, an URL or a local file and a hash function that can hash input strings.

![GitHub forks](https://img.shields.io/github/forks/Sh3llcod3/memecrypt.svg?style=for-the-badge&label=Fork)
![GitHub stars](https://img.shields.io/github/stars/Sh3llcod3/memecrypt.svg?style=for-the-badge&label=Stars)
![GitHub watchers](https://img.shields.io/github/watchers/Sh3llcod3/memecrypt.svg?style=for-the-badge&label=Watch)
# Prerequisites
- A GNU/Linux based OS (Tested on Ubuntu 16.04.4 LTS)
- Bash or any other shell.
- Git installed
- Python3 installed with these modules available: random, string, sys, traceback, time, base64, requests, binascii, codecs.
# Usage
Clone the repository, then mark the file as an executable with `$ chmod +x memecrypt.py`. No superuser privilages are required.
To view all the supported arguments, simply type `$ ./memecrypt.py -h` to view all the help options.
Here's what the help screen looks like.
```
 -h --help
        Show this help screen and exit.
 -v --version
        Print version information and exit.
 -s --substitution
        Use the substitution cipher. Takes -i,-k,-u,-f,-c as valid args.
 -e --encrypt
        Specify encrypt mode for -s. Needs -i if text is entered by hand.
 -x --decrypt
        Specify decrypt mode for -s. Requires use of -c for entered text.
 -c --ciphertext ciphertext
        Specify the ciphertext to work with. Use when -x is used.
 -k --key key
        Specify the key to use. Needed, if -s is used with -e/-x mode
 -f --file file-path
        Use local file for input. Works on most functions.
 -u --url url
        cURL the contents of the URL for input. Please ensure url starts with 'http://'.
 -i --input input-string
        Specify the string on which to work on.
 -d --hash
        Hash the input specified by -i and print the digest.
 -n --number n
        Output a digest of length n (for -d).
 -r --rounds rounds
        Number of times to run input through the function (for -d)
 -q --quiet
        Less verbose output. Ideal for I/O redirection. Works on all functions.
```
# Examples
The help screen may be quite confusing, however this tool is very easy to use once you have tried it out on a couple of times. Here are a few examples of how the arguments can be used.
### Substitution Cipher
Let's check out how we can use the subsititution cipher to encrypt and decrypt data.
```bash
 $ ./memecrypt.py -s -e -i "Input string" -k "The key"
[!] Note: Please use the same key for decryption.
[+] Encrypted result: dzFcXiYtcnEiKyxTezFcIQ==

$ ./memecrypt.py -s -x -c "dzFcXiYtcnEiKyxTezFcIQ==" -k "The key"
[+] Decrypted result: Input string

$ ./memecrypt.py -s -e -u "http://cat.thatlinuxbox.com" -k "A cat has 10 lives"
[+] Successfully fetched data from url.
[!] Note: Please use the same key for decryption.
[+] Encrypted result: YEpXWmBKV1pgdlc2WnZm9TYXpvJWFCb3Judjdd.......(and so on)...

$ ./memecrypt.py -s -e -u "http://cat.thatlinuxbox.com" -k "A cat has 10 lives" -q > ascii_cat

$ ls
ascii_cat

$ ./memecrypt.py -s -x -f "./ascii_cat" -k "A cat has 10 lives"
[+] Successfully read 1548 characters from file.
[+] Decrypted result: 
**********************************************************

                     IM IN YUR COMPUTERZ...

               .__....._             _.....__,
                 .": o :':         ;': o :".
                 `. `-' .'.       .'. `-' .'   
                   `---'             `---'  

         _...----...      ...   ...      ...----..._
      .-'__..-""'----    `.  `"`  .'    ----'""-..__`-.
     '.-'   _.--"""'       `-._.-'       '"""--._   `-.`
     '  .-"'                  :                  `"-.  `
       '   `.              _.'"'._              .'   `
             `.       ,.-'"       "'-.,       .'
               `.                           .'
          jgs    `-._                   _.-'
                     `"'--...___...--'"`

                     WATCHIN YUR SCREENZ        

**********************************************************

$  ./memecrypt.py -s -x -f "./ascii_cat" -k "A cat has 9 lives"
[+] Successfully read 1548 characters from file.
[-] Invalid characters found, please check key or message.
```
The `-s` flag specifies that we are selecting the substitution cipher, `-e` puts it in encrypt mode and `-x` puts it in decrypt mode. `-i` is used in encrypt mode to specify the plaintext and `-c` is used in decrypt mode to specify the cipher text. Regardless of mode the `-u` flag will get the data from the url before encrypting/decrypting it. Similarly, irrespective of mode, the `-f` argument will read a file and encrypt/decrypt data from it. The key needs to be specified with `-k` in all cases. When encrypted, the output will be in base64.

In the first example, we are `encrypting` a string and then `decrypting` it. In the third and fourth examples we are getting data from a URL with `-u` and in the fourth example in particular, we are specifying that we only want the encrypted text with `-q`, which we are redirecting it to a file called `ascii_cat`. In the second-last example we are decrypting the contents of the `ascii_cat` file by specifying `-f`.
### Hash function
This example below shows how to hash a string.
```bash
$ ./memecrypt.py -d -i "String to be hashed" -r 32 -n 64

[+] Hash: EA63C2Cd18faAaBaC13478fB8cCf84fAB779CDfd703A35DFf49Ff3949acCE48a
[~] Rounds: 32
[~] Length: 128
[~] Input: String to be hashed
[i] Hash computed in 0.0059 seconds.

```
In this example above, we specify that we want to use the hashing algorithm with `-d`, the input string with `-i`, the number of rounds we wish to run it through the hash function with `-r` and the number of output characters with `-n 64`. The arguments can be in any order with any one taking precedence over the other. For the hash function the `-r` and the `-n` arguments are optional, they can be omitted to specify defaults of `1` and `32` respectively. Finally we could have added the `-q` argument to only print the output hash.
```bash
$ ./memecrypt.py -d -i "String to be hashed" -r 32 -n 64 -q
EA63C2Cd18faAaBaC13478fB8cCf84fAB779CDfd703A35DFf49Ff3949acCE48a
```
# Strength
This algorithm should be strong enough to keep out casual reposters. However any determined meme-stealer/cryptanalyst may be able to break this algorithm in less than 5 minutes. In such case, I recommend that you use a real encryption algorithm like `AES`.

<img src="https://bit.ly/2v1xJSn" width="500px" height="500px">
