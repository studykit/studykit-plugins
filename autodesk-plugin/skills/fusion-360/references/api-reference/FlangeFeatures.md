# FlangeFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlangeFeatures.h>

## Description

Collection that provides access to all of the existing flange features in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](FlangeFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](FlangeFeatures_item.htm) | Function that returns the specified flange feature using an index into the collection. |
| [itemByName](FlangeFeatures_itemByName.htm) | Function that returns the specified flange feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](FlangeFeatures_count.htm) | The number of flange features in the collection. |
| [isValid](FlangeFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](FlangeFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.flangeFeatures](Features_flangeFeatures.htm)

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |