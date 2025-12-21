# SheetMetalFeatures.FlangeFeatures Property

Parent Object: [SheetMetalFeatures](../SheetMetalFeatures/SheetMetalFeatures.md)

## Description

Property that returns the FlangeFeatures collection object. This collection provides access to existing FlangeFeature objects.

## Syntax

SheetMetalFeatures.**FlangeFeatures**() As [FlangeFeatures](../FlangeFeatures/FlangeFeatures.md)

## Property Value

This is a read only property whose value is a [FlangeFeatures](../FlangeFeatures/FlangeFeatures.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Edit width extent of an existing flange feature](../../sample-programs/FlangeDefinition_SetEdgeWidthExtent_Sample.md) | This sample demonstrates editing the width extent of an existing flange feature. This expects an existing sheet metal document that contains a flange feature that contains for physical flanges. It changes the type of width extent for each of the physical flanges. The result from the FlangeWidthsCreation sample can be used as the document to run this macro in. |
| [Creating flange features](../../sample-programs/FlangeDefinition_SetOffsetWidthExtent_Sample.md) | Demonstrates creating flange features of various width extents. This creates a new document, creates a face feature and adds a flange feature on four edges. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |