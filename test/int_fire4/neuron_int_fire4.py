import pylab
from neuron import h
from neuron import gui  # VERY IMPORTANT to include 'gui'! Despite the fact that it is unused.

RUN_TIME = 200
SPIKES_START = 1
SPIKES_INTERVAL = 20
SPIKES_NUMBER = 10000
SPIKE_TIMES = [i for i in range(SPIKES_START, SPIKES_NUMBER, SPIKES_INTERVAL)]

soma = h.Section(name='soma')

iaf_neuron = h.IntFire4()
iaf_neuron.m = 0.0
iaf_neuron.taue = 0.5
iaf_neuron.taui1 = 5
iaf_neuron.taui2 = 10
iaf_neuron.taum = 30

generator = h.NetStim()
generator.number = SPIKES_NUMBER  # pool of available spike to emit.
generator.start = SPIKES_START
generator.interval = SPIKES_INTERVAL
generator.noise = 0

conn = h.NetCon(generator, iaf_neuron)
conn.delay = 1.0
conn.weight[0] = 0.5
iaf_neuron_nc = h.NetCon(iaf_neuron, None)

m_vec = h.Vector()
t_vec = h.Vector()
spike_vec = h.Vector()
spike_t_vec = h.Vector()
t_vec.record(h._ref_t)
m_vec.record(iaf_neuron._ref_m)
iaf_neuron_nc.record(spike_t_vec, spike_vec, 1)

duration = RUN_TIME
h.tstop = duration
h.run()

pylab.figure("Neuron IntFire")

pylab.subplot(2, 1, 1)
pylab.xlim(0, RUN_TIME)
pylab.plot(t_vec, m_vec, '.')
pylab.ylabel("IntFire m")

pylab.subplot(2, 1, 2)
pylab.xlim(0, RUN_TIME)
pylab.ylim(0, 3)
pylab.plot(SPIKE_TIMES, [2] * len(SPIKE_TIMES), "b.", label='generator')
pylab.plot(spike_t_vec, spike_vec, "r.", label='iaf_neuron')
pylab.ylabel("spikes")
pylab.legend()

pylab.show()
