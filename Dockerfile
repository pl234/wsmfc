# FROM python:3.9-slim
# WORKDIR /app
# COPY . /app
# RUN pip install --no-cache-dir -r requirements.txt
# EXPOSE 8000
# CMD ["python", "withoutStoring_CallingAll.py"]








# FROM python:3.9

# RUN apt-get update \
#     && apt-get install -y python3-tk \
#     && rm -rf /var/lib/apt/lists/*

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD ["python", "withoutStoring_CallingAll.py"]










FROM python:3.9

# Install system dependencies
RUN apt-get update \
    && apt-get install -y xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install tkinter wrapper for Xvfb
RUN pip install python3-xlib pyvirtualdisplay

# Copy the current directory contents into the container at /app
COPY . .

# Run your application with Xvfb
CMD ["Xvfb", ":99", "-screen", "0", "800x600x16", "-ac"] && \
    ["export", "DISPLAY=:99.0"] && \
    ["python", "withoutStoring_CallingAll.py"]

