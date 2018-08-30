PY = python3

HELLO_WORLD_DIR = opencv-helloworld
HELLO_WORLD_FILE = opencv-helloworld.py

IMG_PROCESSING_DIR = opencv-img-processing
IMG_PROCESSING_FILE = opencv-img-processing.py

all: img-processing

.PHONY: all

hello-world: $(HELLO_WORLD_DIR)/$(HELLO_WORLD_FILE)
	cd $(HELLO_WORLD_DIR) &&\
	$(PY) $(HELLO_WORLD_FILE) &&\
	cd ..

img-processing: $(IMG_PROCESSING_DIR)/$(IMG_PROCESSING_FILE)
	cd $(IMG_PROCESSING_DIR) &&\
	$(PY) $(IMG_PROCESSING_FILE) &&\
	cd ..
