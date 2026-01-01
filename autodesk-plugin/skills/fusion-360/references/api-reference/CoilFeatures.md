# CoilFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeatures.h>

## Description

Collection that provides access to all of the existing coil features in a design and supports the ability to create new coil features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CoilFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](CoilFeatures_item.htm) | Function that returns the specified coil feature using an index into the collection. |
| [itemByName](CoilFeatures_itemByName.htm) | Function that returns the specified coil feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](CoilFeatures_count.htm) | The number of coil features in the collection. |
| [isValid](CoilFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CoilFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.coilFeatures](Features_coilFeatures.htm)

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |