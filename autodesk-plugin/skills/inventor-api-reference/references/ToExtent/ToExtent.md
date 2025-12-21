# ToExtent Object

Derived from: [PartFeatureExtent](../PartFeatureExtent/PartFeatureExtent.md) Object

## Description

The ToExtent object defines the feature extent type where the feature extent is defined up to a specified entity.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ToExtent/ToExtent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Direction](../ToExtent/ToExtent_Direction.md) | Gets and sets the direction of the feature. |
| [ExtendToFace](../ToExtent/ToExtent_ExtendToFace.md) | Property that gets and sets whether the plane defined by the 'to entity' should be extended to contain the extents of the profile. |
| [MinimumSolution](../ToExtent/ToExtent_MinimumSolution.md) | Gets and sets whether the feature terminates on the nearest valid face when there are multiple options for valid termination faces. |
| [Parent](../ToExtent/ToExtent_Parent.md) | Property that returns the parent PartFeature of the definition. |
| [ToEntity](../ToExtent/ToExtent_ToEntity.md) | Gets and sets the entity that defines the 'to' extents of the feature. |
| [Type](../ToExtent/ToExtent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Display feature information](../../sample-programs/DumpFeatureInfo_Sample.md) | Displays information about all of the extrude features in the active document. A part document must be active when this is run. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |