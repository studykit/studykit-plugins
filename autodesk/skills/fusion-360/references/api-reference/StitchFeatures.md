# StitchFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeatures.h>

## Description

Collection that provides access to all of the existing Stitch features in a component and supports the ability to create new Stitch features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](StitchFeatures_add.htm) | Creates a new stitch feature. |
| [classType](StitchFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](StitchFeatures_createInput.htm) | Creates a StitchFeatureInput object. Use properties and methods on this object to define the stitch feature you want to create and then use the Add method, passing in the StitchFeatureInput object. |
| [item](StitchFeatures_item.htm) | Function that returns the specified stitch feature using an index into the collection. |
| [itemByName](StitchFeatures_itemByName.htm) | Function that returns the specified stitch feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](StitchFeatures_count.htm) | The number of Stitch features in the collection. |
| [isValid](StitchFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](StitchFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.stitchFeatures](Features_stitchFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Stitch Feature API Sample](StitchFeatureSample_Sample.htm) | Demonstrates creating a new stitch feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |