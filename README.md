# LIF Neuron Simulator

An interactive Leaky Integrate-and-Fire (LIF) neuron simulator I built with Python and Streamlit. Move four sliders and watch a single neuron charge up, fire, and rest.

**Live app:** (https://lif-neuron-simulator-9ysy4vdov5h2ds5iahkyxu.streamlit.app/)

## Why I built this

I'm a Class 11 student interested in neuromorphic engineering and computational neuroscience. I kept reading about the LIF model, but the equation alone didn't click for me. I wanted to change one number and see what the neuron does, so I built this.

## The model

At every time step, the membrane voltage V updates like this:

    V = V + (I - leak * V) * dt

- `I` pushes the voltage up (input current)
- `leak * V` pulls it back down (the "leaky" part)
- When V reaches the threshold, the neuron spikes, V resets to 0, and the neuron rests for the refractory period

## What the sliders do

| Slider | What it controls |
|---|---|
| Input Current | How hard the neuron is being pushed |
| Leak Rate | How fast voltage drains away on its own |
| Threshold | The voltage needed to fire a spike |
| Refractory Period | How many steps the neuron stays silent after a spike |

The graph shows membrane voltage (purple), the threshold (red dashed line), and each spike (orange dots). Below it you get the total spike count and a spike rate.

## Things to try

- Lower the input current until the neuron stops firing completely
- Raise the leak rate and see how much more current it needs to fire
- Set the refractory period to 0 and compare spike counts

## Run it locally

    git clone https://github.com/arush4213/lif-neuron-simulator
    cd lif-neuron-simulator
    pip install streamlit matplotlib
    streamlit run app.py

## Limitations

- It simulates one neuron only, not a network
- Uses simple Euler integration with a fixed step size (dt = 0.5) and 300 steps
- Voltage and current are in arbitrary units, not real biological values

## Built with

Python, Streamlit, Matplotlib

## Author

Arush Kalra
GitHub: [arush4213](https://github.com/arush4213)
LinkedIn: [arush-kalra](https://linkedin.com/in/arush-kalra-3278bb307)
