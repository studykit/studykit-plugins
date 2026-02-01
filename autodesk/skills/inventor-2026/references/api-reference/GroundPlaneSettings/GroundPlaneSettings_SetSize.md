# GroundPlaneSettings.SetSize Method

Parent Object: [GroundPlaneSettings](../GroundPlaneSettings/GroundPlaneSettings.md)

## Description

Method that sets the current size of the displayed graphics for the ground plane. The plane is functionally infinite but has a plane that is displayed to allow the user to visualize it. This method will fail if the AutoResize property is set to True.

## Syntax

GroundPlaneSettings.**SetSize**( ***PointOne*** As [Point](../Point/Point.md), ***PointTwo*** As [Point](../Point/Point.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PointOne | [Point](../Point/Point.md) | Point object that defines the first corner of the ground plane in model space. If the input point does not lie on the ground plane, the point is projected to the plane. |
| PointTwo | [Point](../Point/Point.md) | Point object that defines the diagonally opposite corner of the ground plane in model space. If the input point does not lie on the ground plane, the point is projected to the plane. |

## Version

Introduced in version 2011
