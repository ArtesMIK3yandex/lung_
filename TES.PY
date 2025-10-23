import os
import sys

print("Python:", sys.version)
print("Python path:", sys.executable)

try:
    import torch
    print("PyTorch успешно импортирован!")
    print("PyTorch версия:", torch.__version__)
    print("CUDA доступна:", torch.cuda.is_available())
except Exception as e:
    print("Ошибка импорта PyTorch:", e)
    
# Проверка DLL
dll_path = r"C:\Users\Artem\Desktop\lung_segmenter_project\venv\Lib\site-packages\torch\lib\c10.dll"
print(f"\nDLL существует: {os.path.exists(dll_path)}")