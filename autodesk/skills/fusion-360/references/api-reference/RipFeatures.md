# RipFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatures.h>

## Description

Collection that provides access to all of the existing Rip features in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](RipFeatures_add.htm) | Creates a new Rip feature. |
| [classType](RipFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createRipFeatureInput](RipFeatures_createRipFeatureInput.htm) | Creates a RipFeatureInput object. Use methods on this object to define the rip you want to create and then use the add method, passing in the RipFeatureInput object. |
| [item](RipFeatures_item.htm) | Function that returns the specified Rip feature using an index into the collection. |
| [itemByName](RipFeatures_itemByName.htm) | Function that returns the specified Rip feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](RipFeatures_count.htm) | The number of Rip features in the collection. |
| [isValid](RipFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RipFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.ripFeatures](Features_ripFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Rip Feature Sample](RipFeatureSample_Sample.htm) | Demonstrates creating a new sheet metal rip feature. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |