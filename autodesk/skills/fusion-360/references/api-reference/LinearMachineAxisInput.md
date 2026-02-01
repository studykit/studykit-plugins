# LinearMachineAxisInput Object

Derived from: [MachineAxisInput](MachineAxisInput.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/LinearMachineAxisInput.h>

## Description

Object that defines the properties required to create a new linear machine axis object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](LinearMachineAxisInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [axisType](LinearMachineAxisInput_axisType.htm) | The type of axis. This axis type determines which parameters of this object are valid to be accessed or modified. |
| [direction](LinearMachineAxisInput_direction.htm) | The unit vector that represents the direction along which the linear axis will move. This vector is in the machine's coordinate system (e.g. the X axis is always (1,0,0)). |
| [homePosition](LinearMachineAxisInput_homePosition.htm) | Specifies the value that this axis returns to when the machine is homed. Units are cm for linear axes or radians for rotary axes. |
| [isValid](LinearMachineAxisInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](LinearMachineAxisInput_name.htm) | The user facing name of this axis. |
| [objectType](LinearMachineAxisInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [physicalRange](LinearMachineAxisInput_physicalRange.htm) | Range of possible values for this axis. Units are cm for linear axes or radians for rotary axes. |
| [toolChangePosition](LinearMachineAxisInput_toolChangePosition.htm) | ![Preview](../images/TestTubeSmall.png)Specifies the value that this axis returns to, prior to a tool change. Units are cm for linear axes or radians for rotary axes. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |