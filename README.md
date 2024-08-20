# copper-spack

This is a spack environment for copper.

## How to install Copper with local spack

This assume that you have a valid `spack` in your path

```
module load cmake
spack install mochi-thallium%oneapi
git clone https://github.com/argonne-lcf/copper-spack.git
spack repo add ./copper-spack/
spack install copper%oneapi
```

Then you can simply load copper  via

```
spack load copper
```


## How to load Copper on Aurora


```
module load spack-pe-oneapi copper
```
