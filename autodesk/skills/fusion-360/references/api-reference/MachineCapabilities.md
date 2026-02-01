# MachineCapabilities Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineCapabilities.h>

## Description

Object that represents the capabilities of the machine.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachineCapabilities_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [additiveTechnology](MachineCapabilities_additiveTechnology.htm) | Gets which additive technology the machine supports. Return "NA" if the machine does not support Additive |
| [isAdditiveSupported](MachineCapabilities_isAdditiveSupported.htm) | Gets and sets if the machine is capable of additive operations. |
| [isCuttingSupported](MachineCapabilities_isCuttingSupported.htm) | Gets and sets if the machine is capable of subtractive cutting. |
| [isMillingSupported](MachineCapabilities_isMillingSupported.htm) | Gets and sets if the machine is capable of subtractive milling. |
| [isTurningSupported](MachineCapabilities_isTurningSupported.htm) | Gets and sets if the machine is capable of subtractive turning. |
| [isValid](MachineCapabilities_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MachineCapabilities_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Machine.capabilities](Machine_capabilities.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |