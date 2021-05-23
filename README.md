# TWDNE API

API to generate anime faces and return them encoded in base64 strings. GAN for anime faces was made by [Gwern](https://www.gwern.net), check out his work with [This Waifu Does Not Exist website](https://www.thiswaifudoesnotexist.net/).
 
## Usage

**1) GAN Model download**
- Download the TWDNE3.onnx model from https://hivemind-repo.s3-us-west-2.amazonaws.com/twdne3/twdne3.onnx and move it to your project repo
- If that's no longer active, look for an update on https://www.gwern.net/Faces

**2) Option 1: Using Docker**
- Build the docker image `docker build -t myimage ./`
- Run the image exposing a port, e.g. `docker run -p 80:80 myimage`

**2) Option 2: Python**
- Install the requirements
- Add gunicorn or some other dependency to run the fastapi server
- On MacOS you may need to install OpenMP `brew install libomp`

**3) Send get requests**
- Send a get request with optional parameteres
- An empty get requests runs the generation with a random seed and the default 0.7 "artistic value", e.g. `http://localhost`
- With the seed parameter it generates the image with that seed `http://localhost?seed=SomeString`, with the same seed you always get the same image
- With the artvalue parameter you can change the above-mentioned value `http://localhost?artvalue=0.85` (above 1.2 it gets really crazy)
- You can combine them to use both features, `http://localhost?seed=SomeString&artvalue=0.85`

**Bonus**
By uncommenting the lines above the return statement in `main.py` you can save the images. 
If using docker you must add a volume to save them in your file system.

## Credits
This project originated from [jfreds91's waifu_bot](https://github.com/jfreds91/waifu_bot) for discord.
The code in the generator.py and part of main.py is from that repo.
