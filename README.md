# AF Discovery -- Segmenting Ultrasound (US) Images for Amniotic Fluid (AF) - An AI4GoodLab 2023 Project
This repository contains the code and documentation for the team **AF Discovery**, part of the **AI4GoodLab** 2023 initiative. Our team of five, along with our TA, completed this project within a three-week timeframe. The technical description is *"Machine Learning Pipeline for Segmenting Ultrasound (US) Images to Assess Amniotic Fluid (AF)"*.

![Picture8](https://github.com/mehjabin-rahman/ultrasound-image-segmentation-classification/blob/main/workflow.png)

## Our Mission
We are **AF Discovery**, dedicated to enhancing patient care for expectant mothers by equipping clinicians with a machine learning solution that facilitates timely and confident decision-making.

## Importance of **AF Discovery**
Amniotic fluid surrounds a developing fetus and its volume is critical for fetal health. Both excessive and insufficient amniotic fluid levels can lead to serious complications requiring urgent medical intervention. 

For instance, low amniotic fluid volume (AFV) may necessitate time-sensitive decisions such as induced labor or cesarean delivery. With over 280 million women facing AFV-related complications annually, accurate and timely assessments are essential.

Currently, AFV calculations are performed manually by ultrasound technicians and physicians, which is time-consuming and subject to human error. In low-resource settings, the lack of time often leads to visual assessments rather than precise calculations.

Our solution leverages machine learning to segment fetal ultrasound images and determine AFV in real-time, thereby saving valuable time and resources for healthcare providers and empowering patients to make informed decisions.

## Development and Training Process
We have developed a supervised deep learning convolutional neural network model, known as U-NET, to segment 2D fetal ultrasound images and a regression model to predict outcomes.

Due to the unavailability of a labeled AFV ultrasound dataset, we utilized a similar dataset of fetal head ultrasound images. Our UNET model was trained on this dataset, which was divided into labeled training and test sets. The regression model was subsequently trained using clinical measures associated with the training images. This pipeline can be adapted for AFV datasets in the future.

The fetal head images were annotated for head circumference and preprocessed before being input into the UNET model. The regression model then utilized the UNET's segmentation predictions to estimate outcomes, specifically predicting fetal head circumference.

## Model Performance
While our model successfully segments fetal head ultrasound images, there is potential for improvement. Various similarity coefficients suggest that our prediction accuracy can be enhanced. Future steps will focus on refining our model and adapting it for AF datasets.

## Using the AF Discovery WebApp
Users can upload screenshots of their ultrasound images and receive predicted AFV results within moments. This functionality could be extended to live video feeds, enabling real-time segmentation of ultrasound features in the future.

---

## Technologies Utilized
- Machine Learning Framework: TensorFlow
- GPU: Google Colab
- Development Environments: Colab, Jupyter, Spyder
- Code Sharing Platforms: Colab, Google Shared Drive, GitHub
- Serverless Architecture
- Mock-up Design: Figma
- Front-end Deployment: Gradio

## Dataset Acknowledgment
We acknowledge the dataset provided by Thomas L. A. van den Heuvel, Dagmar de Bruijn, Chris L. de Korte, and Bram van Ginneken in their publication titled "Automated Measurement of Fetal Head Circumference Using 2D Ultrasound Images" [Data set]. This dataset, available at Zenodo (http://doi.org/10.5281/zenodo.1322001), was instrumental in training our machine learning models.

## References
- Thomas L. A. van den Heuvel, Dagmar de Bruijn, Chris L. de Korte, and Bram van Ginneken. Automated measurement of fetal head circumference using 2D ultrasound images [Data set]. Zenodo. http://doi.org/10.5281/zenodo.1322001
- arXiv:2303.07852 [eess.IV] https://doi.org/10.48550/arXiv.2303.07852

