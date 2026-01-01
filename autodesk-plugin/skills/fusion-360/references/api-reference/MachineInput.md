# MachineInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineInput.h>

## Description

Base abstract class for inputs to be used when creating machines. Used by Machine.create(MachineInput) method. Implemented by "MachineFromFileInput" and "MachineFromLibraryinput" classes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachineInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](MachineInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MachineInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Derived Classes

[MachineFromFileInput](MachineFromFileInput.htm), [MachineFromLibraryInput](MachineFromLibraryInput.htm), [MachineFromTemplateInput](MachineFromTemplateInput.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |