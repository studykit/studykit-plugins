# DataHubs Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataHubs.h>

## Description

Collection object that provides a list of all available hubs.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [asArray](DataHubs_asArray.htm) | Get the current list of all hubs. |
| [classType](DataHubs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](DataHubs_item.htm) | Returns the specified hub. |
| [itemById](DataHubs_itemById.htm) | Returns the hub specified using the ID of the hub. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](DataHubs_count.htm) | The number of hubs in this collection. |
| [isValid](DataHubs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DataHubs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Data.dataHubs](Data_dataHubs.htm)

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |