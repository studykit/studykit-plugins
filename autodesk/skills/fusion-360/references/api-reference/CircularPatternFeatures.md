# CircularPatternFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeatures.h>

## Description

Collection that provides access to all of the existing circular pattern features in a component and supports the ability to create new circular pattern features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](CircularPatternFeatures_add.htm) | Creates a new circular pattern feature. |
| [classType](CircularPatternFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](CircularPatternFeatures_createInput.htm) | Creates a CircularPatternFeatureInput object. Use properties and methods on this object to define the circular pattern you want to create and then use the Add method, passing in the CircularPatternFeatureInput object. |
| [item](CircularPatternFeatures_item.htm) | Function that returns the specified circular pattern feature using an index into the collection. |
| [itemByName](CircularPatternFeatures_itemByName.htm) | Function that returns the specified circular pattern feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](CircularPatternFeatures_count.htm) | The number of circular pattern features in the collection. |
| [isValid](CircularPatternFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CircularPatternFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.circularPatternFeatures](Features_circularPatternFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [CircularPattern Feature API Sample](CircularPatternFeatureSample_Sample.htm) | Demonstrates creating a new circular pattern feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |