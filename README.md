# Generate Audio Image Descriptions with LlaVa 7B and speecht5_tts (using Ollama)

This repository contains the code for the extraction of image descriptions using LLava:7B with Ollama (4-bit-Quantized Version)
The generated description is then transformed into audio using the Microsoft speecht5_tts model

We use the ```Matthijs/cmu-arctic-xvectors```  embeddings dataset.



## Requirements 

You need to install **Ollama** locally on your machine to run this code. [Link to install ollama](https://ollama.com/)


Once installed you need to import the Llava:7b model. You can do so using the following command:
```
ollama pull llava:7b
```

**You can install these requirements for this project via:**
```
!pip install -r requirements.txt
```


## Usage

The code provided in this repo is straightforward, clone the repo using the following:
```
git clone https://github.com/rayaneghilene/text-to-audio.git
```

Use the following command to run the code:

```
python main.py
```



## References

**Speecht5_tts model:**

```
  @inproceedings{ao-etal-2022-speecht5,
    title = {{S}peech{T}5: Unified-Modal Encoder-Decoder Pre-Training for Spoken Language Processing},
    author = {Ao, Junyi and Wang, Rui and Zhou, Long and Wang, Chengyi and Ren, Shuo and Wu, Yu and Liu, Shujie and Ko, Tom and Li, Qing and Zhang, Yu and Wei, Zhihua and Qian, Yao and Li, Jinyu and Wei, Furu},
    booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
    month = {May},
    year = {2022},
    pages={5723--5738},
}

```

**Llava model:**
```
@misc{liu2023visual,
      title={Visual Instruction Tuning}, 
      author={Haotian Liu and Chunyuan Li and Qingyang Wu and Yong Jae Lee},
      year={2023},
      eprint={2304.08485},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

**Dataset:**
```
@article{article,
author = {Kominek, John and Black, Alan},
year = {2004},
month = {01},
pages = {},
title = {The CMU Arctic speech databases},
journal = {SSW5-2004}
}
```
## Contact
Contact me if you have any questions at rayane.ghilene@ensea.fr
