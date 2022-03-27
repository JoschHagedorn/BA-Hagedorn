# BA-Hagedorn
This Repository contains the code used in the Bachelor thesis from Josch Hagedorn. It builts on the DeepFilter Repository (https://github.com/fperdigon/DeepFilter). Additional information can be found in the pdf-file.
## Reproducibility
  
### Download this git repository and run local
The firts step is to clone this repository
 
~~~
git clone https://github.com/JoschUniHD/BA-Hagedorn
~~~

Then lets prepare the dataset.

If you are using Windows open Powershell using the cd command place yourself on  inside the repository folder, then 
execute the download_data.ps1 Powershell script using the command:

~~~
powershell -ExecutionPolicy Bypass -File '.\download_data.ps1'
~~~

If you are using a Unix-like system such as Linux, MacOS, FreeBSD, etc open a console in the path of DeepFilter code, 
then execute the download_data.sh bash file. 

~~~
bash ./download_data.sh
~~~

The next step is to create the Conda environment using the provided environment.yml file. For this step you need the 
conda python package manage installed. In case you don't have it installed we recommend installing 
[Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) to avoid installing unnecessary Python 
packages. 

To create the conda environment run the following command:
~~~
conda env create -f environment.yaml
~~~

Then activate the Python environment you just created with the following command:

~~~
conda activate DeepFilter
~~~

Finally start the training and the experiments by running the command:

~~~
python Experiment_?_?_main.py
~~~

This python script will train all the models and execute the experiments. There are 7 different experiments. After each one all resulting files should be movend into a new folder before the next experiment is executed. The evaluation of the results is done in the Jupyter Notebooks.

If you have a Nvidia CUDA capable device for GPU acceleration this code will automatically use it (faster). Otherwise the 
training will be done in CPU (slower).   
    
## License

The MIT License (MIT)

Copyright (c) 2021 Francisco Perdigon Romero, David Castro Piñol

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
