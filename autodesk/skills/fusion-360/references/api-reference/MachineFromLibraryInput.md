# MachineFromLibraryInput Object

Derived from: [MachineInput](MachineInput.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineFromLibraryInput.h>

## Description

Object used as input to create a machine from library URL. Used by "Machine.create(MachineInput)" method. The object holds the data needed to create a machine from the specified library URL

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MachineFromLibraryInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](MachineFromLibraryInput_create.htm) | Creates a MachineFromLibraryInput object to be used as input for Machine.create method, in order to create a machine from a library location. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ignoreSimulationModel](MachineFromLibraryInput_ignoreSimulationModel.htm) | Gets and sets whether or not to ignore the simulation model when creating or loading the machine. If set to true the simulation model will not be set on the new machine. |
| [isValid](MachineFromLibraryInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MachineFromLibraryInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [url](MachineFromLibraryInput_url.htm) | The URL path to the library machine. |

## Accessed From

[MachineFromLibraryInput.create](MachineFromLibraryInput_create.htm)

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |