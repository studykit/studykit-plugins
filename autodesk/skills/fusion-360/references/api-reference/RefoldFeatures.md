# RefoldFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RefoldFeatures.h>

## Description

Collection that provides access to all of the existing refold features in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RefoldFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](RefoldFeatures_item.htm) | Function that returns the specified refold feature using an index into the collection. |
| [itemByName](RefoldFeatures_itemByName.htm) | Function that returns the specified refold feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](RefoldFeatures_count.htm) | The number of refold features in the collection. |
| [isValid](RefoldFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RefoldFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.refoldFeatures](Features_refoldFeatures.htm)

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |