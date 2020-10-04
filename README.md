# Memecrypt

Memecrypt is an encryption tool designed for fun and CTF challenge use.
It can be imported as a python module or used as a standalone
program, depending on whichever is needed.

![GitHub forks](https://img.shields.io/github/forks/Sh3llcod3/Memecrypt.svg?style=for-the-badge&label=Fork)
![GitHub stars](https://img.shields.io/github/stars/Sh3llcod3/Memecrypt.svg?style=for-the-badge&label=Stars)
![GitHub watchers](https://img.shields.io/github/watchers/Sh3llcod3/Memecrypt.svg?style=for-the-badge&label=Watch)


# Usage

There are 2 main ways to use memecrypt. Both ways are covered here.

## Program use

Install from PyPi

```shell
$ python3 -m pip install memecrypt
```

#### Options

Let's start by viewing all the supported arguments.

```shell
$ memecrypt
[+] Usage: memecrypt [options]

[i] Examples:

      memecrypt -se -i foo -k bar

      memecrypt --subs -x -f file.txt -k "a_key"

      memecrypt -sx -i 'lorem ipsum' -k 'some key'

      memecrypt --subs -e -u cat.thatlinuxbox.com -k 'ascii cat'

[i] Positional arguments:

       -s --subs
              Select the substitution cipher.
       -e --encrypt
              Select encryption mode.
       -x --decrypt
              Select decryption mode.
       -k --key key
              Specify key.
       -i --input input-string
              Specify input string.
       -u --url url
              GETs data from the url.
       -f --file file-path
              Specify input file path.

[i] Optional arguments:

       -h --help
              Show this help screen and exit.
       -v --version
              Print version and exit.
       -q --quiet
              Only show output. Any errors are still displayed.
       -o --output-file file
              Specify a file to write to.
       -p --pipe-input
              Take input from stdin.
```

#### Encryption

```shell

# As an argument
$ ./memecrypt.py -se -i "foo bar" -k "lorem ipsum"
[!] Note: Please use the same key for decryption.
[+] Encrypted result:
---------------------
MHFGL1AjdjpSXXx8

# From a URL
$ ./memecrypt.py --subs --encrypt --url cat.thatlinuxbox.com --key "cat"
[+] Fetched data from URL.
[!] Note: Please use the same key for decryption.
[+] Encrypted result:
---------------------
WiJeTFoiXkxaOl5ETDpeREw6XkRMOl5ET.....(and so on).....

# From a local file
$ ./memecrypt.py -se -f <file-path> -k "foobar" -q
NWl8eSlMd35ZXTQxU289Y0ZdNGdGTCdrU2FBQ3pM...(and so on)...

```

#### Decryption

```shell

# Decrypt as an argument.
./memecrypt.py -sx -i bVQ0cjJfVkY1TGNCKFRWWzIkZVF... -k wow
[+] Decrypted result:
---------------------
Much encryption, very wow

# Decrypt from file
$ ./memecrypt.py --subs --decrypt -f ../../projects/outputfile -k lol
[+] Decrypted result:
---------------------
Cupcake ipsum dolor. Sit amet topping chocolate bar

```

#### Notes

Arguments can be placed in any order and combined however you want, as long as they don't need
a passed value or directly contradict.

## Module use

Install using `python3 -m pip install memecrypt`

#### Initialising

Let's start by creating an instance of the `meme_cipher` class.

```Python
# Import our module
import memecrypt

# Create an instance
cipher = memecrypt.meme_cipher(message=None, enc_key=None, show_colors=True)

# message is the message to work on
# enc_key is the key
# show_colors=False to turn off all colors
```

#### Setting a message

Set message using method or attribute.

```Python
# Using our previous instance
cipher.set_message("foo")

# We can access/modify this by accessing the message attribute
print(cipher.message)
# Prints: foo

# Let's try and set a blank message.
cipher.set_message(None)
# Prints: [!] Memecrypt: Plaintext/Ciphertext cannot be empty.

```

#### Setting a key

This works the same way as setting a message. We'll use
our `cipher` instance. Again, the key cannot be blank or `None`.

```Python
# Setting a key
cipher.set_key("bar")

# We can access/modify the key from the enc_key attribute
print(cipher.enc_key)
# Prints: bar

# Same as before, we can't set a blank key
cipher.set_key('')
# Prints: [!] Memecrypt: Key value cannot be empty.

```

#### Encrypting

Encrypt the values. If key or message is missing, error.

```Python
# message => foo, key => bar
cipher.encrypt()
# Returns: 'NEgydQ=='

```

#### Decrypting

Perform decryption

```Python
# message => NEgydQ==, key=> bar
cipher.decrypt()
# Returns: 'foo'

```

#### Input sources

Take input from file.

```Python
# transfer the contents of the url.
cat = cipher.fetch_url("cat.thatlinuxbox.com")
# Returns a ascii cat.
cipher.set_message(cat)
# We just set our message as the ascii cat!

# Read a local file.
foo_file = cipher.read_file("/path/to/file/file.txt")
# foo_file will have contents of file.txt

# Set our message to contents of file.txt
cipher.set_message(foo_file)

```

#### Output files

Write output to a file.

```Python
# Append to a file. Create file if file non-existent.
cipher.write_to("path/to/file/file.txt", "lorem ipsum dolor")

# Let's put our encrypted output to a file.
cipher.write_to("foo_bar.txt", cipher.encrypt())
```
