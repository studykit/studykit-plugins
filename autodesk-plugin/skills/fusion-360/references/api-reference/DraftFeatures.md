# DraftFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatures.h>

## Description

Collection that provides access to all of the existing draft features in a component and supports the ability to create new draft features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](DraftFeatures_add.htm) | Creates a new draft feature. |
| [classType](DraftFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](DraftFeatures_createInput.htm) | Creates a DraftFeatureInput object. Use properties and methods on this object to define the draft you want to create and then use the Add method, passing in the DraftFeatureInput object. |
| [item](DraftFeatures_item.htm) | Function that returns the specified draft feature using an index into the collection. |
| [itemByName](DraftFeatures_itemByName.htm) | Function that returns the specified draft feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](DraftFeatures_count.htm) | The number of draft features in the collection. |
| [isValid](DraftFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DraftFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.draftFeatures](Features_draftFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Draft Feature API Sample](DraftFeatureSample_Sample.htm) | Demonstrates creating a new draft feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |