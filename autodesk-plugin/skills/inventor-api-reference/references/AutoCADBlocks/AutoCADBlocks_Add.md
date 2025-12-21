# AutoCADBlocks.Add Method

Parent Object: [AutoCADBlocks](../AutoCADBlocks/AutoCADBlocks.md)

## Description

Method that places an AutoCAD block onto the sheet.

## Syntax

AutoCADBlocks.**Add**( ***Definition*** As [AutoCADBlockDefinition](../AutoCADBlockDefinition/AutoCADBlockDefinition.md), ***Position*** As [Point2d](../Point2d/Point2d.md), [***Rotation***] As Double, [***Scale***] As Double, [***PromptStrings***] As Variant, [***Static***] As Boolean ) As [AutoCADBlock](../AutoCADBlock/AutoCADBlock.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Definition | [AutoCADBlockDefinition](../AutoCADBlockDefinition/AutoCADBlockDefinition.md) | AutoCADBlockDefinition object to use for placing the block. |
| Position | [Point2d](../Point2d/Point2d.md) | Point2d that specifies the location on the sheet to place the block instance. |
| Rotation | Double | Optional input double that specifies the rotation angle in radians. |
| Scale | Double | Optional input double that specifies the scale.   This is an optional argument whose default value is 1.0. |
| PromptStrings | Variant | Optional input array of strings to use as input for prompted text fields that my be present in the block definition.   This is an optional argument whose default value is null. |
| Static | Boolean | Optional input Boolean that indicates whether to show the scale and rotation grip points on the block. If True, the grip points are disabled. If not specified, a value of False is used.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [AutoCAD block insertion](../../sample-programs/AutoCADBlocks_Add_Sample.md) | Demonstrates inserting an AutoCAD block. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |