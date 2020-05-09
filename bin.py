import os

license_key = os.environ.get("NEW_RELIC_LICENSE_KEY")

import newrelic.agent

settings = newrelic.agent.global_settings()
settings.license_key = license_key
settings.app_name = "BazelExample"
settings.log_file = "./newrelic-python-agent.log"
settings.log_level = "INFO"
settings.distributed_tracing.enabled = True
settings.browser_monitoring.auto_instrument = True

newrelic.agent.initialize()
newrelic.agent.register_application()

import lib


def version():
    """
  Check and show the Python runtime we claim is actual Python runtime
  """
    python_version = lib.python_version()
    print("******************************************************")
    print("* The system-wide Python version running is : %s *" % python_version)
    print("******************************************************" + "\n")


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":

    if "NEW_RELIC_LICENSE_KEY" in os.environ:
        print("Your New Relic license key is: " + license_key + "\n")
        version()
        app.run(host="0.0.0.0", port=8080)
    else:
        print("Please set your NEW_RELIC_LICENSE_KEY environ" + "\n")
