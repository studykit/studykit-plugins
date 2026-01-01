# MachineAxis Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxis.h>

## Description

Abstract base class representing a single machine axis.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachineAxis_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [axisType](MachineAxis_axisType.htm) | The type of axis. |
| [hasLimits](MachineAxis_hasLimits.htm) | Does this axis have a limited range of motion. |
| [homePosition](MachineAxis_homePosition.htm) | Specifies the value that this axis returns to when the machine is homed. Units are cm for linear axes or radians for rotary axes. Will return NaN if home position isn't set. |
| [isValid](MachineAxis_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](MachineAxis_name.htm) | The name of this axis. |
| [objectType](MachineAxis_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [physicalRange](MachineAxis_physicalRange.htm) | Range of possible values for this axis. Units are cm for linear axes or radians for rotary axes. |
| [toolChangePosition](MachineAxis_toolChangePosition.htm) | ![Preview](../images/TestTubeSmall.png)Specifies the value that this axis returns to, prior to a tool change. Units are cm for linear axes or radians for rotary axes. Will return NaN if tool change position isn't set. |

## Accessed From

[MachinePart.axis](MachinePart_axis.htm)

## Derived Classes

[LinearMachineAxis](LinearMachineAxis.htm), [RotaryMachineAxis](RotaryMachineAxis.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |