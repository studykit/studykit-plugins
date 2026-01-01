# RotaryMachineAxis Object

Derived from: [MachineAxis](MachineAxis.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/RotaryMachineAxis.h>

## Description

Object that represents an axis with rotary motion (e.g. A, B, and C).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RotaryMachineAxis_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [axisType](RotaryMachineAxis_axisType.htm) | The type of axis. |
| [hasLimits](RotaryMachineAxis_hasLimits.htm) | Does this axis have a limited range of motion. |
| [homePosition](RotaryMachineAxis_homePosition.htm) | Specifies the value that this axis returns to when the machine is homed. Units are cm for linear axes or radians for rotary axes. Will return NaN if home position isn't set. |
| [isValid](RotaryMachineAxis_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](RotaryMachineAxis_name.htm) | The name of this axis. |
| [objectType](RotaryMachineAxis_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [physicalRange](RotaryMachineAxis_physicalRange.htm) | Range of possible values for this axis. Units are cm for linear axes or radians for rotary axes. |
| [rotationAxis](RotaryMachineAxis_rotationAxis.htm) | The infinite line that defines the direction and location of the axis of rotation. |
| [toolChangePosition](RotaryMachineAxis_toolChangePosition.htm) | ![Preview](../images/TestTubeSmall.png)Specifies the value that this axis returns to, prior to a tool change. Units are cm for linear axes or radians for rotary axes. Will return NaN if tool change position isn't set. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |