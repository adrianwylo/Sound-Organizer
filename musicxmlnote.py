import xml.etree.ElementTree as ET

def collect_notes(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    data = []
    
    for measure_elem in root.iter('measure'):
        measure_number = measure_elem.attrib.get('number')
        measure_n = set()   
        for note_elem in measure_elem.iter('note'):
            pitch_elem = note_elem.find('pitch')
            if pitch_elem is not None:
                step_elem = pitch_elem.find('step')
                octave_elem = pitch_elem.find('octave')
                if step_elem is not None and octave_elem is not None:
                    step = step_elem.text
                    octave = octave_elem.text
                    note = step + octave
                    measure_n.add(note)

        data.append(measure_n)
    
    return data

# Usage example
musicxml_file = '/home/headphones/Desktop/Strings Attached/Musescore files/Experiments/coding.musicxml'
data = collect_notes(musicxml_file)
for measure, notes in enumerate(data):
    print(f"M{measure}: ")
    for el in notes:
        print(el)
    
    