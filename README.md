# `hydra_description` package

[![license - apache 2.0](https://img.shields.io/:license-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)

This ROS package provides URDF files and meshes for the Hydra multi-robot
system. See this repository's branches for different variants of the multi robot
system configuration. 

<p align="center">
  <img src=https://github.com/alexarbogast/za_ros/assets/46149643/ee7f7bb1-abc0-44a2-aa61-de2652a10314 width=600/>
</p>

> [!NOTE]
> __`robot_positioner`__ variant:
>
> The robot_positioner branch contains an experimental setup using the third
> robot as the positioner. Coordinated motion control for this system
> configuration is still a work in progress.

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

