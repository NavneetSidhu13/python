# Convert "nginx,mysql,redis" to a list.

services = "nginx,mysql,redis"
services_list = services.split(',')
print(services_list)

# From this dictionary, print all web servers.

servers = {
    "web": ["web1.example.com", "web2.example.com"],
    "db": ["db1.example.com"],
    "cache": ["redis1.example.com"]
}

for server in servers.get("web",[]):
    print(server)
    
# Validate if a port is an integer before using it.
port = "8080"
if port.isdigit():
    port = int(port)
    print(f"Port is valid: {port}")
else:
    print("Port is not a valid integer")
    
# Print only error messages from a list of log entries.

logs = [
    "INFO: Service started successfully.",
    "ERROR: Failed to connect to database.",
    "WARNING: Disk space is running low.",
    "ERROR: Unable to find configuration file."
]
error_logs = [log for log in logs if "ERROR" in log]
print(error_logs)

#What data type to use for a JSON config?

#Answer: Use a dict in Python.
# Example of a JSON config represented as a Python dictionary
json_config = {
    "version": "1.0",
    "services": {
        "web": {
            "port": 80,
            "ssl": True
        },
        "db": {
            "host": "localhost",
            "port": 3306,
            "user": "admin",
            "password": "secret"
        }
    },
    "logging": {
        "level": "INFO",
        "file": "/var/log/app.log"
    }
} 
  