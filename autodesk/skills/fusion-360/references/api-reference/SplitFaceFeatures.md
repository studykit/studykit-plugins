# SplitFaceFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeatures.h>

## Description

Collection that provides access to all of the existing split face features in a component and supports the ability to create new split face features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](SplitFaceFeatures_add.htm) | Creates a new split face feature. |
| [classType](SplitFaceFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](SplitFaceFeatures_createInput.htm) | Creates a SplitFaceFeatureInput object. Use properties and methods on this object to define the split face you want to create and then use the Add method, passing in the SplitFaceFeatureInput object. |
| [item](SplitFaceFeatures_item.htm) | Function that returns the specified split face feature using an index into the collection. |
| [itemByName](SplitFaceFeatures_itemByName.htm) | Function that returns the specified split face feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](SplitFaceFeatures_count.htm) | The number of split face features in the collection. |
| [isValid](SplitFaceFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SplitFaceFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[Features.splitFaceFeatures](Features_splitFaceFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Split Face Feature API Sample](SplitFaceFeatureSample_Sample.htm) | Demonstrates creating a new split face feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |