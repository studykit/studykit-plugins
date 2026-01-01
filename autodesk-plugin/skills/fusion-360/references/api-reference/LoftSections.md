# LoftSections Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSections.h>

## Description

The set of two or more sections used to define the shape of the loft.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](LoftSections_add.htm) | Adds a new section to the loft. The initial end condition is "Free". Additional methods on the returned LoftSection can be used to further define the section. |
| [classType](LoftSections_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](LoftSections_item.htm) | Function that returns the specified LoftSection using an index into the collection. They are returned in the same order that they are used in the loft. Their order can be modified using the reorder method of the LoftSection object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](LoftSections_count.htm) | The number of LoftSections in the collection. |
| [isValid](LoftSections_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](LoftSections_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[LoftFeature.loftSections](LoftFeature_loftSections.htm), [LoftFeatureInput.loftSections](LoftFeatureInput_loftSections.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |