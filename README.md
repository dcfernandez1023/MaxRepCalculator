# Final Project

<b>Course</b>: CS 486 - Deploying Working Software, University of San Francisco

<b>Author</b>: Dominic Fernandez

<b>Date</b>: May 12, 2021

## Description
This project is a very simple web application that calculates the one rep max of a weight-lifting
exercise based on the Brzycki formula (https://en.wikipedia.org/wiki/One-repetition_maximum).  

Though the application itself is simple, the main purpose of this project is to implement 
a Continuous Deployment Pipeline with test automation, `Docker`, and `Github Actions`.

Dev: http://dev-dcfernandez-1693893477.us-west-2.elb.amazonaws.com/
Prod: http://prod-dcfernandez-2002147699.us-west-2.elb.amazonaws.com/


## Usage 
### Installation
To run this project locally, you first need to install Docker (https://docs.docker.com/get-docker/).
If you are using Windows, install WSL2 onto your computer and download Docker for the Linux 
distribution you chose (https://docs.microsoft.com/en-us/windows/wsl/install-win10).

After installing Docker, you can fork this Github repository and pull the code down locally.

### Running the Application 
To run the application locally, navigate to the root directory of the project and run `docker build -t one-rep-max-calculator .` to build the Docker image.
Then, run `docker run -p <desired-port>:<desired-port> one-rep-max-calculator` or `docker run -p <desired-port>:<desired-port> -d one-rep-max-calculator`
to run as a daemon.  The Docker container should now be accessible at `http://localhost:<desired-port>`.

To stop the Docker container, use command `docker ps` to see details about the containers you have currently running.  Find the container ID or name 
of the container you just created and run `docker stop <container ID/name>`.  (Note: if you did not run the Docker container as a daemon, you will 
have to first CTL+C to kill the process running the Docker container).

See https://docs.docker.com/reference/ for additional Docker commands.
