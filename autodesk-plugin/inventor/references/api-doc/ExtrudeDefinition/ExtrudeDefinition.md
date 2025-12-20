# ExtrudeDefinition Object

## Description

ExtrudeDefinition Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../ExtrudeDefinition/ExtrudeDefinition_Copy.md) | Method that creates a copy of this ExtrudeDefinition object. The new ExtrudeDefinition object is independent of any feature. It can edited and used as input to edit an existing feature or to create a new Extrude feature. |
| [SetDistanceExtent](../ExtrudeDefinition/ExtrudeDefinition_SetDistanceExtent.md) | Method that changes the extents to be “distance” extents. If this method is called on an asymmetric extrude, the second direction extent is removed. To change extent values, use the properties on the object returned by the Extent property. |
| [SetDistanceExtentTwo](../ExtrudeDefinition/ExtrudeDefinition_SetDistanceExtentTwo.md) | Method that sets the second direction extent to be “distance” extents. This method returns an error if the first extent type is not distance extent. |
| [SetDistanceFromFaceExtent](../ExtrudeDefinition/ExtrudeDefinition_SetDistanceFromFaceExtent.md) | Method that changes the extents to be “Distance From Face” extents. |
| [SetFromToExtent](../ExtrudeDefinition/ExtrudeDefinition_SetFromToExtent.md) | Method that changes the extents to be “from and to face” extents. |
| [SetThroughAllExtent](../ExtrudeDefinition/ExtrudeDefinition_SetThroughAllExtent.md) | Method that changes the extents to be “through all” extents. |
| [SetToExtent](../ExtrudeDefinition/ExtrudeDefinition_SetToExtent.md) | Method that changes the extents to be “to entity” extents. |
| [SetToNextExtent](../ExtrudeDefinition/ExtrudeDefinition_SetToNextExtent.md) | Method that changes the extents to be “to next face” extents. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedBodies](../ExtrudeDefinition/ExtrudeDefinition_AffectedBodies.md) | Read-write property that gets and sets the collection of bodies affected by this feature. If this property is not set for multi-body parts, the default solid body is used as the affected body. This property applies only to features in a part. |
| [AffectedOccurrences](../ExtrudeDefinition/ExtrudeDefinition_AffectedOccurrences.md) | Read-write property that gets and sets the collection of occurrences that should participate in this feature. If this property is not set, all possible occurrences will participate. This property applies only to features in an assembly. |
| [Application](../ExtrudeDefinition/ExtrudeDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Extent](../ExtrudeDefinition/ExtrudeDefinition_Extent.md) | Read-only property that returns the PartFeatureExtent object that defines how the extent of the feature is defined. The type of extent object returne. |
| [ExtentTwo](../ExtrudeDefinition/ExtrudeDefinition_ExtentTwo.md) | Read-only property that returns the PartFeatureExtent object that defines how the second direction extent of the feature is defined. The type of exte. |
| [ExtentTwoType](../ExtrudeDefinition/ExtrudeDefinition_ExtentTwoType.md) | Read-only property that returns an enum indicating how the second direction extent of the feature is defined. This indicates the type of object retur. |
| [ExtentType](../ExtrudeDefinition/ExtrudeDefinition_ExtentType.md) | Read-only property that returns an enum indicating how the extent of the feature is defined. This indicates the type of object returned by the Extent. |
| [InferiMates](../ExtrudeDefinition/ExtrudeDefinition_InferiMates.md) | Read-write property that gets and sets whether to automatically place iMates on full circular edges. If set to True, Inventor places the iMates on cl. |
| [IsTwoDirectional](../ExtrudeDefinition/ExtrudeDefinition_IsTwoDirectional.md) | Read-only property that returns whether extents have been defined in two directions for the extrude. If this property returns True, the ExtentTwoType. |
| [MatchShape](../ExtrudeDefinition/ExtrudeDefinition_MatchShape.md) | Read-write property that gets and sets how open profiles are handled. |
| [Operation](../ExtrudeDefinition/ExtrudeDefinition_Operation.md) | Read-write property that gets and sets the type of operation used to add the feature to the model. Valid inputs are kNewBodyOperation, kJoinOperation, kCutOperation, kIntersectOperation and kSurfaceOperation. |
| [Parent](../ExtrudeDefinition/ExtrudeDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Profile](../ExtrudeDefinition/ExtrudeDefinition_Profile.md) | Read-write property gets and sets the sketch profile used for the extrude feature. |
| [TaperAngle](../ExtrudeDefinition/ExtrudeDefinition_TaperAngle.md) | Read-write property that provides access to the taper angle of an extrude feature. If not supplied, the feature will be created with a taper angle of. |
| [TaperAngleTwo](../ExtrudeDefinition/ExtrudeDefinition_TaperAngleTwo.md) | Read-write property that provides access to the second direction taper angle of an asymmetric extrude feature. This property is not applicable and ret. |
| [Type](../ExtrudeDefinition/ExtrudeDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ExtrudeDefinition.Copy](../ExtrudeDefinition/ExtrudeDefinition_Copy.md), [ExtrudeFeature.Definition](../ExtrudeFeature/ExtrudeFeature_Definition.md), [ExtrudeFeatureProxy.Definition](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Definition.md), [ExtrudeFeatures.CreateExtrudeDefinition](../ExtrudeFeatures/ExtrudeFeatures_CreateExtrudeDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Display feature information](../../sample-programs/DumpFeatureInfo_Sample.md) | Displays information about all of the extrude features in the active document. A part document must be active when this is run. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |