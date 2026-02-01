# PathPatternFeatures Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeatures.h>

## Description

Collection that provides access to all of the existing path pattern features in a component and supports the ability to create new path pattern features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](PathPatternFeatures_add.htm) | Creates a new path pattern feature. |
| [classType](PathPatternFeatures_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](PathPatternFeatures_createInput.htm) | Creates a PathPatternFeatureInput object. Use properties and methods on this object to define the path pattern you want to create and then use the Add method, passing in the PathPatternFeatureInput object. |
| [item](PathPatternFeatures_item.htm) | Function that returns the specified path pattern feature using an index into the collection. |
| [itemByName](PathPatternFeatures_itemByName.htm) | Function that returns the specified path pattern feature using the name of the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](PathPatternFeatures_count.htm) | The number of path pattern features in the collection. |
| [isValid](PathPatternFeatures_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](PathPatternFeatures_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Features.pathPatternFeatures](Features_pathPatternFeatures.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Path Pattern Feature API Sample](PathPatternFeatureSample_Sample.htm) | Demonstrates creating a new path pattern feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |