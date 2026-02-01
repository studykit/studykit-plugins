# DistanceExtentDefinition Object

Derived from: [ExtentDefinition](ExtentDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceExtentDefinition.h>

## Description

Defines the inputs for a distance ExtentDefinition object. This feature extent type defines the distance as well as whether the extent is symmetric or in only one direction. If the extent is not symmetric, a positive or negative distance can be used to control the direction. For a hole, the IsSymmetric property value will always be false.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DistanceExtentDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](DistanceExtentDefinition_create.htm) | Statically creates a new DistanceExtentDefinition object. This is used as input when defining the extents of a feature to be a specified distance. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [distance](DistanceExtentDefinition_distance.htm) | Returns the parameter controlling the distance. You can edit the distance by editing the value of the parameter object. |
| [isValid](DistanceExtentDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DistanceExtentDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentFeature](DistanceExtentDefinition_parentFeature.htm) | Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null. |

## Accessed From

[DistanceExtentDefinition.create](DistanceExtentDefinition_create.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |