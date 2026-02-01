# MachineFromTemplateInput Object

Derived from: [MachineInput](MachineInput.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineFromTemplateInput.h>

## Description

Object used as input to create a machine from a given template. Used by "Machine.create(MachineInput)" method. The object holds the data needed to create a machine based on the specified template.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachineFromTemplateInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](MachineFromTemplateInput_create.htm) | Create a "MachineFromTemplateInput" object to be used as input for "Machine.create(MachineInput)" method. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](MachineFromTemplateInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [machineTemplate](MachineFromTemplateInput_machineTemplate.htm) | Machine template identifier used to generate a certain type of machine. |
| [objectType](MachineFromTemplateInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[MachineFromTemplateInput.create](MachineFromTemplateInput_create.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |