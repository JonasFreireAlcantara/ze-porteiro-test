# Zé Porteiro Test

Implementation of the test automation for the Zé Porteiro mobile app.


## Requirements

- Any IDE (recommended Pycharm)
- Node >= 16 (recommended version)
- NPM  >= 8 (recommended version)
- Python >= 3.7 (recommended to use virtual environment)
- Android SDK (Download Android Studio, will be easier ;) )
- Java

> For easy installation of npm and node version use nvm: https://github.com/nvm-sh/nvm#installing-and-updating

> If you're on linux an easy to manage java versions is using the [SDKMan](https://sdkman.io/) program 

> We recommend you to creating a virtual environment for installing the Python dependencies ;)


## Installation

### Android SDK

Download the Android Studio, and install the most recent Android SDK. After that set
the following environment variables.

- JAVA_HOME - path to installation of java root folder
- ANDROID_HOME - path to the root SDK installation folder
- PATH - add platform-tools and tools directories to the PATH environment variable

### Appium Server

```shell
# Install the globally
npm install -g appium appium-doctor

# Run to test the environment for Android
appium-doctor --android
```

### Appium Client

```shell
# Install the client dependencies
pip install -r requirements.txt
```


