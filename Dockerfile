# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirments.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the Streamlit app when the container launches
CMD ["streamlit", "run", "web.py"]
