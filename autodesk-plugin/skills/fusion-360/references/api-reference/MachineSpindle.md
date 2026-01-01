# MachineSpindle Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineSpindle.h>

## Description

Object representing a spindle on the machine

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachineSpindle_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [description](MachineSpindle_description.htm) | The description of this spindle. |
| [isValid](MachineSpindle_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [maxSpeed](MachineSpindle_maxSpeed.htm) | Specifies the maximum speed (rpm) for this spindle. |
| [minSpeed](MachineSpindle_minSpeed.htm) | Specifies the minimum speed (rpm) for this spindle. |
| [objectType](MachineSpindle_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [peakTorque](MachineSpindle_peakTorque.htm) | ![Preview](../images/TestTubeSmall.png)Specifies the peak torque (Nm) for this spindle. |
| [peakTorqueSpeed](MachineSpindle_peakTorqueSpeed.htm) | ![Preview](../images/TestTubeSmall.png)Specifies the speed (rpm) at which this spindle reaches peak torque (Nm). |
| [power](MachineSpindle_power.htm) | ![Preview](../images/TestTubeSmall.png)Specifies the power (kW) for this spindle. |

## Accessed From

[MachinePart.spindle](MachinePart_spindle.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |