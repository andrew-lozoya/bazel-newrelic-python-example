Introduction
----------------------
[![Bazel](https://img.shields.io/badge/bazelbuild-v3.1.0-76D275?logo=image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiI+DQogIDxzdHlsZT4NCiAgICAucmVndWxhcntmaWxsOiM0M0EwNDc7fSAuZGFyay1sZWZ0e2ZpbGw6IzAwNzAxQTt9IC5kYXJrLXJpZ2h0e2ZpbGw6IzAwNDMwMDt9IC5saWdodHtmaWxsOiM3NkQyNzU7fQ0KICA8L3N0eWxlPg0KDQogIDxwYXRoIGNsYXNzPSJsaWdodCIgICAgICBkPSJNMTQ0IDMyIGwxMTIgMTEyIC0xMTIgMTEyIGwtMTEyIC0xMTJ6Ii8+DQogIDxwYXRoIGNsYXNzPSJyZWd1bGFyIiAgICBkPSJNMzIgMTQ0IHYxMTIgbDExMiAxMTIgdi0xMTJ6Ii8+DQoNCiAgPHBhdGggY2xhc3M9ImxpZ2h0IiAgICAgIGQ9Ik0zNjggMzIgIGwxMTIgMTEyIC0xMTIgMTEyIC0xMTIgLTExMnoiLz4NCiAgPHBhdGggY2xhc3M9InJlZ3VsYXIiICAgIGQ9Ik00ODAgMTQ0IHYxMTIgbC0xMTIgMTEyIHYtMTEyeiIvPg0KDQogIDxwYXRoIGNsYXNzPSJyZWd1bGFyIiAgICBkPSJNMjU2IDE0NCBsMTEyIDExMiAtMTEyIDExMiAtMTEyIC0xMTJ6Ii8+DQogIDxwYXRoIGNsYXNzPSJkYXJrLWxlZnQiICBkPSJNMjU2IDM2OCB2MTEyIGwtMTEyIC0xMTIgIHYtMTEyeiIvPg0KICA8cGF0aCBjbGFzcz0iZGFyay1yaWdodCIgZD0iTTI1NiAzNjggbDExMiAtMTEyIHYxMTIgbC0xMTIgMTEyeiIvPg0KPC9zdmc+DQoNCg==)](https://github.com/bazelbuild/bazel) [![Bazel](https://img.shields.io/badge/bazelfederation-v0.0.1-76D275?logo=image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiI+DQogIDxzdHlsZT4NCiAgICAucmVndWxhcntmaWxsOiM0M0EwNDc7fSAuZGFyay1sZWZ0e2ZpbGw6IzAwNzAxQTt9IC5kYXJrLXJpZ2h0e2ZpbGw6IzAwNDMwMDt9IC5saWdodHtmaWxsOiM3NkQyNzU7fQ0KICA8L3N0eWxlPg0KDQogIDxwYXRoIGNsYXNzPSJsaWdodCIgICAgICBkPSJNMTQ0IDMyIGwxMTIgMTEyIC0xMTIgMTEyIGwtMTEyIC0xMTJ6Ii8+DQogIDxwYXRoIGNsYXNzPSJyZWd1bGFyIiAgICBkPSJNMzIgMTQ0IHYxMTIgbDExMiAxMTIgdi0xMTJ6Ii8+DQoNCiAgPHBhdGggY2xhc3M9ImxpZ2h0IiAgICAgIGQ9Ik0zNjggMzIgIGwxMTIgMTEyIC0xMTIgMTEyIC0xMTIgLTExMnoiLz4NCiAgPHBhdGggY2xhc3M9InJlZ3VsYXIiICAgIGQ9Ik00ODAgMTQ0IHYxMTIgbC0xMTIgMTEyIHYtMTEyeiIvPg0KDQogIDxwYXRoIGNsYXNzPSJyZWd1bGFyIiAgICBkPSJNMjU2IDE0NCBsMTEyIDExMiAtMTEyIDExMiAtMTEyIC0xMTJ6Ii8+DQogIDxwYXRoIGNsYXNzPSJkYXJrLWxlZnQiICBkPSJNMjU2IDM2OCB2MTEyIGwtMTEyIC0xMTIgIHYtMTEyeiIvPg0KICA8cGF0aCBjbGFzcz0iZGFyay1yaWdodCIgZD0iTTI1NiAzNjggbDExMiAtMTEyIHYxMTIgbC0xMTIgMTEyeiIvPg0KPC9zdmc+DQoNCg==)](https://github.com/bazelbuild/bazel-federation) [![PyPI](https://img.shields.io/badge/pypi_newrelic-v5.12.1.141-0ab0bf?logo=image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NCIgaGVpZ2h0PSI2NCI+PHBhdGggZD0iTTYzLjUzIDI1LjE0NWMtMy4wMDMtMTMuOC0xOS41NS0yMS45MTQtMzYuOTY2LTE4LjEzUy0yLjUzIDI1LjA2LjQ3IDM4Ljg1NHMxOS41NSAyMS45MTggMzYuOTYyIDE4LjEzIDI5LjA5OC0xOC4wMjcgMjYuMS0zMS44NHpNMzIuMDAyIDQ0LjcyYTEyLjcyIDEyLjcyIDAgMCAxLTguOTk0LTIxLjcxNCAxMi43MiAxMi43MiAwIDAgMSAyMS43MTQgOC45OTRjMCA3LjAyNS01LjY5NSAxMi43Mi0xMi43MiAxMi43MnoiIGZpbGw9IiMwMDhjOTkiLz48cGF0aCBkPSJNMzQuODEzIDE0LjE5MmMtMTAuMDg2LjAwMi0xOC4yNiA4LjE4LTE4LjI2IDE4LjI2NnM4LjE3OCAxOC4yNiAxOC4yNjQgMTguMjZTNTMuMDggNDIuNTQgNTMuMDggMzIuNDU1YzAtNC44NDQtMS45MjUtOS41LTUuMzUtMTIuOTE1cy04LjA3Mi01LjM1LTEyLjkxNi01LjM0OHpNMzEuOTk4IDQzLjFhMTEuMTEgMTEuMTEgMCAwIDEtNy44NTYtMTguOTY2IDExLjExIDExLjExIDAgMCAxIDE4Ljk2NiA3Ljg1NmMwIDYuMTM0LTQuOTcyIDExLjEwOC0xMS4xMDYgMTEuMXoiIGZpbGw9IiM3MGNjZDMiLz48L3N2Zz4=)](https://pypi.org/project/newrelic/5.12.1.141/) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This project demonstrates the usage of Bazel to retrieve dependencies from `pip` repositories that includes basic New Relic insturmentation with best practices.

To build this example, you will need to [install Bazel](http://bazel.io/docs/install.html).

This application demonstrates the usage of [`rules_python`](https://github.com/bazelbuild/rules_python/) to configure dependencies. The dependencies are configured in the `WORKSPACE` file.

The [`py_binary`](https://docs.bazel.build/versions/master/be/python.html#py_binary) rule then creates an executable Python program consisting of a collection of `.py` source files (possibly belonging to other py_library rules), a `*.runfiles` directory tree containing all the code and data needed by the program at run-time, and a stub script that starts up the program with the correct initial environment and data.

The example code already assumes you've set the following [`NEW_RELIC_LICENSE_KEY`](https://docs.newrelic.com/docs/accounts/install-new-relic/account-setup/license-key) environ:

Build the application using Bazel>=3.0.0 with a the system-wide python interpreter. (Tested on Python3)

``` shell
$ bazel run :bin
Starting local Bazel server and connecting to it...
INFO: Analyzed target //:bin (22 packages loaded, 578 targets configured).
INFO: Found 1 target...
Target //:bin up-to-date:
  bazel-bin/bin
INFO: Elapsed time: 11.867s, Critical Path: 0.12s
INFO: 0 processes.
INFO: Build completed successfully, 5 total actions
INFO: Build completed successfully, 5 total actions
Your New Relic license key is: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

******************************************************
* The system-wide Python version running is : 3.7.7 *
******************************************************

 * Serving Flask app "bin" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
```

To generate load to the web server application:
``` shell
curl --request GET --url http://localhost:8080/andrewlozoya

127.0.0.1 - - [08/May/2020 21:47:01] "GET /andrewlozoya HTTP/1.1" 200 -
```

# New Relic Instrumentation

Since we can not use the recommend `newrelic-admin` wrapper script in Bazel builds. We must import a Python agent package into your app and make a call to [`initialize`](https://docs.newrelic.com/docs/agents/python-agent/python-agent-api/initialize) the agent. This call modifies your app's import mechanism so that when libraries are imported, the New Relic agent listens for the function classes it recognizes.

Once [`initialize`](https://docs.newrelic.com/docs/agents/python-agent/python-agent-api/initialize) is called, it sets up the Python agent but does not register the agent with the collector. The [`register_application`](https://docs.newrelic.com/docs/agents/python-agent/python-agent-api/register_application) call will then register the agent with the New Relic collector.

Keep in mind unlike standard Python functionality, the import order matters! the New Relic package MUST be imported at the earliest. 

```python
import newrelic.agent
settings = newrelic.agent.global_settings()
settings.license_key = 'NEWRELIC_LICENSE_KEY'
settings.app_name = 'BazelExample'
settings.log_file = './newrelic-python-agent.log'
settings.log_level = 'INFO'
settings.distributed_tracing.enabled = True
settings.browser_monitoring.auto_instrument = True

newrelic.agent.initialize()
newrelic.agent.register_application()
```

New Relic for Python lets you futher change the default behavior of the New Relic Python agent using addtional  [configuration options](https://docs.newrelic.com/docs/agents/python-agent/configuration/python-agent-configuration#environment-variables).

| Environment variable | Configuration setting |
| ------ | ------ |
| NEW_RELIC_LICENSE_KEY | license_key |
| NEW_RELIC_APP_NAME | app_name |
| NEW_RELIC_MONITOR_MODE |	monitor_mode |
| NEW_RELIC_DEVELOPER_MODE | developer_mode |
| NEW_RELIC_LOG |	log_file |
| NEW_RELIC_LOG_LEVEL |	log_level |
| NEW_RELIC_HIGH_SECURITY | high_security
| NEW_RELIC_PROXY_SCHEME | proxy_scheme
| NEW_RELIC_PROXY_HOST | proxy_host |
| NEW_RELIC_PROXY_PORT | proxy_port |
| NEW_RELIC_PROXY_USER | proxy_user |
| NEW_RELIC_PROXY_PASS | proxy_pass |
| NEW_RELIC_AUDIT_LOG | audit_log_file |
| NEW_RELIC_STARTUP_TIMEOUT | startup_timeout |
| NEW_RELIC_SHUTDOWN_TIMEOUT | shutdown_timeout |
| NEW_RELIC_LABELS | labels |
| NEW_RELIC_PROCESS_HOST_DISPLAY_NAME | process_host.display_name |
| NEW_RELIC_API_KEY | api_key |
| NEW_RELIC_CA_BUNDLE_PATH | ca_bundle_path |
| NEW_RELIC_DISTRIBUTED_TRACING_ENABLED | distributed_tracing.enabled |
| NEW_RELIC_FEATURE_FLAG |
