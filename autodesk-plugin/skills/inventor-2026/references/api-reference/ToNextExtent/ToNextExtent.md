# ToNextExtent Object

Derived from: [PartFeatureExtent](../PartFeatureExtent/PartFeatureExtent.md) Object

## Description

The ToNextExtent object provides access to the information that defines the extent for a feature that's extent is determined by extruding up to the closest set of faces that the feature completely intersects.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ToNextExtent/ToNextExtent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Direction](../ToNextExtent/ToNextExtent_Direction.md) | Property that gets and sets the direction of the feature. Valid \input is kPositiveExtentDirection or kNegativeExtentDirection. kPositiveExtentDirection defines the extrusion direction to be in the same direction as the normal of the sketch plane. |
| [Parent](../ToNextExtent/ToNextExtent_Parent.md) | Property that returns the parent PartFeature of the definition. |
| [Terminator](../ToNextExtent/ToNextExtent_Terminator.md) | Gets and sets the SurfaceBody that specifies the solid or the surface on which to terminate the revolution. |
| [Type](../ToNextExtent/ToNextExtent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Display feature information](../../sample-programs/DumpFeatureInfo_Sample.md) | Displays information about all of the extrude features in the active document. A part document must be active when this is run. |

## Version

Introduced in version 5
