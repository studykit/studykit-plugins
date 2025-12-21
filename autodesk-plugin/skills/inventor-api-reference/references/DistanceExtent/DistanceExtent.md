# DistanceExtent Object

Derived from: [PartFeatureExtent](../PartFeatureExtent/PartFeatureExtent.md) Object

## Description

The DistanceExtent object defines an extent given by a specified distance value.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DistanceExtent/DistanceExtent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Direction](../DistanceExtent/DistanceExtent_Direction.md) | Property that gets and sets the distance direction of the feature. Valid input is kPositiveExtentDirection, kNegativeExtentDirection, or kSymmetricExtentDirection. kPositiveExtentDirection defines the offset direction to be in the same direction as the normal of the sketch plane. |
| [Distance](../DistanceExtent/DistanceExtent_Distance.md) | Property that returns the parameter controlling the distance extent of the feature. |
| [Parent](../DistanceExtent/DistanceExtent_Parent.md) | Property that returns the parent PartFeature of the definition. |
| [Type](../DistanceExtent/DistanceExtent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Display feature information](../../sample-programs/DumpFeatureInfo_Sample.md) | Displays information about all of the extrude features in the active document. A part document must be active when this is run. |

## Version

Introduced in version 5
