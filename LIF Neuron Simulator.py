import streamlit as st
import matplotlib.pyplot as plt
import time
  
# title and subheading 
st.title("LIF Neuron Simulator")
st.markdown("Adjust the sliders to control how the neuron behaves")

# user control variables
input_current=st.slider("Input Current", 0.0, 3.0, 1.5)      
leak_rate=st.slider("Leak Rate", 0.01, 0.5, 0.1)             
threshold=st.slider("Threshold", 0.5, 3.0, 1.0)              
refractory_period=st.slider("Refractory Period (steps)", 0, 20, 5)

# simulation settings
dt = 0.5      
steps = 300   
voltage = 0.0       
refrac_timer = 0    
voltage_history = []  
spike_times = []      
spike_values = []

# refractory period
for t in range(steps):   
    if refrac_timer > 0:      
        refrac_timer -= 1     
        voltage = 0.0         
    else:                     
        voltage += (input_current - leak_rate * voltage) * dt   
    if voltage >= threshold:                      
        spike_times.append(t)                
        spike_values.append(voltage)
        voltage = 0.0                             
        refrac_timer = refractory_period          
    voltage_history.append(voltage)  
  
# graph
fig, ax = plt.subplots(figsize=(10, 4))   
ax.plot(voltage_history, color='purple', linewidth=2, label='Membrane Voltage')         
ax.axhline(y=threshold, color='red', linestyle='--', linewidth=1.5, label='Threshold')  
ax.scatter(spike_times, spike_values, color='orange', zorder=5, s=80, label='Spike')    
ax.set_xlabel("Time Steps")      
ax.set_ylabel("Membrane Voltage") 
ax.set_xlim(0, steps)            
ax.legend(loc='upper right')     
placeholder = st.empty()   
with placeholder.container():          
    st.pyplot(fig)                     
    col1, col2 = st.columns(2)         
    col1.metric("Total Spikes", len(spike_times))   
    col2.metric("Spike Rate", f"{round(len(spike_times) / (steps * dt) * 1000)} spikes/sec")  
plt.close(fig)       
time.sleep(0.1)      
st.rerun() 
