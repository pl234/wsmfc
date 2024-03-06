# # # FROM python:3.9-slim
# # # WORKDIR /app
# # # COPY . /app
# # # RUN pip install --no-cache-dir -r requirements.txt
# # # EXPOSE 8000
# # # CMD ["python", "withoutStoring_CallingAll.py"]








# # # FROM python:3.9

# # # RUN apt-get update \
# # #     && apt-get install -y python3-tk \
# # #     && rm -rf /var/lib/apt/lists/*

# # # WORKDIR /app

# # # COPY requirements.txt .

# # # RUN pip install --no-cache-dir -r requirements.txt

# # # COPY . .

# # # CMD ["python", "withoutStoring_CallingAll.py"]










# # # FROM python:3.9

# # # # Install system dependencies
# # # RUN apt-get update \
# # #     && apt-get install -y xvfb \
# # #     && rm -rf /var/lib/apt/lists/*

# # # # Set the working directory in the container
# # # WORKDIR /app

# # # # Copy the requirements file into the container at /app
# # # COPY requirements.txt .

# # # # Install any needed dependencies specified in requirements.txt
# # # RUN pip install --no-cache-dir -r requirements.txt

# # # # Install tkinter wrapper for Xvfb
# # # RUN pip install python3-xlib pyvirtualdisplay

# # # # Copy the current directory contents into the container at /app
# # # COPY . .

# # # # Run your application with Xvfb
# # # CMD ["Xvfb", ":99", "-screen", "0", "800x600x16", "-ac"] && \
# # #     ["export", "DISPLAY=:99.0"] && \
# # #     ["python", "withoutStoring_CallingAll.py"]





# # # Use the official Python image as a base image
# # FROM python:3.9-slim

# # # Set the working directory in the container
# # WORKDIR /app

# # # Copy the current directory contents into the container at /app
# # COPY . /app

# # # Install dependencies
# # RUN apt-get update && apt-get install -y \
# #     python3-tk \
# #     && rm -rf /var/lib/apt/lists/*

# # RUN pip install --no-cache-dir -r requirements.txt

# # # Set environment variables
# # ENV FLASK_APP=withoutStoring_CallingAll.py

# # # Expose the Flask port
# # EXPOSE 8000

# # # Run the Flask application
# # CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]





# FROM python:3.9-slim

# # Install required dependencies
# RUN apt-get update && apt-get install -y \
#     xvfb \
#     x11-utils \
#     && rm -rf /var/lib/apt/lists/*

# # Set up a virtual display
# ENV DISPLAY=:99

# # Copy your application files into the container
# COPY . /app
# WORKDIR /app

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Start Xvfb and run your application
# CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x24 & python withoutStoring_CallingAll.py"]







FROM python:3.9-slim

# Install required dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Copy your application files into the container
COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your application
CMD ["python", "withoutStoring_CallingAll.py"]
