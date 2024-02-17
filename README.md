# `hydra_description` package

This ROS package provides URDF files and meshes for the Hydra multi-robot
system. See this repository's branches for different variants of the multi robot
system configuration. 

<p align="center">
  <img src=https://github.com/alexarbogast/za_ros/assets/46149643/02d6b3e5-c266-4b67-a2fe-4b5805c6f989 width=600/>
</p>

> [!NOTE]
> __`ampf`__ variant:
>
> The ampf branch contains the setup of the physical system at
> [ampf](https://ampf.research.gatech.edu/).

## Installation

First, create a catkin workspace.

```bash
mkdir -p catkin_ws/src && cd catkin_ws/src
```

#### Dependencies

The multi-robot description depends on the mesh files provided by the
[za_description](https://github.com/alexarbogast/za_description) package.
Install this package locally or, alternatively, clone it as a submodule in
[za_ros](https://github.com/alexarbogast/za_ros) package.

For `za_description` local installation:
```bash
git clone git@github.com:alexarbogast/za_description.git
```
#### Building the package

Clone the contents of this repository and checkout the desired branch.

```bash
git clone git@github.com:alexarbogast/hydra_description.git
git checkout <branch>
```

Build the ROS packages.

```bash
cd ../
catkin build
```

## Resources

- http://wiki.ros.org/xacro
- http://wiki.ros.org/urdf

