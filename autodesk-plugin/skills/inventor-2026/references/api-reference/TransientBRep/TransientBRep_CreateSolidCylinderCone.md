# TransientBRep.CreateSolidCylinderCone Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Method that create a solid cylinder or cone.

## Remarks

To create a circular cylinder or cone use the same values for the BottomMajorRadius and BottomMinorRadius arguments. To create an elliptical cylinder or cone use two different values. To create a cylinder use the same values for the BottomMajorRadius and TopMajorRadius. To create a cone use different values. When creating elliptical cones or cylinders the orientation of the major axis is defined by the MajorAxisPosition argument. . All values are in centimeters The SurfaceBody containing the cylinder or cone is returned.

## Syntax

TransientBRep.**CreateSolidCylinderCone**( ***BottomPoint*** As [Point](../Point/Point.md), ***TopPoint*** As [Point](../Point/Point.md), ***BottomMajorRadius*** As Double, ***BottomMinorRadius*** As Double, ***TopMajorRadius*** As Double, [***MajorAxisPosition***] As Variant ) As [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BottomPoint | [Point](../Point/Point.md) | Input Point that defines the center of the bottom of the cylinder or cone. |
| TopPoint | [Point](../Point/Point.md) | Input Point that defines the center of the top of the cylinder or cone. |
| BottomMajorRadius | Double | Input Double that defines the major axis radius at the bottom of an elliptical cylinder or cone or the radius at the bottom of a circular cylinder or cone. |
| BottomMinorRadius | Double | Input Double that define the minor axis radius at the bottom of an elliptical cylinder or cone. For a circular cylinder or cone this value should be the same at the BottomMajorRadius argument. |
| TopMajorRadius | Double | Input Double that specifies the radius at the top of the cylinder or cone. In the case of an elliptical cylinder or cone this is the radius of the major axis. |
| MajorAxisPosition | Variant | Optional input Point that specifies the orientation of the major axis. This is only needed in the case of an elliptical cylinder or cone. If not provided the major axis is determined based on the model coordinate system. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create primitive BRep](../../sample-programs/TransientBRep_Sample.md) | This sample demonstrates the creation of primitive (solid) BRep. |
| [Client graphics creation of 3D primitives](../../sample-programs/TransientBRep_CreateSolidCylinderCone_Sample.md) | This sample demonstrates the creation of 3D primitives (cylinder, cone, etc.) using client graphics. |

## Version

Introduced in version 2009
