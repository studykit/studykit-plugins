# BalloonTips.Item Property

Parent Object: [BalloonTips](../BalloonTips/BalloonTips.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

BalloonTips.**Item**( ***Index*** As Variant ) As [BalloonTip](../BalloonTip/BalloonTip.md)

## Property Value

This is a read only property whose value is a [BalloonTip](../BalloonTip/BalloonTip.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the BalloonTip to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the BalloonTip internal name. If an out of range index or a name of a non-existent BalloonTip is provided, an error will occur. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |