# Install pip
# apt install python3-pip

# install env 
# sudo apt install python3-venv

# create env
# python3 -m venv myenv

# install docker fo renv
# pip install docker

# deactivate  --> to exit env

# source myenv/bin/activate --> to enter


python file docker_script.py

import docker
import sys

def pull_image(image_name):
    """
    Pulls a Docker image from the Docker Hub registry.

    Args:
        image_name (str): The name of the Docker image to pull.

    Returns:
        docker.models.images.Image: The pulled Docker image object.
    """
    try:
        # Initialize the Docker client
        client = docker.from_env()

        # Pull the Docker image
        print(f"Pulling image: {image_name}")
        image = client.images.pull(image_name)
        print(f"Image pulled successfully: {image.id}")

        return image

    except docker.errors.APIError as e:
        print(f"An error occurred while pulling the image: {e}")
        sys.exit(1)

    except docker.errors.DockerException as e:
        print(f"A Docker-related error occurred: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python docker_script.py [image_name[:tag]]")
        sys.exit(1)

    image_name = sys.argv[1]
	
# command to download docker image
# python docker_script.py <image-name>:<tag>
