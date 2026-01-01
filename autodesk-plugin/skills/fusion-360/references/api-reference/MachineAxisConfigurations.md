# MachineAxisConfigurations Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisConfigurations.h>

## Description

Collection of axis configuration objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addLinear](MachineAxisConfigurations_addLinear.htm) | Add a new linear axis configuration for a kinematics part. |
| [addRotary](MachineAxisConfigurations_addRotary.htm) | Add a new rotary axis configuration for a kinematics part. |
| [classType](MachineAxisConfigurations_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](MachineAxisConfigurations_item.htm) | Get the configuration at index in this collection |
| [itemById](MachineAxisConfigurations_itemById.htm) | Get the configuration with the given ID |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](MachineAxisConfigurations_count.htm) | Get the number of configurations in the collection. |
| [isValid](MachineAxisConfigurations_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MachineAxisConfigurations_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[ControllerConfigurationMachineElement.axisConfigurations](ControllerConfigurationMachineElement_axisConfigurations.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |