# ChamferEdgeSets Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferEdgeSets.h>

## Description

Collection that provides access to all of the existing chamfer edge sets associated with a chamfer feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addDistanceAndAngleChamferEdgeSet](ChamferEdgeSets_addDistanceAndAngleChamferEdgeSet.htm) | Adds a set of edges an equal distance offset to this chamfer feature. |
| [addEqualDistanceChamferEdgeSet](ChamferEdgeSets_addEqualDistanceChamferEdgeSet.htm) | Adds a set of edges an equal distance offset to this chamfer feature.   To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [addTwoDistancesChamferEdgeSet](ChamferEdgeSets_addTwoDistancesChamferEdgeSet.htm) | Adds a set of edges an equal distance offset to this chamfer feature.   To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [classType](ChamferEdgeSets_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ChamferEdgeSets_item.htm) | Function that returns the specified chamfer edge set using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ChamferEdgeSets_count.htm) | The number of chamfer edge sets in the collection. |
| [isValid](ChamferEdgeSets_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ChamferEdgeSets_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[ChamferFeature.edgeSets](ChamferFeature_edgeSets.htm), [ChamferFeatureInput.chamferEdgeSets](ChamferFeatureInput_chamferEdgeSets.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Equal Distance Chamfer Feature API Sample](EqualDistanceChamferFeature_Sample.htm) | Creates an equal distance chamfer on the selected edge. If there are tangent contiguous edges that will also be included in the chamfer. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |