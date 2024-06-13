# Dreammate-Generator

**ABSTRACT**

This study aims to develop a ideal face image generation by text description. We trained a VQGAN model using the AI-Hub montage dataset and integrated this model as the encoder and decoder for the KoDALLE framework. Subsequently, we refined the output of the KoDALLE model to align with aesthetically pleasing facial features using StyleGANEX, which had been trained on CelebA dataset. This approach aimed to generate final outputs that closely resemble idealized human appearances. Despite the seamless progression during the training phase, the process was hindered by limited computational resources, preventing sufficient model training. Consequently, the validation results were suboptimal, and the final application did not produce satisfactory outcomes.

**training process**


1. Download [페르소나 기반의 몽타주 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=618)
2. Preprocess the dataset with [preprocess.ipynb](https://github.com/aisys-group5/Dreammate-Generator/blob/main/KoDALLE/preprocess.ipynb)
3. train VQGAN with [train_vqgan.ipynb](https://github.com/aisys-group5/Dreammate-Generator/blob/main/train_vqgan.ipynb)
4. train KoDALLE with train_kodalle.ipynb
5. Manipulate generated images with [Style_Transform.ipynb](https://github.com/aisys-group5/Dreammate-Generator/blob/main/Style_Transform.ipynb)
