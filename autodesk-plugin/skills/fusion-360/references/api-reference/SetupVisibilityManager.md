# SetupVisibilityManager Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Visibility/SetupVisibilityManager.h>

## Description

Class to manage the visibility of various elements of the setup.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SetupVisibilityManager_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](SetupVisibilityManager_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [machineBaseVisible](SetupVisibilityManager_machineBaseVisible.htm) | Controls the visibility of the setup's machine base where it exists. This is always disabled for additive setups. |
| [machineVisible](SetupVisibilityManager_machineVisible.htm) | Controls the visibility of the setup's machine. |
| [objectType](SetupVisibilityManager_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Setup.visibilityManager](Setup_visibilityManager.htm)

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |