# BoxFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoxFeatures.h>

## Description

Collection that provides access to all of the existing box features in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BoxFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](BoxFeatures_item.htm) | Function that returns the specified box feature using an index into the collection. |
| [itemByName](BoxFeatures_itemByName.htm) | Function that returns the specified box feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](BoxFeatures_count.htm) | The number of box features in the collection. |
| [isValid](BoxFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BoxFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.boxFeatures](Features_boxFeatures.htm)

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |