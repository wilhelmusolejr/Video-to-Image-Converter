# Video to Image Converter

<p>This project is a Python-based tool that converts videos to images. For each video in the "video" folder, it extracts frames and saves them as images in a corresponding directory within the "image" folder.
</p>

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/video-to-image-converter.git
    ```
2. Navigate to the project directory:
    ```sh
    cd video-to-image-converter
    ```
3. Install the required dependencies:
    ```sh
    pip install opencv-python
    ```

## Usage

1. Ensure your videos are in the "video" folder.
2. Double-click the `Start me.bat` file or run it from the command line:
    ```sh
    Start me.bat
    ```
3. The extracted images will be saved in the "image" folder, organized by video file name.

## Example

```sh
video/
├── video1.mp4
├── video2.mp4

image/
├── video1/
│   ├── 0_42.jpg
│   ├── 1_42.jpg
│   └── ...
└── video2/
    ├── 0_56.jpg
    ├── 1_56.jpg
    └── ...
