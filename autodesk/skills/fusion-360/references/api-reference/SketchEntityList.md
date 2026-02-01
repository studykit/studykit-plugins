# SketchEntityList Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEntityList.h>

## Description

A list of sketch entities.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SketchEntityList_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](SketchEntityList_item.htm) | Function that returns the specified sketch entity using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](SketchEntityList_count.htm) | Returns the number of sketch entities in the list. |
| [isValid](SketchEntityList_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SketchEntityList_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[SketchPoint.connectedEntities](SketchPoint_connectedEntities.htm)

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |