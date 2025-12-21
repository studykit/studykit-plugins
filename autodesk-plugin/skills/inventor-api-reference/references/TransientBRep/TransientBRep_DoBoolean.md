# TransientBRep.DoBoolean Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Method that performs the specified Boolean operation between the blank and tool bodies.

## Remarks

If successful, the blank body is modified as a result of the Boolean operation. Because of this the BlankBody must always be a transient SurfaceBody. The toolbody is not modified. This is analogous to a machining operation where you have the blank that is being machined and the tool that removes material.

## Syntax

TransientBRep.**DoBoolean**( ***BlankBody*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***ToolBody*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***BooleanType*** As [BooleanTypeEnum](../BooleanTypeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BlankBody | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input/Output SurfaceBody that will be modified as a result. |
| ToolBody | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody that is used to operate on the blank body. |
| BooleanType | [BooleanTypeEnum](../BooleanTypeEnum.md) | Input BooleanTypeEnum that specifies the type of Boolean operation to perform. Valid values are kBooleanTypeDifference, kBooleanTypeUnion, and kBooleanTypeIntersect. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create primitive BRep](../../sample-programs/TransientBRep_Sample.md) | This sample demonstrates the creation of primitive (solid) BRep. |
| [Client graphics creation of 3D primitives](../../sample-programs/TransientBRep_CreateSolidCylinderCone_Sample.md) | This sample demonstrates the creation of 3D primitives (cylinder, cone, etc.) using client graphics. |

## Version

Introduced in version 2009
