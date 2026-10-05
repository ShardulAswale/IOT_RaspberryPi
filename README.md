# Raspberry Pi Voice-Controlled GPIO

Python desktop experiment controlling GPIO outputs through spoken commands.

## How it works

`alexa.py` provides a Tkinter interface. Pressing Start records microphone audio, sends it to Google's speech recogniser through SpeechRecognition and matches commands such as `light on`, `led off`, `fan on` and `motor off`. Outputs use physical BOARD pins 3 and 5.

## Usage

Requires a Raspberry Pi environment supporting RPi.GPIO, Python with Tkinter, a microphone, SpeechRecognition and its microphone audio backend. Speech recognition requires internet access.

Configure compatible GPIO circuitry for the outputs, then run:

```sh
python alexa.py
```

## Notes

This is a command-matching prototype, not an Amazon Alexa integration. Dependencies and wiring instructions are not bundled. Recognition-error handling needs correction before reliable use.
