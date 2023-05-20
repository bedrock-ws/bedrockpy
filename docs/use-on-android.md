# Using *bedrockpy* on Android

Because a lot of people might not have a computer to run *bedrockpy*, it
is a common case to run a server on an Android device as well as playing
on it. To avoid jumping around different blog posts, here is a simple
variant to install and use *bedrockpy* on Android.

## Install Termux

Termux is a free and open-source terminal emulator for Android. Download
it from [F-Droid](https://f-droid.org/en/packages/com.termux/) **from the
website**.

```{warning}
While Termux is available on the Google Play Store as well, you should
still consider downloading it from F-Droid due to lack of support.
```

## Install Python

{{wip}}

{{needs_research}}

```bash
mkdir -p python/bpy &&
cd $_ &&
pkg in python &&
pip install bedrockpy[fast] &&
```

```{todo}
Provide installer script?
```