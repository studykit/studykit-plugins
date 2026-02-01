# ReplaceFaceFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReplaceFaceFeatures.h>

## Description

Collection that provides access to all of the existing replace face features in a component and supports the ability to create new replace face features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ReplaceFaceFeatures_add.htm) | Creates a new replace face feature. |
| [classType](ReplaceFaceFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](ReplaceFaceFeatures_createInput.htm) | Creates a ReplaceFaceFeatureInput object. Use properties and methods on this object to define the replace face you want to create and then use the Add method, passing in the ReplaceFaceFeatureInput object. |
| [item](ReplaceFaceFeatures_item.htm) | Function that returns the specified replace face feature using an index into the collection. |
| [itemByName](ReplaceFaceFeatures_itemByName.htm) | Function that returns the specified replace face feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ReplaceFaceFeatures_count.htm) | The number of replace face features in the collection. |
| [isValid](ReplaceFaceFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ReplaceFaceFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.replaceFaceFeatures](Features_replaceFaceFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [ReplaceFace Feature](ReplaceFaceFeatureSample_Sample.htm) | Demonstrates creating a new replaceface feature. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |