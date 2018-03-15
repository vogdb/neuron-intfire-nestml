import nest
import pylab

nest.Install("neuron_simulator_models")
neuron = nest.Create(
    "int_fire4",
    params={'tau_m': 30., 'tau_syn_ex': 0.5, 'tau_syn_in_rise': 5., 'tau_syn_in_fall': 10.}
)
multimeter = nest.Create(
    'multimeter',
    params={"record_from": ["V_m"], "withtime": True, "interval": 0.1}
)

RUN_TIME = 200
SPIKES_START = 1
SPIKES_INTERVAL = 20
SPIKES_NUMBER = 10000
SPIKE_TIMES = [float(i) for i in range(SPIKES_START, SPIKES_NUMBER, SPIKES_INTERVAL)]

generator = nest.Create(
    'spike_generator',
    params={"spike_times": SPIKE_TIMES}
)
detector = nest.Create(
    'spike_detector',
    params={"withtime": True}
)

nest.Connect(multimeter, neuron)
nest.Connect(neuron, detector)
nest.Connect(generator, neuron, syn_spec={
    "delay": 1.0,
    "weight": 0.5,
    "model": "static_synapse"
})
nest.Simulate(RUN_TIME)

pylab.figure("Nest IntFire1")

multimeter_status = nest.GetStatus(multimeter)[0]
multimeter_events = multimeter_status['events']

pylab.subplot(2, 1, 1)
pylab.xlim(0, RUN_TIME)
pylab.plot(multimeter_events['times'], multimeter_events["V_m"], '.')
pylab.ylabel("IntFire1 V_m")

detector_status = nest.GetStatus(detector)[0]
detector_events = detector_status['events']

pylab.subplot(2, 1, 2)
pylab.xlim(0, RUN_TIME)
pylab.ylim(0, 3)
pylab.plot(SPIKE_TIMES, [2] * len(SPIKE_TIMES), "b.", label='generator')
pylab.plot(detector_events['times'], detector_events['senders'], "r.", label='iaf_neuron')
pylab.ylabel("spikes")
pylab.legend()

pylab.show()
