import argparse
import os
import generator
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import io
import base64

parser = argparse.ArgumentParser(description='twdne CLI')
parser.add_argument('-s', type=str, dest='seed', nargs='+',
	help='optional seed string')
parser.add_argument('-t', type=float, dest='TRUNCATION',
	help='truncation value to use. Defaults to None to use package default')

# handle arguments
args = vars(parser.parse_args())
if isinstance(args['seed'], list):
	args['seed'] = ' '.join(args['seed'])

# get generator specific args
gen_args = {
	'TRUNCATION':args['TRUNCATION'],
	'seed':args['seed']
}

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

print(f'img: {base64_encoded_result_str}')
# # save waifu
# dirname = os.path.dirname(__file__)
# filename = 'docker_waifu'
# if gen_args['seed'] is not None:
#     filename = gen_args['seed']
# output_filepath = os.path.join(dirname,f'{filename}.png')
# im.save(output_filepath)
# print(f'saved: {output_filepath}')


# with(open(output_filepath, 'r')) as file:
#     png = file.read()

# return png
