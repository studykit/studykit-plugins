# GeneratedData Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/GeneratedData/GeneratedData.h>

## Description

Parent class of all generated data classes. Acts like a void pointer for the entries in the OperationBase.GeneratedDataCollection property.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](GeneratedData_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](GeneratedData_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](GeneratedData_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[GeneratedDataCollection.item](GeneratedDataCollection_item.htm), [GeneratedDataCollection.itemByIdentifier](GeneratedDataCollection_itemByIdentifier.htm)

## Derived Classes

[OptimizedOrientationResults](OptimizedOrientationResults.htm)

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |