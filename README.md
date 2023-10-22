# Iris-Data-PCA-Exploration
![dataset-cover](https://github.com/Prometheussx/Iris-Data-PCA-Exploration/assets/54312783/ca6dd4a3-493a-43bb-a383-9a6ca7e75d1c)

This project is a demo that applies PCA (Principal Component Analysis) analysis on the Iris dataset using Python and the Scikit-learn library. PCA is utilized to reduce high-dimensional data to lower dimensions.

# Using Iris Dataset and PCA

In this project, Principal Component Analysis (PCA) analysis was applied on Iris dataset using Python and Scikit-learn library. PCA is a technique used to reduce a multidimensional dataset to fewer dimensions and preserve the underlying variance of the data. The project consists of taking the data set, performing PCA analysis and visualizing the results with a graph.

## Project Content

- `iris_pca.py`: Python code implementing PCA analysis.
- `README.md`: This file containing information about the project.

## Requirements

The following requirements are needed for this code to work:

- Python 3.x
- Scikit-learn
- Pandas
- Matplotlib

You can use the following commands to install the necessary libraries:

```
pip install scikit-learn
pip install pandas
pip install matplotlib
```

## Data Set

This project was realized using the Iris dataset. Iris dataset is a dataset containing the characteristics of flower species. This dataset is predefined within the Scikit-learn library and therefore no external source is needed to pull the dataset.

## Project Phases

The project consists of the following steps:

1. Iris dataset is extracted.
2. PCA analysis is applied and the dataset is reduced from 4 dimensions to 2 dimensions.
3. The results are visualized on a graph.

## How to Use

You can follow the steps below to use the project:

1. Clone the project to your computer:

```
git clone https://github.com/Prometheussx/Iris-Data-PCA-Exploration.git
```

2. Go to the project folder:

```
cd Iris-Data-PCA-Exploration
```

3. Run the code:

```
python PCA.py
```

4. Examine the graph on the screen to see the results.
- Shows the variance explained by each component. The first component explains 92.46%, and the second     component explains 5.30% of the variance.
```python
print("Variance ratio:", pca.explained_variance_ratio_)  
```
  
- Indicates that 97.76% of the variance is preserved, implying a successful PCA with a 2.24% data loss.
```python
print("Sum:", sum(pca.explained_variance_ratio_))  
```
  


![image](https://github.com/Prometheussx/Iris-Data-PCA-Exploration/assets/54312783/cb6112ef-39be-420e-8ff7-b2b8b077284f)

![image](https://github.com/Prometheussx/Iris-Data-PCA-Exploration/assets/54312783/3103cfd9-16e8-4224-bbdc-d8ec21cf2894)

## Contact Information

For any questions, feedback or requests to contribute to the project, you can contact the contact information below:

- LinkedIn: [https://www.linkedin.com/in/erdem-taha-sokullu/]
- Email: [erdemtahasokullu@gmail.com]
- Kaggle: [https://www.kaggle.com/erdemtaha]
## Problems and Requests

You can report any issues or request new features using the [Issues](https://github.com/Prometheussx/Iris-Data-PCA-Exploration/issues) section of the project on GitHub. Try to be as detailed as possible when describing issues and requests.

## Contributing

For any bug reports or requests to contribute to the project, please contact GitHub.

## License

This project is licensed under the MIT license. For more information, see [LICENSE](LICENSE).
