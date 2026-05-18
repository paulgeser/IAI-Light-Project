# Reflection

## 1. Which approach won, and when is classical still worth it?

The results show that the classical baseline (TF-IDF + Logistic Regression) outperformed the pretrained zero-shot Transformer model (DistilBERT) by far, with scores of 0.97 vs 0.55 accuracy. 
After some quick research into the SST-2 training dataset used for DistilBERT training, the reason for the lower performance became clear.
I found out under this link: https://www.kaggle.com/datasets/atulanandjha/stanford-sentiment-treebank-v2-sst2 that the model was trained on movie reviews, which are definitely not the same domain as SMS spam messages. 
It is most likely that the model doesn't really know what to do in data domain it was not specifically trained on. On the opposite the classical model learns the patterns directly from the training data. 
It has learned the domain much better than the transformer did. Since this problem statement is rather easy for a classical model to learn, as there are likely clear word patterns indicating spam emails, it is much more efficient to use a classical model than a transformer. 
In general if the training data is available, the task is well defined and speed matters, classical models are often more performant over large pretrained models. 
Large pretrained models are better suited to scenarios with limited training data or complex tasks.
Additionally if you consider the cost difference between the classical and pretrained models, you will see that the classical model is more cost-effective. The classical model does not require a large amount of data to be downloaded and can be trained in seconds using only CPU resources. 
In contrast, the pretrained model has to download large data files and is not optimised for running on a CPU, therefore it generally takes longer to run.
Finally in this scenario involving SMS spam messages, I would choose a classical model over a large pretrained model because it's faster and more accurate (for this specific task).

## 2. What's in the Docker image that isn't in a venv?

Venv runs on top of the operating system and only captures the Python libraries, so it's not guaranteed that the same Venv libraries will work on Mac and Windows because the underlying operating systems are very different.
For example file paths are different on Mac and Windows and other issues such as case sensitivity could also cause problems. The Python interpreter version could also be different, which could cause issues as well.
Docker is designed for exactly this scenario. It covers the full operating system and therefore offers much better reproduction results. 
When running the project in a Docker container on both computers, you will get the same results since both times the exact same OS, system libraries, Python interpreter and model weights are used.


## 3. One thing that broke, one thing that surprised me

Initially I had some issues with my requirements.txt file. When I used the command 'pip freeze > requirements.txt', it worked, but then my IDE always showed errors for the file. 
After some time I noticed that the file's encoding had changed from UTF-8 to UTF-16 after using the command. I changed it back manually and then had no further problems.

I was quite surprised by the performance differences between the two models. I never expected the large pretrained model to perform so badly on this simple task. 
I also found it interesting to discover that the pretrained model was trained on movie reviews, which is probably the root of the issue. From this I conclude that when training models myself in the future, it is not just the algorithm that can solve and work with any data, the data itself is really the foundation and has to be suitable, otherwise it won't work well.