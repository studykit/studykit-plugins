# PersonalUseLimits Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/PersonalUseLimits.h>

## Description

Object that provides information about file limits associated with a "Fusion for Personal Use license".

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](PersonalUseLimits_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [editableFileCount](PersonalUseLimits_editableFileCount.htm) | Returns the current number of documents that are set by the user to be editable. |
| [editableFiles](PersonalUseLimits_editableFiles.htm) | Returns a list of the DataFile objects that have been set by the user to be editable. |
| [isValid](PersonalUseLimits_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [maxEditableFileCount](PersonalUseLimits_maxEditableFileCount.htm) | Returns the maximum number of documents that can be set by the user to be editable. |
| [objectType](PersonalUseLimits_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Data.personalUseLimits](Data_personalUseLimits.htm)

## Version

Introduced in version May 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |