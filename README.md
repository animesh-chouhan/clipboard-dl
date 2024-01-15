# clipboard-dl

Download files just by copying the link

## Usage

Useful for downloading images and videos by running the script in background and copying the links to clipboard. You can set the delays or modify the code to suit your needs. You can also ignore the errors and just log them instead of exiting the program by setting the `ignore_errors` flag in the script.

Copy `clipboard-dl.py` in the directory where you want to download the links and run the following command:

```sh
pip3 install pyperclip wget
python3 clipboard-dl.py
```

## Example output

```sh
animesh@pop-os:~/Github/clipboard-dl$ python3 clipboard-dl.py
100% [..................] 22245 / 22245e0f82885392ca506dfcb15d35efdacdb.jpg
100% [..................] 36413 / 36413360_F_595866810_5MUb99dOylJIuvU2mcDDpkx6qj4WdS7c.jpg
100% [..................] 43184 / 43184wwbS4K64XJjl5O215tE8sJ_geRGwCmgYQ3RXJxZTwR4.jpg
100% [..................] 15688 / 156884a9s4018ht791.png
Invalid url
Exception: HTTP Error 403: Forbidden
```
