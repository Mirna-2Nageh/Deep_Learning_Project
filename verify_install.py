import torch
import numpy as np
import pandas as pd
import matplotlib
import sklearn
import cv2
from PIL import Image

print("="*60)
print("MEDICAL AI ENVIRONMENT VERIFICATION")
print("="*60)
print(f"✓ PyTorch: {torch.__version__}")
print(f"✓ CUDA Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"✓ GPU: {torch.cuda.get_device_name(0)}")
print(f"✓ NumPy: {np.__version__}")
print(f"✓ Pandas: {pd.__version__}")
print(f"✓ Matplotlib: {matplotlib.__version__}")
print(f"✓ scikit-learn: {sklearn.__version__}")
print(f"✓ OpenCV: {cv2.__version__}")
print("="*60)
print("✅ All packages installed successfully!")
print("="*60)
