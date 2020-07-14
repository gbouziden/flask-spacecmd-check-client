import subprocess
import logging
from os import environ
from flask import Flask, request
 
app = Flask(__name__)
LOGGER = logging.getLogger(__name__)
 
 
@app.route("/", methods=["GET"])
def main():
    """
    Run Bash Script
    :return:
    """
    hostname = request.args.get('hostname')
    # Send Hostname to environment variable
    environ['HOSTNAME'] = hostname
    try:
        output = subprocess.check_output(f'spacecmd --nossl system_search $HOSTNAME | grep $HOSTNAME', shell=True)
        return output
    except subprocess.CalledProcessError as e:
        if 'non-zero' in str(e):
            LOGGER.error(e)
            return ""
        else:
            LOGGER.error(f"Error Occured With Exception: {str(e.output)}")
            raise e
 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')
