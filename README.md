### About

A NestML implementation of Neuron simulator IntFire models.

### Usage

The model can be used as a custom Nest model.
```python
nest.Install("neuron_simulator_models")
neuron = nest.Create(
    'int_fire1', params={
        'tau': 0.6,
        'refrac': 200.0,
    }
)
```


### Build
Models are written in NestML. **IMPORTANT!** For the time of writing this README, [NestML](https://github.com/nest/nestml/tree/31f4b97dab299150bb44f4dcfdc7fac499a81b38) worked for me only with Python2.7. Keep it in mind when building this model.

Please use `build.sh` to prepare the model for NEST. It requires that you have a proper installation of NestML and there is an environment var `NESTML_INSTALL_DIR` that leads to it. In case of a successful building the `build` dir should contain a NEST model and this model should be accessible in NEST under the namespace `research_team_models`. Please see Usage above.
  
The below instructions are given in case you want to customize the build process. The location for these instructions is the **project's root** location.

To build the model for NEST:
```
java -jar <path to nestml 'target' dir>nestml.jar research_team_models --target build
```

To install the built to NEST:
```
cd build
cmake -Dwith-nest=$NEST_INSTALL_DIR/bin/nest-config .
make all
make install
```

More details in the [NestML repo](https://github.com/nest/nestml/#installing-and-running-nestml)

### Verification

We use a corresponding Neuron model for verification.
