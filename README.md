# contained

![Mediamodifier-Design](public/Mediamodifier-Design.svg)

> ###### "Containerize and Terminalize your Browsing."


Contained is a tool that runs on a docker container from the command line written in Python which is meant to function as a web browser.

To install, run:

```bash 
sudo apt install docker.io
git clone https://github.com/linuxfandudeguy/contained
cd contained
sudo docker build -t contained .
sudo docker run --rm -it contained https://example.com
```

Now have a copy of contained running on your computer. (linux based systems only)
