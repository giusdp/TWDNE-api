# This Waifu Does Not Exist (TWDNE) API

## Usage

**GAN Model download**
- Download the TWDNE3.onnx model from https://hivemind-repo.s3-us-west-2.amazonaws.com/twdne3/twdne3.onnx and move it to your project repo
- If that's no longer active, look for an update on https://www.gwern.net/Faces#

**Option 1: Using Docker**
- Build the docker image `docker build -t myimage ./`
- Run the image exposing a port, e.g. `docker run -p 80:80 myimage`

**Option 2: Python**
- Install the requirements
- Add gunicorn or some other dependency to run the fastapi server
- On MacOS you may need to install OpenMP `brew install libomp`


### Coming soon
- Post request to give a seed (a string) and change the artistic value


## Credits
This project originated from [jfreds91's waifu_bot](https://github.com/jfreds91/waifu_bot) for discord.
The code in the generator.py and part of main.py is from that repo.
