# import the frameworks, packages and libraries 
import streamlit as st 
from PIL import Image 
from io import BytesIO 
import numpy as np 
import cv2 # computer vision 

# function to convert an image to a 
# water color sketch 

def convertto_watercolorsketch(inp_img): 
	img_1 = cv2.edgePreservingFilter(inp_img, flags=2, sigma_s=50, sigma_r=0.8) 
	img_water_color = cv2.stylization(img_1, sigma_s=100, sigma_r=0.5) 
	return(img_water_color) 

def median_blur_pencil_sketch(image):
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Median blur
    blurred_image = cv2.medianBlur(gray_image, 21)

    # Invert the blurred image
    inverted_blurred = cv2.bitwise_not(blurred_image)

    # Create pencil sketch
    sketch_image = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    return sketch_image


# function to convert an image to a pencil sketch 
def pencilsketch(inp_img): 
	img_pencil_sketch, pencil_color_sketch = cv2.pencilSketch( 
		inp_img, sigma_s=50, sigma_r=0.07, shade_factor=0.0825) 
	return(img_pencil_sketch) 

def Gaussian_pencil_sketch(inp_img):
    # Convert to grayscale
    gray_image = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    # Invert the blurred image
    inverted_blurred = cv2.bitwise_not(blurred_image)
    # Blend with the original grayscale
    sketch_image = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    return sketch_image


def apply_advanced_oil_painting_effect(inp_img):
    stylized_effect = cv2.stylization(inp_img, sigma_s=60, sigma_r=0.6)
    gray_image = cv2.cvtColor(stylized_effect, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
    edges = cv2.Laplacian(blurred_image, cv2.CV_8U, ksize=5)
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    edges_inverted = cv2.bitwise_not(edges_colored)
    combined_result = cv2.bitwise_and(stylized_effect, edges_inverted)
    return combined_result

# function to load an image 
def load_an_image(image): 
	img = Image.open(image) 
	return img 

# the main function which has the code for 
# the web application 
def main(): 
	
	# basic heading and titles 
	# st.title('WEB APPLICATION TO CONVERT IMAGE TO SKETCH') 
	# st.write("This is an application developed for converting your ***image*** to a ***Water Color Sketch*** OR ***Pencil Sketch***") 
	st.title('Artistic Image Transformation - Sketches & Paintings')
	st.write("Convert your images to a **Watercolor Sketches**, **Pencil Sketches**, or stunning **Oil Paintings** with just a few clicks.")
	st.subheader("Please Upload your image") 
	
	# image file uploader 
	image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"]) 

	# if the image is uploaded then execute these 
	# lines of code 
	if image_file is not None: 
		
		# select box (drop down to choose between water 
		# color / pencil sketch) 
		option = st.selectbox('How would you like to convert the image', 
							('Convert to water color sketch', 
							'Convert to pencil sketch', 
							'Convert to oil sketch' , 
							'Convert to Gaussian pencil sketch',
							'Convert to Median pencil sketch'
							)) 
		if option == 'Convert to water color sketch': 
			image = Image.open(image_file) 
			final_sketch = convertto_watercolorsketch(np.array(image)) 
			im_pil = Image.fromarray(final_sketch) 

			# two columns to display the original image and the 
			# image after applying water color sketching effect 
			col1, col2 = st.columns(2) 
			with col1: 
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 
				st.header("Water Color Sketch") 
				st.image(im_pil, width=250) 
				buf = BytesIO() 
				img = im_pil 
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="watercolorsketch.png", 
					mime="image/png"
				) 

		if option == 'Convert to pencil sketch': 
			image = Image.open(image_file) 
			final_sketch = pencilsketch(np.array(image)) 
			im_pil = Image.fromarray(final_sketch) 
			
			# two columns to display the original image 
			# and the image after applying 
			# pencil sketching effect 
			col1, col2 = st.columns(2) 
			with col1: 
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 
				st.header("Pencil Sketch") 
				st.image(im_pil, width=250) 
				buf = BytesIO() 
				img = im_pil 
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="watercolorsketch.png", 
					mime="image/png"
				) 
		if option == 'Convert to oil sketch':
			image = Image.open(image_file) 
			final_sketch = apply_advanced_oil_painting_effect(np.array(image)) 
			im_pil = Image.fromarray(final_sketch) 
			
			# two columns to display the original image 
			# and the image after applying 
			# pencil sketching effect 
			col1, col2 = st.columns(2) 
			with col1: 
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 
				st.header("Oil Sketch") 
				st.image(im_pil, width=250) 
				buf = BytesIO() 
				img = im_pil 
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="watercolorsketch.png", 
					mime="image/png"
				)
		if option == 'Convert to Gaussian pencil sketch':
			image = Image.open(image_file) 
			final_sketch = Gaussian_pencil_sketch(np.array(image)) 
			im_pil = Image.fromarray(final_sketch) 
			
			# two columns to display the original image 
			# and the image after applying 
			# pencil sketching effect 
			col1, col2 = st.columns(2) 
			with col1: 
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 
				st.header("Gaussian Pencil Sketch") 
				st.image(im_pil, width=250) 
				buf = BytesIO() 
				img = im_pil 
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="watercolorsketch.png", 
					mime="image/png"
				) 
		if option == 'Convert to Median pencil sketch':
			image = Image.open(image_file) 
			final_sketch = median_blur_pencil_sketch(np.array(image)) 
			im_pil = Image.fromarray(final_sketch) 
			
			# two columns to display the original image 
			# and the image after applying 
			# pencil sketching effect 
			col1, col2 = st.columns(2) 
			with col1: 
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 
				st.header("Median Blur Pencil Sketch") 
				st.image(im_pil, width=250) 
				buf = BytesIO() 
				img = im_pil 
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="watercolorsketch.png", 
					mime="image/png"
				)
if __name__ == '__main__': 
	main() 
