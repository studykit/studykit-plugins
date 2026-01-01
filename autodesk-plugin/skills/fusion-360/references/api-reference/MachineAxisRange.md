# MachineAxisRange Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisRange.h>

## Description

Class representing limits of motion for a machine axis.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachineAxisRange_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](MachineAxisRange_create.htm) | Creates a new range object with limited extents. Requires min to be less than or equal to max. Types of the fields depend on where this range is being used. Centimeters are used for distances and radians for angles. |
| [createInfinite](MachineAxisRange_createInfinite.htm) | Creates a new unbounded range object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isInfinite](MachineAxisRange_isInfinite.htm) | Is the range infinite. |
| [isValid](MachineAxisRange_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [max](MachineAxisRange_max.htm) | Maximum value of range Type depends on where this range is being used. Centimeters are used for distances and radians for angles. Returns infinity if this range is infinite. |
| [min](MachineAxisRange_min.htm) | Minimum value of range. Type depends on where this range is being used. Centimeters are used for distances and radians for angles. Returns -infinity if this range is infinite. |
| [objectType](MachineAxisRange_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[LinearMachineAxis.physicalRange](LinearMachineAxis_physicalRange.htm), [LinearMachineAxisInput.physicalRange](LinearMachineAxisInput_physicalRange.htm), [MachineAxis.physicalRange](MachineAxis_physicalRange.htm), [MachineAxisInput.physicalRange](MachineAxisInput_physicalRange.htm), [MachineAxisRange.create](MachineAxisRange_create.htm), [MachineAxisRange.createInfinite](MachineAxisRange_createInfinite.htm), [RotaryMachineAxis.physicalRange](RotaryMachineAxis_physicalRange.htm), [RotaryMachineAxisConfiguration.wrapAroundAtRange](RotaryMachineAxisConfiguration_wrapAroundAtRange.htm), [RotaryMachineAxisInput.physicalRange](RotaryMachineAxisInput_physicalRange.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |