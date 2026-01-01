# TrimFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeatures.h>

## Description

Collection that provides access to all of the existing trim features in a component and supports the ability to create new trim features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](TrimFeatures_add.htm) | Creates a new trim feature. |
| [classType](TrimFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](TrimFeatures_createInput.htm) | Creates a TrimFeatureInput object. Use properties and methods on this object to define the trim feature you want to create and then use the Add method, passing in the TrimFeatureInput object. |
| [item](TrimFeatures_item.htm) | Function that returns the specified trim feature using an index into the collection. |
| [itemByName](TrimFeatures_itemByName.htm) | Function that returns the specified trim feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](TrimFeatures_count.htm) | The number of trim features in the collection. |
| [isValid](TrimFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](TrimFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[Features.trimFeatures](Features_trimFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Trim Feature API Sample](TrimFeatureSample_Sample.htm) | Demonstrates creating a new trim feature. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |