# Telegram Scraper

A Python script to scrape messages and images from Telegram channels using the Telethon library.

## Requirements

- Python 3.x
- Install the required dependencies:
  ```bash
  pip install telethon python-dotenv asyncio
  ```

## Setup

1. **Create a `.env` file** in the project directory with the following variables:
   ```
   TG_API_ID=your_api_id
   TG_API_HASH=your_api_hash
   phone=your_phone_number
   ```
   - You can obtain your `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org).

2. **Customize the script**:
   - Add the URLs of the Telegram channels to the respective lists in the script:
     ```python
     message_channels = ['https://t.me/DoctorsET', ...]
     image_channels = ['https://t.me/lobelia4cosmetics', ...]
     ```

## Features

- **Scrape Messages**: Fetch up to `message_limit` messages from specified Telegram channels and save them as JSON files.
- **Download Images**: Download images from specified Telegram channels and save them in an `images/` directory.

## Usage

1. Clone this repository and install dependencies:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   pip install -r requirements.txt
   ```

2. Add your API credentials to the `.env` file.

3. Modify the `message_channels` and `image_channels` lists in the script as needed.

4. Run the script:
   ```bash
   python your_script.py
   ```

## Output

- **Messages**: Saved as JSON files with the format:
  ```
  <channel_name>_messages.json
  ```
- **Images**: Downloaded in the `images/` directory.

## Customization

Feel free to modify the following parameters in the script:

- **Channel URLs**:
  ```python
  message_channels = ['https://t.me/DoctorsET', ...]
  image_channels = ['https://t.me/lobelia4cosmetics', ...]
  ```

- **Message Limit**: Adjust the number of messages to fetch by modifying the `message_limit` variable.

# Data Augmentation

A Python script for applying augmentations to images and bounding boxes using the `albumentations` library.

## Features

### Augmentation Pipeline
- Horizontal and vertical flips.
- Random brightness and contrast adjustments.
- Random scaling, shifting, and rotation.

### Bounding Box Support
- Handles bounding boxes in the YOLO format (`x_center`, `y_center`, `width`, `height`).

### Visualization
- Displays augmented images with bounding boxes.

## Requirements
- Python 3.x
- Install dependencies:
  ```bash
  pip install albumentations opencv-python matplotlib
  ```

## Usage

### 1. Create an Augmentation Pipeline
- Define your augmentation settings using:
  ```python
  transform = create_augmentation_pipeline()
  ```

### 2. Load Image and Labels
- Read an image and its bounding box labels (in YOLO format) using:
  ```python
  image, bboxes, class_labels = load_image_and_labels(image_path, label_path)
  ```

### 3. Apply Augmentations
- Apply the defined augmentations to the image and bounding boxes:
  ```python
  aug_image, aug_bboxes, aug_class_labels = apply_augmentations(image, bboxes, class_labels, transform)
  ```

### 4. Save Augmented Data
- Save the augmented image and updated labels using:
  ```python
  save_augmented_data(aug_image, aug_bboxes, aug_class_labels, image_save_path, label_save_path)
  ```

### 5. Visualize Bounding Boxes
- Display the augmented image along with its bounding boxes:
  ```python
  visualize_bboxes(aug_image, aug_bboxes)
  ```