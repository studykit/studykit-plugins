# RemoveFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RemoveFeatures.h>

## Description

Collection that provides access to all of the existing Remove features in a component and supports the ability to create new Remove features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](RemoveFeatures_add.htm) | Creates a new Remove feature. |
| [classType](RemoveFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](RemoveFeatures_item.htm) | Function that returns the specified Remove feature using an index into the collection. |
| [itemByName](RemoveFeatures_itemByName.htm) | Function that returns the specified remove feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](RemoveFeatures_count.htm) | The number of Remove features in the collection. |
| [isValid](RemoveFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RemoveFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.removeFeatures](Features_removeFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Remove Feature](RemoveFeatureSample_Sample.htm) | Demonstrates creating a new remove feature. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |