# ESCAPE data science summer school 2021: Apache Spark

Welcome to the Apache Spark lecture! Please, read carefuly this page before starting the lecture as it contains important information to set up the materials. 

### Goals of the lecture

*  Learning the basics of cluster computing, and the big data challenges in modern science.
- Learning how to integrate scientific tools into Apache Spark, and how to perform efficient analysis on large volumes of data.

### Timetable

- **Session 1:** 
  - I will review the landscape of cluster computing by addressing some of the most pressing questions today: what is cluster computing? What does it mean working in a distributed environment? What are the data and computing challenges that the scientific community is facing nowadays, and how can we tackle those? Some useful concepts like functional programming and implicit parallelisation will be discussed. I will also introduce Apache Spark, a cluster computing framework for analysing large datasets that proved successful in the industry. I will specifically focus on the Apache Spark SQL module and DataFrames API, and we will start practicing through a series of simple exercises.
- **Session 2:** 
  - In this session, we will use the Apache Spark Python API (PySpark) and learn on concrete examples how to interface and play with popular scientific libraries (Numpy, Pandas, ...). We will also see how to test and debug a code written with Spark, and integrate it in a Continuous Integration pipeline.
- **Session 3:** 
  - For the last session, we will finish with concrete applications in the domain of astronomy: catalog & image manipulation, machine learning and streaming data (if time permits).

### Pre-requisites:

- Latest version of Docker installed. In case you do not have it, all the exercises will be also accessible from Google Colab - but you will need a Google account.
- A good knowledge in Python
- Some general knowledge on parallel computing, and its challenges
- Some knowledge in functional programming can help.


### How to play the notebooks?

As Spark needs a specific environment, the best way is to use Docker. We provide a Dockerfile in the repo and a script to launch pyspark with jupyter:

```bash
$ ./launch_notebooks.sh
...
Removing intermediate container e3782eaa192c
 ---> 367a84556afd
Successfully built 367a84556afd
Successfully tagged spark_stfc:latest
[I 05:30:38.614 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
[I 05:30:39.375 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/site-packages/jupyterlab
[I 05:30:39.375 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
[I 05:30:39.381 NotebookApp] Serving notebooks from local directory: /home/jovyan/work
[I 05:30:39.381 NotebookApp] The Jupyter Notebook is running at:
[I 05:30:39.382 NotebookApp] http://(b14861473286 or 127.0.0.1):8888/?token=aba4b32c134e9fbca8ce99954c9ea2554dc68b7d9990a70c
# --> Just follow the url generated using one of the two options.
```

Copy the generated URL in your browser tab, and walk to the notebook folder. Then open a notebook to play it. Note that you can either directly run the notebook as is, or play it as slides using the RISE button (use SPACE to move between slides):

<img src="pictures/rise_button.png" alt="alt text"/>

### How to enter the container?

To enter the container and fully enjoy all Spark features, you would just use the runner:

```bash
./launch_container.sh
[+] Building 22.1s (12/12) FINISHED
 => [internal] load build definition from Dockerfile                                                                         0.0s
 => => transferring dockerfile: 37B
...
(base) jovyan@77081e01d859:~/work$

```

From here, you can launch any regular Spark job. For example, try:

```bash
cd src/
spark-submit --master local[*] count_points.py
```

### Alternative to Docker for notebooks: Google Colab

If you do not have Docker, or you do not want to use it, you can also play the notebooks directly in Colab:

- Session1: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()
- Session2: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()
- Session3: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()

Note you will need a Google account.