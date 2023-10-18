import fygenlib.fygen as fygen

def set_params(freq, wave, *ports):
  i = 0
  fygens = []
  for port in ports:
    fygens.append(fygen.FYGen(port, debug_level=0))
    i += 1

  for fygenerator in fygens:
    angle1 = 360 / len(fygens)
    angle2 = angle1/2
    fygenerator.set(
      channel=fygen.CH1,
      enable=True,
      wave=wave,
      offset_volts=0,
      phase_degrees=angle1*i,
      freq_hz=freq/1000000, #MHz!
      volts=5)
    fygenerator.set(
      channel=fygen.CH2,
      enable=True,
      wave=wave,
      offset_volts=0,
      phase_degrees=angle1*i + angle2,
      freq_hz=freq/1000000, #MHz!
      volts=5)
    i+=1

def main():
  set_params(6000, 'sin', 'COM9', 'COM10', 'COM11')

if __name__ == "__main__":
  main()