# PointGraphics.SetCustomImage Method

Parent Object: [PointGraphics](../PointGraphics/PointGraphics.md)

## Description

Method that sets the custom image to use for this PointGraphics object. This is cause the PointerRenderStyleProperty to return kCustomImagePointStyle. You can remove the custom image by setting the PointRenderStyle to one of the predefined point types.

## Syntax

PointGraphics.**SetCustomImage**( ***GraphicsImageSet*** As [GraphicsImageSet](../GraphicsImageSet/GraphicsImageSet.md), ***GraphicsImageIndex*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GraphicsImageSet | [GraphicsImageSet](../GraphicsImageSet/GraphicsImageSet.md) | Input GraphicsImageSet to assign to this PointGraphics object. |
| GraphicsImageIndex | Long | Input Long that indicates which image in the GraphicsImageSet to use for this PointGraphics object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics - image in point graphics](../../sample-programs/PointGraphics_SetCustomImage_Sample.md) | The following sample demonstrates creation of point client graphics with a custom image. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |