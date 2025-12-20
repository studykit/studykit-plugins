# FromToExtent Object

Derived from: [PartFeatureExtent](../PartFeatureExtent/PartFeatureExtent.md) Object

## Description

The FromToExtent object provides access to the information that defines the extent for a feature using 'from' and 'to' faces to define the extent.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FromToExtent/FromToExtent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Direction](../FromToExtent/FromToExtent_Direction.md) | Gets and sets the direction of the feature. |
| [ExtendFromFace](../FromToExtent/FromToExtent_ExtendFromFace.md) | Property that gets and sets whether the 'from face' should be extended to contain the extents of the feature. This property is not valid for every surface type. |
| [ExtendToFace](../FromToExtent/FromToExtent_ExtendToFace.md) | Property that gets and sets whether the 'to face' should be extended to contain the extents of the feature. This property is not valid for every surface type. |
| [FromFace](../FromToExtent/FromToExtent_FromFace.md) | Property that gets and sets the face that defines the 'from' extents of the feature. |
| [MinimumSolution](../FromToExtent/FromToExtent_MinimumSolution.md) | Gets and sets whether the feature terminates on the nearest valid face when there are multiple options for valid termination faces. |
| [Parent](../FromToExtent/FromToExtent_Parent.md) | Property that returns the parent PartFeature of the definition. |
| [ToFace](../FromToExtent/FromToExtent_ToFace.md) | Property that gets and sets the face that defines the 'to' extents of the feature. |
| [Type](../FromToExtent/FromToExtent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

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