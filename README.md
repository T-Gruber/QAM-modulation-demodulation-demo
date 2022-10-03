# Quadrature-Amplitude-Modulation

QAM is a modulation method use in telecommunications.
The available demonstrations for modulation and demodulatoin clarify the mode of operation (for QPSK/4-QAM).

# Requirements
- Python 3
- Python packages:
    - matplotlib
    - numpy 
    - scipy

# QAM Modulation
The transmitted signal results from the superposition of a quadrature and in-phase component, which are 90 degrees out of phase. According to the following equation [1]:
$$I(t)cos(2 \pi ft) + Q(t)cos(2 \pi ft + \pi /2) = I(t)cos(2 \pi ft) - Q(t)sin(2 \pi ft) = A(t)cos(2 \pi ft + \phi(t))$$
$$A(t) = \sqrt(I(t)^2+Q(t)), \phi(t) = arctan(\frac{Q(t)}{I(t)})$$

The corressponding demonstration shows the quadrature, in-phase component as well as the superposition of both. on the other hand, the resulting position is also shown in the constellation diagram.

Run QAM_Modulation.py
```console
python3 QAM_Modulation.py
```
![Alt text](QAM_modulation.png?raw=true "QAM demodulation")


# QAM Demodulation
The quadrature and in-phase components can be recovered from the transmitted signal. To do this, superimpose the original modulation signal with the transmitted signal for the in-phase component, low-pass filter it and then amplify it (analogously for the quadrature component). According to the following equation [1]:
$$I(t) = s(t)cos(2 \pi ft) = I(t)cos(2 \pi ft)cos(2 \pi ft) - Q(t)sin(2 \pi ft)cos(2 \pi ft)$$ 
$$= \frac{1}{2}I(t)(1+cos(4 \pi ft)) - \frac{1}{2}Q(t)sin(4 \pi ft)$$
$$= \frac{1}{2}I(t)+ \frac{1}{2}(I(t)cos(4 \pi ft)- Q(t)sin(4 \pi ft)$$ 
$$= \frac{1}{2}I(t) (lowpass filtered) = I(t) (amplified))$$

Run QAM_Demodulation.py
```console
python3 QAM_Demodulation.py
```

![Alt text](QAM_demodulation.png?raw=true "QAM demodulation")


# References
- https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation