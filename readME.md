Step 1: Fill in the config.ini file with the necessary values for target_hosts and target_ports.

Step 2: Build the Docker image using the provided Dockerfile:


`docker build -t my_python_app .`

Replace my_python_app with the desired name for your Docker image.

Step 3: Run the Docker container and start interactive (-i) terminal (-t) session:

`docker run -ti my_python_app`

Replace my_python_app with the name of the Docker image you built in Step 2.

Follow appearing guide to properly run the script (ports needs followed format - start_port-end_port e.g. 22-443)
