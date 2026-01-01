# MachineSpindleInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineSpindleInput.h>

## Description

Object representing the set of inputs required to create a new MachineSpindle.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachineSpindleInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [description](MachineSpindleInput_description.htm) | The description of this spindle. |
| [isValid](MachineSpindleInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [maxSpeed](MachineSpindleInput_maxSpeed.htm) | Specifies the maximum speed (rpm) for this spindle. |
| [minSpeed](MachineSpindleInput_minSpeed.htm) | Specifies the minimum speed (rpm) for this spindle. |
| [objectType](MachineSpindleInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [peakTorque](MachineSpindleInput_peakTorque.htm) | ![Preview](../images/TestTubeSmall.png)Specifies the peak torque for this spindle. |
| [peakTorqueSpeed](MachineSpindleInput_peakTorqueSpeed.htm) | ![Preview](../images/TestTubeSmall.png)Specifies the peak torque speed for this spindle. |
| [power](MachineSpindleInput_power.htm) | ![Preview](../images/TestTubeSmall.png)Specifies the power for this spindle. |

## Accessed From

[MachinePartInput.createSpindleInput](MachinePartInput_createSpindleInput.htm), [MachinePartInput.spindleInput](MachinePartInput_spindleInput.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |