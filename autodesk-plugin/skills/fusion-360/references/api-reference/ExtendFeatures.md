# ExtendFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeatures.h>

## Description

Collection that provides access to all of the existing Extend features in a component and supports the ability to create new Extend features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ExtendFeatures_add.htm) | Creates a new extend feature. |
| [classType](ExtendFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](ExtendFeatures_createInput.htm) | Creates an ExtendFeatureInput object. Use properties and methods on this object to define the extend feature you want to create and then use the Add method, passing in the ExtendFeatureInput object. |
| [item](ExtendFeatures_item.htm) | Function that returns the specified extend feature using an index into the collection. |
| [itemByName](ExtendFeatures_itemByName.htm) | Function that returns the specified extend feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ExtendFeatures_count.htm) | The number of Extend features in the collection. |
| [isValid](ExtendFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ExtendFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.extendFeatures](Features_extendFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [extendFeatures.add](extendFeatures_add_Sample.htm) | Demonstrates the extendFeatures.add method. To use this sample, have a design open that contains at least one surface body. When you run the sample, you will be prompted to select an open edge of the body. |
| [Extend Feature API Sample](ExtendFeatureSample_Sample.htm) | Demonstrates creating a new extend feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |