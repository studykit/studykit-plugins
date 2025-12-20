# LoftFeatureProxy.StartFace Property

Parent Object: [LoftFeatureProxy](../LoftFeatureProxy/LoftFeatureProxy.md)

## Description

Property that returns the that acts as the cap of the first section of the loft. This property will return nothing in the cases where the loft does not have a starting face. These cases are when the loft sections are not closed or when the loft operation does not result in a solid.

## Syntax

LoftFeatureProxy.**StartFace**() As [Face](../Face/Face.md)

## Property Value

This is a read only property whose value is a [Face](../Face/Face.md).

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |