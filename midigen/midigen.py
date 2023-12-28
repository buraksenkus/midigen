from typing import List, Tuple
import os, time
from music21 import scale as m21_scale
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo
from midigen.key import Key, VALID_KEYS
from midigen.track import Track


class MidiGen:
    def __init__(
        self,
        tempo: int = 120,
        time_signature: Tuple = (4, 4),
        key_signature: Key = None,
    ):
        """
        Initialize a new MidiGen instance.

        :param tempo: The tempo in BPM.
        :param time_signature: 2 ints tuple representing the numerator and denominator.
        :param key_signature: The key signature as a string, e.g., 'C' for C major.
        """
        self.midi_file = MidiFile()
        
        self.tracks = []
        self.tempo = tempo
        self.time_signature = time_signature
        self.key_signature = key_signature if key_signature else Key("C")

        self.set_tempo(tempo)
        self.set_time_signature(*time_signature)
        self.set_key_signature(self.key_signature)

        # Automatically add a default track
        self.active_track_index = None
        self.add_track()
    
    def __str__(self):
        """
        Return a string representation of the MidiGen object.
        :return: A string with the track, tempo, time signature, and key signature of the MidiGen object.
        """
        return (
            f"Track: {self.track}\nTempo: {self.tempo}\n \
            Time Signature: {self.time_signature}\nKey Signature: {self.key_signature}"
        )

    @property
    def midi_file(self) -> MidiFile:
        """
        Get the MIDI file.

        :return: The MIDI file.
        """
        return self.midi_file
    
    def add_track(self):
        """
        Add a new track to the MIDI composition and sets it as the active track.

        :return: The newly created Track instance.
        """
        new_track = Track()
        self.tracks.append(new_track)
        self.active_track_index = len(self.tracks) - 1  # Set the new track as active
        return new_track

    def get_active_track(self):
        """
        Returns the currently active track. If there's only one track, it returns that track.
        """
        if not self.tracks:
            raise ValueError("No tracks available in the MIDI file.")

        if len(self.tracks) == 1:
            return self.tracks[0]

        return self.tracks[self.active_track_index]
    
    def set_active_track(self, track_index):
        """
        Sets the active track based on the provided track index.

        :param track_index: The index of the track to be set as active.
        """
        if track_index >= len(self.tracks):
            raise IndexError("Track index out of range.")
        
        self.active_track_index = track_index
    
    def set_mode(self, key_signature: Key, mode: str) -> None:
        """
        Set the mode of the MidiGen object.

        :param key_signature: The key signature, e.g. 'C'.
        :param mode: The mode, e.g. 'major', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian', 'locrian'.
        """
        allowed_modes = ['major', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian', 'locrian']
        if mode not in allowed_modes:
            raise ValueError(f"Invalid mode. Please use a valid mode from the list: {allowed_modes}")
    
        self.mode = mode
        scale_degree = m21_scale.scale_degrees_to_key(key_signature, mode)
        key = Key(scale_degree, mode)
        self.set_key_signature(key)

    def set_tempo(self, tempo: int) -> None:
        """
        Set the tempo for the MIDI file.

        Args:
            bpm (int): Beats per minute. Must be an integer greater than 0.

        Raises:
            ValueError: If bpm is not an integer or is less than or equal to 0.
        """
        if not isinstance(tempo, int) or tempo <= 0:
            raise ValueError("Invalid tempo value: tempo must be a positive integer")
   
        # Remove existing 'set_tempo' messages
        self.midi_file.tracks[0] = [msg for msg in self.track if msg.type != "set_tempo"]
        self.tempo = bpm2tempo(tempo)
        self.track.append(MetaMessage("set_tempo", tempo=self.tempo))

    def set_time_signature(self, numerator: int, denominator: int) -> None:
        """
        Set the time signature for the MIDI file.

        Args:
            numerator (int): The numerator of the time signature. Must be an integer greater than 0.
            denominator (int): The denominator of the time signature. Must be an integer greater than 0.

        Raises:
            ValueError: If numerator or denominator is not an integer or is less than or equal to 0.
        """
        if not (isinstance(numerator, int) and isinstance(denominator, int)):
            raise ValueError(
                "Invalid time signature value: both numerator and denominator must be integers"
            )

        if numerator <= 0 or denominator <= 0:
            raise ValueError(
                "Invalid time signature value: both numerator and denominator must be positive integers"
            )

        # Remove existing 'time_signature' messages
        self.midi_file.tracks[0] = [msg for msg in self.track if msg.type != "time_signature"]

        self.time_signature = MetaMessage(
            "time_signature", numerator=numerator, denominator=denominator
        )
        self.track.append(self.time_signature)

    def set_key_signature(self, key: Key) -> None:
        """
        Set the key signature for the MIDI file.

        Args:
            key (Key): The key signature. Must be a valid key signature (see Key class).

        Raises:
            ValueError: If key is not a valid key signature string.
        """
        self.key_signature = key
        self.track.append(MetaMessage("key_signature", key=str(key)))

    def save(self, filename: str) -> None:
        """
        Compile all tracks and save the MIDI file to the specified path.

        This method first compiles all the individual tracks into the MidiFile
        and then saves the complete MIDI composition to the specified filename.

        Args:
            filename (str): The path where the MIDI file should be saved.
        """
        self.midi_file.tracks.clear()
        for track in self.tracks:
            self.midi_file.tracks.append(track.get_track())

        # Check for existing file and create a unique filename if necessary
        if os.path.exists(filename):
            base, ext = os.path.splitext(filename)
            filename = f"{base}_{int(time.time())}{ext}"

        # Attempt to save the MIDI file
        try:
            self.midi_file.save(filename)
        except FileNotFoundError:
            raise ValueError(f"Cannot save file: Invalid filename or directory: '{filename}'")
        except PermissionError:
            raise ValueError(f"Cannot save file: Permission denied for directory: '{filename}'")
        except Exception as e:
            raise ValueError(f"Cannot save file: Unknown error: {str(e)}")
