# OffsetFromFaceExtent Object

## Description

The OffsetFromFaceExtent object provides access to the information that defines the extent for a feature that's extent is determined by extruding from a Face with offset. This is derived from the PartFeatureExtent object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AlternateSolutionDirection](../OffsetFromFaceExtent/OffsetFromFaceExtent_AlternateSolutionDirection.md) | Read-write property that gets and sets the alternate solution direction of the feature. Valid input is kPositiveExtentDirection or kNegativeExtentDirection. kPositiveExtentDirection defines the offset direction to be in the same direction as the normal of the. |
| [Application](../OffsetFromFaceExtent/OffsetFromFaceExtent_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Direction](../OffsetFromFaceExtent/OffsetFromFaceExtent_Direction.md) | Read-write property that gets and sets the distance direction of the feature. Valid input is kPositiveExtentDirection, kNegativeExtentDirection, or kSymmetricExtentDirection. kPositiveExtentDirection defines the offset direction to be in the same direction as. |
| [Distance](../OffsetFromFaceExtent/OffsetFromFaceExtent_Distance.md) | Read-only property that returns the parameter controlling the distance extent of the feature. |
| [DistanceTwo](../OffsetFromFaceExtent/OffsetFromFaceExtent_DistanceTwo.md) | Read-only property that returns the parameter controlling the distance extent of the feature in the other direction. This returns Nothing if the IsTwoDirectional returns False. |
| [ExtendFromFace](../OffsetFromFaceExtent/OffsetFromFaceExtent_ExtendFromFace.md) | Property that gets and sets whether the 'from face' should be extended to contain the extents of the feature. This property is not valid for every surface type. |
| [FromFace](../OffsetFromFaceExtent/OffsetFromFaceExtent_FromFace.md) | Read-write property that gets and sets the offset from face, this can be a Face or WorkPlane object. |
| [IsTwoDirectional](../OffsetFromFaceExtent/OffsetFromFaceExtent_IsTwoDirectional.md) | Read-write property that gets and sets the offset from face, this can be a Face or WorkPlane object. This is applicable when the Direction is not set to kSymmetricExtentDirection. |
| [MinimumSolution](../OffsetFromFaceExtent/OffsetFromFaceExtent_MinimumSolution.md) | Read-write property that gets and sets whether the feature starts from the nearest valid face when there are multiple options for valid starting faces. |
| [Parent](../OffsetFromFaceExtent/OffsetFromFaceExtent_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../OffsetFromFaceExtent/OffsetFromFaceExtent_Type.md) | Gets the constant that indicates the type of this object. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |