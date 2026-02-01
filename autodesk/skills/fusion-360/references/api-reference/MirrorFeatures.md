# MirrorFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeatures.h>

## Description

Collection that provides access to all of the existing mirror features in a component and supports the ability to create new mirror features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](MirrorFeatures_add.htm) | Creates a new mirror feature. |
| [classType](MirrorFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](MirrorFeatures_createInput.htm) | Creates a MirrorFeatureInput object. Use properties and methods on this object to define the mirror you want to create and then use the Add method, passing in the MirrorFeatureInput object. |
| [item](MirrorFeatures_item.htm) | Function that returns the specified mirror feature using an index into the collection. |
| [itemByName](MirrorFeatures_itemByName.htm) | Function that returns the specified mirror feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](MirrorFeatures_count.htm) | The number of mirror features in the collection. |
| [isValid](MirrorFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MirrorFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.mirrorFeatures](Features_mirrorFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Mirror Feature API Sample](MirrorFeatureSample_Sample.htm) | Demonstrates creating a new mirror feature |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |