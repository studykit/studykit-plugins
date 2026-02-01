# DistanceFromFaceExtent Object

Derived from: [PartFeatureExtent](../PartFeatureExtent/PartFeatureExtent.md) Object

## Description

The DistanceFromFaceExtent object provides access to the information that defines the extent for a feature that's extent is determined by extruding from a Face with offset. This is derived from the PartFeatureExtent object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AlternateSolutionDirection](../DistanceFromFaceExtent/DistanceFromFaceExtent_AlternateSolutionDirection.md) | Read-write property that gets and sets the alternate solution direction of the feature. Valid input is kPositiveExtentDirection or kNegativeExtentDirection. kPositiveExtentDirection defines the offset direction to be in the same direction as the normal of the sketch plane. |
| [Application](../DistanceFromFaceExtent/DistanceFromFaceExtent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Direction](../DistanceFromFaceExtent/DistanceFromFaceExtent_Direction.md) | Read-write property that gets and sets the distance direction of the feature. Valid input is kPositiveExtentDirection, kNegativeExtentDirection, or kSymmetricExtentDirection. kPositiveExtentDirection defines the offset direction to be in the same direction as the normal of the sketch plane. |
| [Distance](../DistanceFromFaceExtent/DistanceFromFaceExtent_Distance.md) | Read-only property that returns the parameter controlling the distance extent of the feature. |
| [DistanceTwo](../DistanceFromFaceExtent/DistanceFromFaceExtent_DistanceTwo.md) | Read-only property that returns the parameter controlling the distance extent of the feature in the other direction. This returns Nothing if the IsTwoDirectional returns False. |
| [ExtendFromFace](../DistanceFromFaceExtent/DistanceFromFaceExtent_ExtendFromFace.md) | Property that gets and sets whether the 'from face' should be extended to contain the extents of the feature. This property is not valid for every surface type. |
| [FromFace](../DistanceFromFaceExtent/DistanceFromFaceExtent_FromFace.md) | Read-write property that gets and sets the distance from face, this can be a Face or WorkPlane object. |
| [IsTwoDirectional](../DistanceFromFaceExtent/DistanceFromFaceExtent_IsTwoDirectional.md) | Read-write property that gets and sets the distance from face, this can be a Face or WorkPlane object. This is applicable when the Direction is not set to kSymmetricExtentDirection. |
| [MinimumSolution](../DistanceFromFaceExtent/DistanceFromFaceExtent_MinimumSolution.md) | Read-write property that gets and sets whether the feature starts from the nearest valid face when there are multiple options for valid starting faces. |
| [Parent](../DistanceFromFaceExtent/DistanceFromFaceExtent_Parent.md) | Property that returns the parent PartFeature of the definition. |
| [Type](../DistanceFromFaceExtent/DistanceFromFaceExtent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2018
