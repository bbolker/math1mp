#! /usr/bin/python
import sys
import os
import midi

## from http://www.atonalmicroshores.com/2014/03/bjorklund-py/
## also see https://github.com/brianhouse/bjorklund
##    (recursive algorithm)
def bjorklund(k, n, r=0):
    """Compute bjorklund's algorithm

    k: number of pulses (negative to reverse)
    n: number of steps (negative to change 0/1 pattern)
    r: rotate
    """
    
    A_val = 1
    B_val = 0
    reverse = False
    if k < 0:
        k = abs(k)
        reverse = True
    if n <= 0:
        if n == 0:
            # lazy error handling
            return []
        n = abs(n)
        A_val = 0
        B_val = 1
    ## initialize pattern        
    A = [[A_val]] * k
    B = [[B_val]] * (n-k)
    A_groups = len(A)
    least = min(A_groups, len(B))
    while least > 1:
        for x in range(least):
            A[x] = A[x] + B[x]
        if least == A_groups:
            B = B[least:]
        else:
            A, B = A[:least], A[least:]
        A_groups = len(A)
        least = min(A_groups, len(B))
    output = []
    for group in A:
        output = output + group
    for group in B:
        output = output + group
    if reverse:
        output.reverse()
    if r != 0:
        output = output[r:] + output[:r]
    return output

def track_start(pattern):
    # Instantiate a MIDI Pattern (contains a list of tracks)
    # Instantiate a MIDI Track (contains a list of MIDI events)
    track = midi.Track()
    # Append the track to the pattern
    pattern.append(track)
    return(track)

def track_add(track,pitch=midi.A_5,length=200):
    # Instantiate a MIDI note on event, append it to the track
    on = midi.NoteOnEvent(tick=0, velocity=20, pitch=pitch)
    track.append(on)
    midi.InstrumentNameEvent(name='Glockenspiel')
    # Instantiate a MIDI note off event, append it to the track
    off = midi.NoteOffEvent(tick=length, pitch=pitch)
    track.append(off)
    return(track)

def sound_pattern(vals,pitches=[midi.A_4,midi.A_5],length=200,
                  repeat=1,play=True,instrument=115):
    pattern = midi.Pattern()
    track = track_start(pattern)
    for i in vals*repeat:
        track_add(track,pitch=pitches[i],length=length)
        # Add the end of track event, append it to the track
    eot = midi.EndOfTrackEvent(tick=1)
    track.append(eot)
    midi.write_midifile("example.mid", pattern)
    if play:
        os.system("timidity -A800 --default-program="+format(instrument)+" example.mid >/dev/null")
        os.system("timidity -A800 --default-program="+format(instrument)+" example.mid -Ow bj.wav >/dev/null")
    return(None)

if __name__=='__main__':
    try:
        pulses = int(sys.argv[1])
        steps = int(sys.argv[2])
        rot = int(sys.argv[3])
        reps = int(sys.argv[4])
        length = int(sys.argv[5])
    except Exception:
        print("usage: python eucrhythm.py <PULSES> <STEPS> <ROT> <REPS> <LENGTH>")
    else:
        print("args:",pulses,steps,rot,reps,length)
        music = bjorklund(pulses, steps, rot)*reps
        print("pattern:",music)
        sound_pattern(music,length=length)

