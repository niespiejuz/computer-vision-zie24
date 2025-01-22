import matplotlib.pyplot as plt
from ultralytics import YOLO

def train_yolo():
    model = YOLO("yolov8n.pt")

    model.train(
        data="./datasets.archive/data.yaml",
        epochs=10,
        imgsz=640,
        batch=8,
    )

def detect_yolo(image_path):
    model = YOLO("./runs/detect/train/weights/best.pt")

    results = model(image_path, conf=0.4)
    result_image = results[0].plot()

    plt.figure(figsize=(10, 10))
    plt.imshow(result_image)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    train_yolo()

    detect_yolo("./datasets/archive/test/images/photo_2023-03-07-12-31-27_jpeg.rf.f0e8a63e3376386e3163dd79d7499054.jpg")
