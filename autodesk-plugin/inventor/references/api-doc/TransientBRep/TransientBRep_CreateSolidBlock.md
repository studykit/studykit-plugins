# TransientBRep.CreateSolidBlock Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Method that creates a solid box.

## Remarks

The size is defined by the input Box object. The edges of the resulting solid box are aligned with axes of the model coordinate system.

## Syntax

TransientBRep.**CreateSolidBlock**( ***Box*** As [Box](../Box/Box.md) ) As [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Box | [Box](../Box/Box.md) | Input Box object that defines the size of the solid block. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create primitive BRep](../../sample-programs/TransientBRep_Sample.md) | This sample demonstrates the creation of primitive (solid) BRep. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |