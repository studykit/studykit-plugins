# LoftDefinition.LoftRails Property

Parent Object: [LoftDefinition](../LoftDefinition/LoftDefinition.md)

## Description

Read-only property that specifies the rails for the loft. If the LoftDefinition.LoftType is not kRegularLoft or kLoftWithRails then set this property will raise error, you should follow below rules to set this property:

* If the LoftDefinition.LoftType returns kRegularLoft you can set this property directly.
* If the LoftDefinition.LoftType returns kLoftWithCenterline you need to clear the LoftDefinition.Centerline before setting this property.
* If the LoftDefinition.LoftType returns kLoftWithAreaGraphSections you need to clear the LoftDefinition.LoftSectionDimensions if any and LoftDefinition.Centerline before setting this property,

## Syntax

LoftDefinition.**LoftRails**() As [LoftRails](../LoftRails/LoftRails.md)

## Property Value

This is a read only property whose value is a [LoftRails](../LoftRails/LoftRails.md).

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |