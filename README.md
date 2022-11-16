
## A Machine Learning Approach to Improve the Detection of CI Skip Commits

CSL7090 | SDE July 2022 | Term Project

**Paper:** 

R. Abdalkareem, S. Mujahid and E. Shihab, "A Machine Learning Approach to Improve the Detection of CI Skip Commits," in IEEE Transactions on Software Engineering, vol. 47, no. 12, pp. 2740-2754, 1 Dec. 2021, doi: 10.1109/TSE.2020.2967380.

Ref : https://ieeexplore.ieee.org/abstract/document/8961089

**Brief Description:**

In today's world going to market faster is extremly important and if we are not able to do so becuase of running longer and longer pipeline cycles for small & small changes in UI or some very minor bug fixes. The paper has tried to solve this problem by using Decision Tree algorithm of Machine Learning. Since this is extremly desired in today's world to make CI-CD pipleine more intelligent that they do not just follow a scheuld or they do not just follow a trigger of push & merge but they be more intelligent and to make them intelligent we have to use AI\ML but in this paper they have used Decision Tree but we think that if we use some other Model which are more efficient in processing human language then may be we can improve the solution proposed in this paper.



## Authors
- [Debonil Ghosh	[M21AIE225] ](https://www.github.com/debonil)
- [Ravi Shankar Kumar [M21AIE247]](https://www.github.com/debonil)



## Demo

https://youtu.be/5iA4ZghTVS0

https://youtu.be/MzQAmS6U23k


## Usage

    1. Data download from GitHub API & prepare feature vector with data-preparation.py

    2. Normalize feature vector, train ML models, and store results all-repo-ml-training.py



## Results

**Detailed Classifier Accuracy summary**
|Classifier         |Mean       |Median     |Max  |Min        |Standard Deviation|
|-------------------|-----------|-----------|-----|-----------|------------------|
|Ridge Classifier   |0.907612264|0.94075    |1    |0.64       |0.099287063       |
|RBF SVM            |0.906718868|0.942      |0.974|0.67       |0.089866116       |
|QDA                |0.906222013|0.943      |1    |0.67       |0.095284405       |
|Logistic Regression|0.904225472|0.94425    |1    |0.69       |0.08755999        |
|Gaussian Process   |0.902325472|0.93775    |1    |0.64       |0.09924061        |
|Random Forest      |0.895325472|0.93625    |1    |0.69       |0.089522373       |
|Naive Bayes        |0.893238679|0.93125    |1    |0.65       |0.098224384       |
|Neural Net         |0.886575157|0.936583333|0.973|0.67       |0.097637189       |
|Nearest Neighbors  |0.838960377|0.87       |0.975|0.556603774|0.136013828       |
|Linear SVM         |0.825698742|0.901833333|0.968|0.393      |0.170268225       |
|Decision Tree      |0.821083962|0.872      |0.975|0.568      |0.143949334       |
|AdaBoost           |0.784083962|0.872      |0.975|0.3        |0.210291759       |

**Detailed Classifier Accuracy for different repositories**

|Classifier         |dropwizard |eBay_parallec|GrammarViz2|jMotif_GI  |jMotif_SAX |ksclarke_solr-iso639-filter|mtsar|steve-community|atracee_contextlogger|zixpo_candybar|
|-------------------|-----------|-------------|-----------|-----------|-----------|---------------------------|-----|---------------|---------------------|--------------|
|Nearest Neighbors  |0.973      |0.973        |0.813      |0.875      |0.958      |0.774                      |0.67 |0.944          |0.957                |0.929         |
|Linear SVM         |0.975      |1            |0.884      |0.938      |0.952      |0.821                      |0.64 |0.951          |0.925                |0.938         |
|RBF SVM            |0.975      |1            |0.884      |0.875      |0.952      |0.821                      |0.69 |0.951          |0.957                |0.938         |
|Gaussian Process   |0.974      |0.973        |0.884      |0.969      |0.958      |0.830                      |0.67 |0.949          |0.935                |0.925         |
|Decision Tree      |0.968      |0.946        |0.393      |0.792      |0.958      |0.811                      |0.66 |0.912          |0.925                |0.892         |
|Random Forest      |0.972      |1            |0.821      |0.875      |0.958      |0.821                      |0.69 |0.944          |0.935                |0.938         |
|Neural Net         |0.975      |1            |0.884      |0.969      |0.952      |0.840                      |0.64 |0.944          |0.935                |0.938         |
|AdaBoost           |0.975      |0.946        |0.821      |0.865      |0.869      |0.557                      |0.61 |0.951          |0.871                |0.925         |
|Naive Bayes        |0.975      |0.568        |0.911      |0.875      |0.869      |0.594                      |0.3  |0.951          |0.86                 |0.938         |
|QDA                |0.975      |0.568        |0.911      |0.875      |0.869      |0.594                      |0.67 |0.951          |0.86                 |0.938         |
|Logistic Regression|0.975      |1            |0.875      |0.969      |0.952      |0.802                      |0.67 |0.951          |0.935                |0.933         |
|Ridge Classifier   |0.975      |1            |0.875      |0.865      |0.952      |0.802                      |0.65 |0.951          |0.925                |0.938         |

## Conclusion

Neural Net has best accuracy among all classifiers, but Random Forest Classifier has explainability of the model with comparable performance with Neural Net