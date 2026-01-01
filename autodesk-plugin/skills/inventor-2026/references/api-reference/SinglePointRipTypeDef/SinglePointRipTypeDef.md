# SinglePointRipTypeDef Object

## Description

The SinglePointRipTypeDef object defines the inputs unique to a single point rip feature.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [GapSide](../SinglePointRipTypeDef/SinglePointRipTypeDef_GapSide.md) | Gets and sets the value that indicates the position of the gap. |
| [GapSize](../SinglePointRipTypeDef/SinglePointRipTypeDef_GapSize.md) | Property that returns the parameter controlling the width of the gap. When creating a new rip feature and the RipDefinition object is not associated with an actual feature, this property will return Nothing. You can use the SetSinglePointRipType method of the RipDefinition to set this value in that case. When this object is obtained from an existing rip feature you can edit the rip feature by modifying the parameter this property returns. |
| [Parent](../SinglePointRipTypeDef/SinglePointRipTypeDef_Parent.md) | Property that returns the parent rip definition feature. |
| [Point](../SinglePointRipTypeDef/SinglePointRipTypeDef_Point.md) | Gets and sets the point that defines the location of the rip. |
| [Type](../SinglePointRipTypeDef/SinglePointRipTypeDef_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2011
