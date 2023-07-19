# MidiGen

MidiGen is a Python class that helps you create, modify, and save MIDI files using the Mido library. It provides an object-oriented approach for managing MIDI files and simplifies common MIDI operations such as adding notes, chords, and arpeggios, changing instruments, and managing tempo, time signatures, and key signatures.

## Usage

```python
from midigen import MidiGen

midi_gen = MidiGen(tempo=120, time_signature=(4, 4), key_signature=0)

# Add a program change (instrument) to channel 0
midi_gen.add_program_change(channel=0, program=0)

# Add notes
midi_gen.add_note(60, 64, 500)
midi_gen.add_note(62, 64, 500)

# Add a chord
midi_gen.add_chord([60, 64, 67], 64, 500)

# Add an arpeggio
midi_gen.add_arpeggio([60, 64, 67], 64, 500, 125)

# Save the MIDI file
midi_gen.save('output.mid')
```

### Class Methods

### __init__(self, tempo=120, time_signature=(4, 4), key_signature=0)

The constructor creates a new MidiGen instance with the specified tempo, time signature, and key signature.

### set_tempo(self, tempo)

Sets the tempo (in BPM) for the MIDI file.

### set_time_signature(self, numerator, denominator)

Sets the time signature for the MIDI file.

### set_key_signature(self, key)

Sets the key signature for the MIDI file.

### add_program_change(self, channel, program)

Adds a program change (instrument) event to the specified channel.

A program change is a MIDI message used to change the instrument or sound (also known as "patch" or "preset") used by a synthesizer or other MIDI device. In a General MIDI (GM) system, there are 128 standard instruments that can be selected using program change messages, allowing you to switch between different instrument sounds such as piano, guitar, strings, and more.

In the context of the MidiGen class, the add_program_change method allows you to change the instrument sound for a specific MIDI channel.

### add_control_change(self, channel, control, value)

Adds a control change event to the specified channel.

### add_pitch_bend(self, channel, value)

Adds a pitch bend event to the specified channel.

### add_note(self, note, velocity, duration, time=0)

Adds a note with the specified pitch, velocity, and duration at the given time (in ticks).

### add_chord(self, notes, velocity, duration, time=0)

Adds a chord with the specified notes, velocity, and duration at the given time (in ticks).

### add_arpeggio(self, notes, velocity, duration, arp_duration, time=0)

Adds an arpeggio with the specified notes, velocity, duration, and arpeggio duration at the given time (in ticks).

### quantize(self, time_value, quantization_value)

Quantizes the given time value to the nearest multiple of the quantization value.

### load_midi_file(self, filename)

Loads an existing MIDI file for further processing or manipulation.

### save(self, filename)

Saves the MIDI file to the specified filename.

## Properties

### tempo

The tempo (in BPM) of the MIDI file.

### time_signature

The time signature of the MIDI file.

### key_signature

The key signature of the MIDI file.

### track

The Mido MidiTrack object associated with the MidiGen instance.


## Libraries


### mido
mido is a Python library for working with MIDI (Musical Instrument Digital Interface) messages and files. MIDI is a protocol for representing and communicating musical information, such as notes, control changes, and timing events. The mido library makes it easy to create, parse, and manipulate MIDI messages in Python, as well as read and write MIDI files.

Some key features of mido include:

- MIDI Message handling: mido provides an intuitive interface for creating, parsing, and manipulating MIDI messages, including note on/off, control change, program change, and more.
- MIDI File support: The library allows you to read and write standard MIDI files, which can be used to store and exchange musical information between software and hardware.
- Real-time MIDI I/O: mido supports sending and receiving MIDI messages in real-time using various backends, such as PortMidi, RtMidi, and more. This enables communication with external MIDI devices or software synthesizers.
- MIDI ports and devices: The library can work with MIDI ports and devices, allowing you to connect to and interact with various hardware and software synthesizers, controllers, and sequencers.

mido is a versatile and accessible library for working with MIDI in Python, making it suitable for a wide range of applications, from simple data conversions to more complex real-time MIDI processing and interaction.

<br/>

### isobar
isobar is a Python library for creating and manipulating musical patterns. It provides a high-level interface for working with musical structures, such as sequences, transformations, and scheduling. It can be a powerful tool for composers, musicians, and researchers working with algorithmic music composition and generative systems.

Here are some of the key features of isobar:

- High-level pattern manipulation: isobar provides several built-in pattern classes that can be combined, transformed, and scheduled easily.
- MIDI output: The library supports sending MIDI events to external synthesizers or software, allowing you to integrate it with a variety of music-making environments.
- Flexible scheduling: isobar includes a flexible timing system that allows you to schedule events with precise timing, control tempo, and create complex rhythmic structures.
- Generative algorithms: The library includes built-in support for various generative algorithms, such as Markov chains and Euclidean rhythms, to help create interesting and evolving musical patterns.
