import os
import generator
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import io
import base64
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index(seed = None, artvalue: float = None):
    return {"img": generate_image(seed, artvalue)}

def generate_image(seed = None, artv = None):

    # get generator specific args
    gen_args = {'TRUNCATION':artv,'seed':seed}

    ### generate waifu ###
    # get session
    sess = generator.load_model('./twdne3.onnx')

    # run inference
    pred = generator.run_inference(sess, **{k: v for k, v in gen_args.items() if v is not None})

    # post process
    arr = generator.post_process_preds(pred)
    im = Image.fromarray(arr)

    # send waifu
    in_mem_file = io.BytesIO()
    im.save(in_mem_file, format = "PNG")
    in_mem_file.seek(0)
    img_bytes = in_mem_file.read()
    base64_encoded_result_bytes = base64.b64encode(img_bytes)
    base64_encoded_result_str = base64_encoded_result_bytes.decode('ascii')

    # # save waifu
    # dirname = os.path.dirname(__file__)
    # filename = 'docker_waifu'
    # if gen_args['seed'] is not None:
    #     filename = gen_args['seed']
    # output_filepath = os.path.join(dirname,f'{filename}.png')
    # im.save(output_filepath)

    return base64_encoded_result_str
