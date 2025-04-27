# `hydra_description` package

[![license - apache 2.0](https://img.shields.io/:license-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)

This ROS package provides URDF files and meshes for the Hydra multi-robot
system. See this repository's branches for different variants of the multi robot
system configuration. 

<p align="center">
  <img src=https://github.com/alexarbogast/hydra_description/assets/46149643/a3f9397e-aa6c-4c70-a886-bd3c5cb4b925 width=600/>
</p>

> [!NOTE]
> __`ros2`__ variant:
>
> The ros2 branch contains the default setup: Three robots spaced evenly around
> a 1-DOF positioner table.

## Installation

First, create a catkin workspace.

```bash
mkdir -p colcon_ws/src && cd colcon_ws/src
```

#### Dependencies

The multi-robot description depends on the mesh files provided by the
[za_description](https://github.com/alexarbogast/za_description) package.
Install this package locally or, alternatively, clone it as a submodule in
[za_ros](https://github.com/alexarbogast/za_ros) package.

For `za_description` local installation:

```bash
git clone git@github.com:alexarbogast/za_description.git
cd za_description
git checkout ros2
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
colcon build
```

## Resources

- http://wiki.ros.org/xacro
- http://wiki.ros.org/urdf
