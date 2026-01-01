# ReverseNormalFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReverseNormalFeatures.h>

## Description

Collection that provides access to all of the existing Reverse Normal features in a component and supports the ability to create new Reverse Normal features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ReverseNormalFeatures_add.htm) | Creates a new Reverse Normal feature. |
| [classType](ReverseNormalFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ReverseNormalFeatures_item.htm) | Function that returns the specified Reverse Normal feature using an index into the collection. |
| [itemByName](ReverseNormalFeatures_itemByName.htm) | Function that returns the specified reverse normal feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ReverseNormalFeatures_count.htm) | The number of Reverse Normal features in the collection. |
| [isValid](ReverseNormalFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ReverseNormalFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.reverseNormalFeatures](Features_reverseNormalFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Reverse Normal Feature](ReverseNormalFeatureSample_Sample.htm) | Demonstrates creating a new reverse normal feature. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |