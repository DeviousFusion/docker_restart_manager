import docker
import logging
from datetime import datetime
from time import sleep

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Docker client
client = docker.from_env()

def restart_containers():
    """Restart containers based on the schedule specified in their labels."""
    try:
        containers = client.containers.list()
    except docker.errors.APIError as e:
        logging.error(f"Error fetching containers: {e}")
        return

    current_time = datetime.now().strftime('%H:%M')
    
    for container in containers:
        try:
            restart_schedule = container.labels.get('drm.restart.schedule', '')
            if not restart_schedule:
                continue

            restart_times = restart_schedule.split(',')

            if current_time in restart_times:
                logging.info(f"Restarting container: {container.name}")
                container.restart()
        except docker.errors.APIError as e:
            logging.error(f"Error handling container {container.name}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error with container {container.name}: {e}")

def main():
    """Main loop to periodically check and restart containers."""
    while True:
        try:
            restart_containers()
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
        
        # Wait for 60 seconds before checking again
        sleep(60)

if __name__ == "__main__":
    main()