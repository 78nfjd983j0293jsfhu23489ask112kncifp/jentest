![](static/img/logo.png)


Inspiration
Breast cancer is worst nightmare of women for centuries. It is really hard to identify in advance and also requires expert doctors. Most of the countries are not well developed or under-developed to provide medical devices to local clinics,hospitals which makes doctor check-up unaffordable or lack for women . Also non-professional doctors are facing with huge challenge in breast cancer identification process.

After making examinations doctors still are not 100% sure to diagnose patient with breast cancer. It is meticulous process and they should take into account all tests. So they need AI based assistant to help them to speed up this process and make decision making process easier and much more effectively.

To address all the problems indicated above we created simple solution solves all. For doctors AI based mammogram analyzer & ultrasonic analyzer with high accuracy. By some estimates, diagnostic errors for medical patients in a general range anywhere from 10% to 28%.

What it does
Identifies most cancer likely areas from given ultrasonic, x-ray images. In nice web application provides functionality and easy to use.

How we built it
There are 2 different architectures used. Pytorch used for all deep learning related tasks. Opencv needed for preprocessing and postprocessing of input and output respectively. Flask used for simple Python web-server. Numpy used for tensor to matrix operations.

U-net based network implemented from scratch for lump segmentation from ultrasonic imagery. Pretrained VGG16 network used for x-ray heatmap generation and segmentation task. Grad-Cam method used to display activation on given input image.

![](https://user-images.githubusercontent.com/39130214/140176829-1a4a237f-c659-4aee-9b26-5717f650b7ae.png)

Challenges we ran into
Worked under extreme time and limited resource pressure. Data was huge problem most of the public datasets are either in low quality or too less to train network work on it. Heavy data augmentations applied. Idea was so raw initially but evolved to its best state. Another challenge was participating alone I joined hackathon so recently it took about 3-4 full days to complete all these things frontend,backend and AI part made by me.

Accomplishments that we're proud of
Learned and implemented U-Net network from scratch also implemented Grad-CAM technique. Finished in time in its best form. Pushed my limits as much as I can to provide better and better for this product. Worked as an individual did my best.

What we learned
Time management, Grad-Cam technique, improved backend programming and sharpened pytorch skills.

What's next for Mamma AI
Improving current AI Integrating more medical machine learning models. Adding more features to the app. Recruiting medical experts, doctors, and patients.
