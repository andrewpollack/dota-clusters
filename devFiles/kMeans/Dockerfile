# Python 3.6.7
FROM continuumio/miniconda3

# author of file
LABEL maintainer="Andrew Pollack <andrewpkq@gmail.com>"

# Packages that we need 
WORKDIR /app

# instruction to be run during image build
RUN conda install jupyter -y && \
    conda install pandas -y && \
    conda clean -y -all

# Make port 8888 available to the world outside this container
EXPOSE 8888

# Create mountpoint
VOLUME /app

# Run jupyter when container launches
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
