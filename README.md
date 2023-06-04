# Rocchio's Method for Document Classification
Document Classification Using Rocchio Method with continuous integration(workflow)

### What is Rocchio's Method?
Rocchio's method is a classic algorithm used for document classification. It is a centroid-based approach that assigns a document to a specific class by comparing its similarity to the centroids of different classes. The algorithm is based on the assumption that documents in the same class share similar feature vectors.


**Rocchio's Method**
$$\left (Q_1 \right) \= \left (Q_0 \right) + \left(beta \sum_{i=1}^n (R_i)/(n_1) \right) -  \left(gamma \sum_{i=1}^n (S_i)/(n_2) \right)$$

### How Rocchio's Method Works
Rocchio's method utilizes a training dataset containing labeled documents to create class prototypes. Each class prototype is represented as a centroid vector in the vector space. During the classification process, unlabeled documents are compared to these class prototypes to determine their most likely class.

The algorithm employs the concept of relevance feedback, where users provide feedback on the correctness of the classification results. By iteratively updating the class prototypes based on user feedback, Rocchio's method improves the accuracy of the classification over time.

### Continuous Integration
This implementation of Rocchio's method is integrated with Continuous Integration (CI), leveraging the power of automated testing and deployment. With CI, every change to the codebase triggers a series of tests that ensure the functionality of the algorithm remains intact.

By using a CI system such as Jenkins or Travis CI, you can set up automatic testing and deployment pipelines for this document classification project. These pipelines can include steps such as code linting, unit tests, integration tests, and even deployment to a production environment. CI ensures that any changes or updates made to the codebase are thoroughly tested and meet the required quality standards.
