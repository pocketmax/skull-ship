# deep learning notes

Using data models
https://tfhub.dev/google/experts/bert/wiki_books/qqp/2
Convert a DM to a different format
Detect a DM format
Extract meta data from DM
Mount a DM on node
Mount a DM on html5
Mount a DM on py
arch
* CenterNet
* EfficientDet
* Faster R-CNN
* Mask R-CNN
* RetinaNet
* SSD


coefficient
* polynomial
    * indeterminate

Really basic tutorial vids on what deep learning is
https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi
terms
* Gradient descent: minimizes error
* Neural network goal: is to split data in the most accurate way possible
* Error function: determines how far you are off from the correct value
* Continuous function: ??? @ 9:00
* Discrete function: ??? @ 9:38
* Logistic regression: @ 10:19
* Activation function: @ 15:14
* Sigmoid: a type of activation function
* Product of the probability: @ 18:40
* Maximum likelihood: @ 19:40
* Log function: @ 20:20
* Continues Error function: 
* Stochastic gradient descent
* Cost surface
* Back propagation
* Sigmoid function

Basic intro to deep learning and neural networks
https://www.youtube.com/watch?v=BR9h47Jtqyw

Tensor flow playlist tutorial
https://www.youtube.com/playlist?list=PLRqwX-V7Uu6YIeVA3dNxbR9PYj4wV31oQ

curl http://download.tensorflow.org/example_images/flower_photos.tgz \
    | tar xz

git clone https://github.com/googlecodelabs/tensorflow-for-poets-2

python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=tf_files/flower_photos/daisy/21652746_cc379e0eea_m.jpg
Returns…
Daisy  0.99508375
Dandelion  0.0028086917
sunflowers 0.002093148
Roses  1.37025945e-05
Tulips  6.3252025e-07

python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=tf_files/flower_photos

1s-phoenix-1281
chapter = GDG cloud phoenix
QUESTIONS
1. what is machine learning?
2. what math subjects does machine learning use? statistics, R lang
    1. math is for data modeling which autoML can do automaticly
3. what is a good source for machine learning to learn with? kaggle.com, coursera, linux academy
4. any difference between training tenserflow model locally or in cloud besides performance?
5. what use cases do tensor cores take advantage of?
6. what are some of the common mistakes people make when trying to learn ML?
7. difference between ML and deep learning?
    1. ML = broad category of automated processing
    2. DL = tries different things to decide if the answer is correct
8. using 2 inputs with data model instead of 1?
    1. put historical transactions into autoML
    2. nfold data

AI and ML sept 29th and UAT
https://www.eventbrite.com/e/aiml-devfest-uat-tickets-55035261950

kaggle.com

TERMS
* Transfer learning: when you build a new model to classify your original dataset, you reuse the feature extraction part and re-train the classification part with your dataset
* training
* Training accuracy: shows the percentage of the images used in the current training batch that were labeled with the correct class
* Validation accuracy: the precision (percentage of correctly-labelled images) on a randomly-selected group of images from a different set.
* Cross entropy: a loss function that gives a glimpse into how well the learning process is progressing (lower numbers are better here).
* loss function
* Cross entropy
* Convolutional neural network
* Softmax layers
* Fully-connected layers
* training step
* Learning rate: controls magnitude of the updates to the final layer during training. Higher value trains faster but less accurate
* evaluation step
* data model
* perimeter tuning
* job
* Bottleneck:an informal term often used for the layer just before the final output layer that actually does the classification
* prediction request
* batch prediction
* Stochastic gradient descent
* Cost surface
* Back propagation
* wide and deep model
* data gathering
* regression problems
* google datalab
* classification problems
* multi class classification problems
* target column
* bias
* noise: data set columns that autoML couldn’t find patterns on
* signal: data set columns that autoML found patterns on
* features: columns in dataset used to train data model
* targeted output field: what we want to predict after the model is trained
* weight
* neural networks
    * convolutions
    * pooling
    * epochs
* jupyter: python tool
* observed class
* predicted class
* Feature importance: AutoML Tables tells you what features it found to be most important for building this model in the Feature importance graph. Feature importance is computed by measuring the impact that each feature has on the prediction, when perturbed across a wide spectrum of values sampled from the dataset. You should review this information to ensure that all of the most important features make sense for your data.

* classification model terms
    * Confusion matrix: The confusion matrix helps you understand where misclassifications occur (which classes get "confused" with each other). Each row is a predicted class and each column is an observed class. The cells of the table indicate how often each classification prediction coincides with each observed class. Confusion matrices are provided only for classification models with 10 or fewer values for the target column.
    * AUC: area under curve. the closer to 1 the more accurate the data model is.
    * AUC PR: The area under the precision-recall (PR) curve. This value ranges from zero to one, where a higher value indicates a higher-quality model.
    * AUC ROC: The area under the receiver operating characteristic (ROC) curve. This ranges from zero to one, where a higher value indicates a higher-quality model.
    * Accuracy: The fraction of classification predictions produced by the model that were correct.
    * Log loss: The cross-entropy between the model predictions and the target values. This ranges from zero to infinity, where a lower value indicates a higher-quality model.
    * F1 score: The harmonic mean of precision and recall. F1 is a useful metric if you're looking for a balance between precision and recall and there's an uneven class distribution.
    * Precision: The fraction of classification predictions produced by the model that were correct.
    * Recall: The fraction of rows with this label that the model correctly predicted. Also called "True positive rate".
    * False positive rate: The fraction of rows predicted by the model to be the target label but aren't (false positive).
* regression model terms
    * MAE: The mean absolute error (MAE) is the average absolute difference between the target values and the predicted values. This metric ranges from zero to infinity; a lower value indicates a higher quality model.
    * RMSE: The root-mean-square error metric is a frequently used measure of the differences between the values predicted by a model or an estimator and the values observed. This metric ranges from zero to infinity; a lower value indicates a higher quality model.
    * RMSLE: The root-mean-squared logarithmic error metric is similar to RMSE, except that it uses the natural logarithm of the predicted and actual values plus 1. RMSLE penalizes under-prediction more heavily than over-prediction. It can also be a good metric when you don't want to penalize differences for large prediction values more heavily than for small prediction values. This metric ranges from zero to infinity; a lower value indicates a higher quality model. The RMSLE evaluation metric is returned only if all label and predicted values are non-negative.
    * R^2: R squared (R^2), also known as the coefficient of determination, is the square of the Pearson correlation coefficient between the labels and predicted values. This metric ranges between zero and one; a higher value indicates a higher quality model.
    * MAPE: Mean absolute percentage error (MAPE) is the average absolute percentage difference between the labels and the predicted values. This metric ranges between zero and infinity; a lower value indicates a higher quality model.
    * Feature importance: AutoML Tables tells you what features it found to be most important for building this model in the Feature importance graph. Feature importance is computed by measuring the impact that each feature has on the prediction, when perturbed across a wide spectrum of values sampled from the dataset. You should review this information to ensure that all of the most important features make sense for your data.

USE CASES
* tag people in photos
* classifying data, pictures or videos
* “ok google” “hey alexa” voice commands
examples of machine learning
* using data to answer questions


dataprep - service used for data cleaning
data flow - pub/sub queue that populates a BigQuery table˘
dialog flow - conversation building tool
* agents: NLU (natural language understanding) module
* intents: defined components of agents that process a users request
    * sections
        * user says
        * action
        * response
        * context
entities - tools used for extracting parameters from natural language inputs
* types
    * System: defined by dialog flow
        * types
            * system mapping: reference values
            * system enum: no reference values
            * system composite: other entities with aliases and returns object type values
    * Developer: defined by developer
    * User: built for each end user in very request
contexts - context of a users request
fulfillment - web hook for passing info to external system 




tensorboard - research tool for finished data models BEFORE they are deployed
data gathering
model building
training
evaluation
perimeter turning
“Wrangle language”
data -> data cleaning > training -> model -> review model -> deploy model

requirements
1. mid tinder: match a pending transaction to a mid with the highest forecasted success rate
2. predict future chargeback: figure out how many days in the future a pending transaction will charge back

https://www.youtube.com/watch?v=HcqpanDadyQ
https://youtu.be/m0rqccviLNM
https://www.youtube.com/watch?v=ZhQK0glTLg0&feature=youtu.be

the main entities involved with ML
* jobs
* models
* model versions
* model service
* trained models
* batch prediction
* prediction request

the actions involved in ML
* training

tensor board analytics and reporting tool for trained data

things to know
a hello world example of machine learning

git clone https://github.com/GoogleCloudPlatform/cloudml-samples.git

training jobs in single instance vs distributed mode

gcloud ai-platform jobs submit training $JOB_NAME \
    --job-dir $OUTPUT_PATH \
    --runtime-version 1.10 \
    --module-name trainer.task \
    --package-path trainer/ \
    --region $REGION \
    -- \
    --train-files $TRAIN_DATA \
    --eval-files $EVAL_DATA \
    --train-steps 1000 \
    --eval-steps 100 \
    --verbosity DEBUG


gcloud ai-platform local train \
    --module-name trainer.task \
    --package-path trainer/ \
    --job-dir $MODEL_DIR \
    -- \
    --train-files $TRAIN_DATA \
    --eval-files $EVAL_DATA \
    --train-steps 1000 \
    --eval-steps 100

PROJECT_ID=$(gcloud config list project --format "value(core.project)")
BUCKET_NAME=${PROJECT_ID}-mlengine
echo $BUCKET_NAME
REGION=us-central1

gsutil mb -l $REGION gs://$BUCKET_NAME


gcloud ai-platform models create $MODEL_NAME --regions=$REGION

gsutil ls -r $OUTPUT_PATH/export
gsutil cp -r data gs://$BUCKET_NAME/data
gcloud ai-platform jobs submit training $JOB_NAME \
    --job-dir $OUTPUT_PATH \
    --runtime-version 1.10 \
    --module-name trainer.task \
    --package-path trainer/ \
    --region $REGION \
    -- \
    --train-files $TRAIN_DATA \
    --eval-files $EVAL_DATA \
    --train-steps 1000 \
    --eval-steps 100 \
    --verbosity DEBUG

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$QWIKLABS_USERNAME" \
    --role="roles/automl.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:custom-vision@appspot.gserviceaccount.com" \
    --role="roles/ml.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:custom-vision@appspot.gserviceaccount.com" \
    --role="roles/storage.admin"

gcloud ai-platform predict \
 --model $MODEL_NAME \
 --version v1 \
 --json-instances ../test.json

gcloud config set core/project PROJECT_ID
gcloud config set compute/zone us-central1-f

datalab create my-datalab --machine-type n1-standard-4

!git clone https://github.com/vijaykyr/tensorflow_teaching_examples.git housing_prices