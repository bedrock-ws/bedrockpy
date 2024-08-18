# Using *bedrockpy* on Android

Because a lot of people might not have a computer to run *bedrockpy*, it
is a common case to run a server on an Android device as well as playing
on it. To avoid jumping around different blog posts, here is a simple
variant to install and use *bedrockpy* on Android.

## Install Termux

Termux is a free and open-source terminal emulator for Android. Download
it from F-Droid [here](https://f-droid.org/en/packages/com.termux/).


## Install Requirements

Open the Termux app and enter the commands below.

```console
pkg in python3
pkg in pipx
pipx install poetry
```


## Create Project

To begin using *bedrockpy*, enter the commands below
and make yourself familar with [Poetry](https://python-poetry.org/)

```shell
mkdir myproject
cd myproject
poetry init
poetry add bedrockpy
```
