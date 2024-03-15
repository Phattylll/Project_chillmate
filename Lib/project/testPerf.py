# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
# from sklearn.preprocessing import LabelEncoder
# from keras.models import load_model
# from keras.preprocessing.image import ImageDataGenerator
# import seaborn as sns
# import matplotlib.pyplot as plt

# def plot_confusion_matrix(conf_matrix, class_labels):
#     plt.figure(figsize=(10, 8))
#     sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
#     plt.xlabel('Predicted Labels')
#     plt.ylabel('True Labels')
#     plt.title('Confusion Matrix')
#     plt.show()

# # Paths
# train_data_path = r'D:\3.1\4.1\ImgPro\test\class'
# model_path = r'D:\3.1\4.1\ImgPro\Lib\project\pkg\model\food_class'
# # Load the model
# model = load_model(model_path)

# # Load training data
# train_datagen = ImageDataGenerator(rescale=1./255)
# train_generator = train_datagen.flow_from_directory(
#     train_data_path,
#     target_size=(224, 224),
#     batch_size=32,
#     class_mode='categorical',
#     shuffle=False
# )

# # Get true labels for training data
# true_labels_train = train_generator.classes

# # Make predictions on training data
# predictions_train = model.predict(train_generator)
# encoder = LabelEncoder()  # Define encoder here
# predicted_labels_train = encoder.fit_transform(predictions_train.argmax(axis=1))

# # Calculate metrics for training data
# accuracy_train = accuracy_score(true_labels_train, predicted_labels_train)
# precision_train = precision_score(true_labels_train, predicted_labels_train, average='weighted')
# recall_train = recall_score(true_labels_train, predicted_labels_train, average='weighted')
# f1_train = f1_score(true_labels_train, predicted_labels_train, average='weighted')

# # Print metrics for training data
# print(f'Training Data Metrics:')
# print(f'Accuracy: {accuracy_train}')
# print(f'Precision: {precision_train}')
# print(f'Recall: {recall_train}')
# print(f'F1-Score: {f1_train}')

# # Calculate confusion matrix for training data
# conf_matrix_train = confusion_matrix(true_labels_train, predicted_labels_train)

# # Plot confusion matrix for training data with details
# class_names = list(train_generator.class_indices.keys())
# disp = ConfusionMatrixDisplay(conf_matrix_train, display_labels=class_names)
# disp.plot(cmap='Blues', values_format='d')
# plt.title('Confusion Matrix (Training Data)')
# plt.show()






from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import seaborn as sns
import matplotlib.pyplot as plt

def plot_confusion_matrix(conf_matrix, class_labels):
    plt.figure(figsize=(10, 8))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.title('Confusion Matrix')
    plt.show()

# Paths
train_data_path = r'D:\3.1\4.1\ImgPro\test\fruit'  # Update with your actual path
model_path = r'D:\3.1\4.1\ImgPro\Lib\project\pkg\model\groupFruit_class_epoch_200.h5'  # Update with your actual path

# Load the model
model = load_model(model_path)

# Load training data
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
    train_data_path,
    target_size=(244, 244),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)

# Get true labels for training data
true_labels_train = train_generator.classes

# Make predictions on training data
predictions_train = model.predict(train_generator)
encoder = LabelEncoder()
predicted_labels_train = encoder.fit_transform(predictions_train.argmax(axis=1))

# Calculate metrics for training data
accuracy_train = accuracy_score(true_labels_train, predicted_labels_train)
precision_train = precision_score(true_labels_train, predicted_labels_train, average='weighted')
recall_train = recall_score(true_labels_train, predicted_labels_train, average='weighted')
f1_train = f1_score(true_labels_train, predicted_labels_train, average='weighted')

# Print metrics for training data
print(f'Training Data Metrics:')
print(f'Accuracy: {accuracy_train}')
print(f'Precision: {precision_train}')
print(f'Recall: {recall_train}')
print(f'F1-Score: {f1_train}')

# Calculate confusion matrix for training data
conf_matrix_train = confusion_matrix(true_labels_train, predicted_labels_train)

# Plot confusion matrix for training data with details
class_names = list(train_generator.class_indices.keys())
plot_confusion_matrix(conf_matrix_train, class_names)

