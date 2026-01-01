# UnstitchFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeatures.h>

## Description

Collection that provides access to all of the existing Unstitch features in a component and supports the ability to create new Unstitch features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](UnstitchFeatures_add.htm) | Creates a new Unstitch feature. |
| [classType](UnstitchFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](UnstitchFeatures_item.htm) | Function that returns the specified Unstitch feature using an index into the collection. |
| [itemByName](UnstitchFeatures_itemByName.htm) | Function that returns the specified unstitch feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](UnstitchFeatures_count.htm) | The number of Unstitch features in the collection. |
| [isValid](UnstitchFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](UnstitchFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.unstitchFeatures](Features_unstitchFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Unstitch Feature API Sample](UnstitchFeatureSample_Sample.htm) | Demonstrates creating a new unstitch feature |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |