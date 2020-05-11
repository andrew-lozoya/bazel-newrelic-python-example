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

Generate some load to the web server:
``` shell
curl --request GET --url http://localhost:8080/andrewlozoya

127.0.0.1 - - [08/May/2020 21:47:01] "GET /andrewlozoya HTTP/1.1" 200 -
```
In as little as a minute, your application will batch send data to New Relic and you'll be able to start monitoring your application's performance.

# New Relic Instrumentation

Since we can not use the recommend `newrelic-admin` wrapper script in Bazel builds. We must import a Python agent package into your app and make a call to [`initialize`](https://docs.newrelic.com/docs/agents/python-agent/python-agent-api/initialize) the agent. This call modifies your app's import mechanism so that when libraries are imported, the New Relic agent listens for the function classes it recognizes.

Once [`initialize`](https://docs.newrelic.com/docs/agents/python-agent/python-agent-api/initialize) is called, it sets up the Python agent to be being manually integrated with a Python application.

Keep in mind unlike standard Python functionality, the import order matters! The New Relic package **MUST** be imported at the earliest for best results. For WSGI and application script files, place the initialize call before all imports, with the exception of the sys import and updates to the sys.path. If you call initialize multiple times, the agent ignores calls after the first if the configuration file and environment options are the same.

For web transactions, the agent normally registers automatically when the first web request or background task occurs of a known framework. Because server-side registration can take upto a second or two, details are usually lost from the earliest transactions.

This can be avoided by forcing registration with [`register_application`](https://docs.newrelic.com/docs/agents/python-agent/python-agent-api/register_application) API, though doing so means your app may wait for registration to complete before serving any web requests or running background tasks. This API should be noted for all ephemera type appliction use-cases.

```python
import newrelic.agent

newrelic.agent.initialize()

settings = newrelic.agent.global_settings()
settings.license_key = 'NEWRELIC_LICENSE_KEY'
settings.app_name = 'BazelExample'
settings.log_file = './newrelic-python-agent.log'
settings.log_level = 'INFO'
settings.distributed_tracing.enabled = True
settings.browser_monitoring.auto_instrument = True
... YOUR_OTHER_IMPORTS

if __name__ == "__main__":
    newrelic.agent.register_application()
    dostuff()
```

# Unsupported or Non-Web frameworks
When working with unsupported or non-web background applications its best to use [`register_application`](https://docs.newrelic.com/docs/agents/python-agent/python-agent-api/register_application) call to immediately register the  the agent with the New Relic collector.

Do not call register_application with a non-zero timeout when the Python global import lock will be held. In other words, do not call it in a module file at global scope while the module is being imported. Doing so may result in a temporary deadlock with the background thread created by this call (the deadlock will not be broken until the timeout expires).

For Gunicorn: The deadlock issue just described can also occur when using Gunicorn. The problem is that triggering `register_application` from the WSGI module is not safe, because it preloads the module into the parent process. To use `register_application` with Gunicorn (with or without a timeout) call it from a `post_fork()` callback. This is not a problem with Apache/mod_wsgi, since those tools have been designed not to do this, so it is safe to create background threads when the WSGI application is loaded.

Please refer to the [`New Relic Python API`](https://docs.newrelic.com/docs/agents/python-agent/python-agent-api) for more New Relic Python API best practices and [`guides`](https://docs.newrelic.com/docs/agents/python-agent/api-guides/guide-using-python-agent-api).

# Agent Configurations
New Relic for Python lets you futher change the default behavior of the New Relic Python agent using addtional  [configuration options](https://docs.newrelic.com/docs/agents/python-agent/configuration/python-agent-configuration#environment-variables). However, the [`global_settings`](https://docs.newrelic.com/docs/agents/python-agent/python-agent-api/global_settings) must accessed **after** the agent is initialized, along with any overrides from user environment variables. If you call [`initialize`](https://docs.newrelic.com/docs/agents/python-agent/python-agent-api/initialize) with no arguments, like in this example the agent will assume you have already specified your license key with the NEW_RELIC_LICENSE_KEY environment variable.

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
