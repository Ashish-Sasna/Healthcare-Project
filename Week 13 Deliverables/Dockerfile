# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /Healthcare

# Copy the current directory contents into the container
COPY Scripts/ /Healthcare/Scripts/
COPY LR_model.pkl /Healthcare/
COPY lbl_enc.pkl /Healthcare/
COPY requirements.txt /Healthcare/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port 5000
EXPOSE 5000

# Entrypoint for executing the app
ENTRYPOINT ["python", "Scripts/app.py"]
