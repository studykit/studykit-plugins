# CombineFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeatures.h>

## Description

Collection that provides access to all of the existing Combine features in a component and supports the ability to create new Combine features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](CombineFeatures_add.htm) | Creates a new combine feature. |
| [classType](CombineFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](CombineFeatures_createInput.htm) | Creates a CombineFeatureInput object. Use properties and methods on this object to define the combine you want to create and then use the Add method, passing in the CombineFeatureInput object. |
| [item](CombineFeatures_item.htm) | Function that returns the specified combine feature using an index into the collection. |
| [itemByName](CombineFeatures_itemByName.htm) | Function that returns the specified combine feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](CombineFeatures_count.htm) | The number of combine features in the collection. This property returns nothing in the case where the feature is non-parametric. |
| [isValid](CombineFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CombineFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.combineFeatures](Features_combineFeatures.htm)

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |