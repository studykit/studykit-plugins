# ConfigurationFuture Object

Derived from: [Future](Future.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationFuture.h>

## Description

Used to check the state of the asynchronous configuration operation

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConfigurationFuture_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ConfigurationFuture_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ConfigurationFuture_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [state](ConfigurationFuture_state.htm) | Returns the current state of the process associated with this future. |

## Accessed From

[ConfigurationRow.generate](ConfigurationRow_generate.htm)

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |