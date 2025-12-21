# FlangeFeatures.Item Property

Parent Object: [FlangeFeatures](../FlangeFeatures/FlangeFeatures.md)

## Description

Returns the specified FlangeFeature object from the collection. This is the default property of the FlangeFeatures collection object.

## Syntax

FlangeFeatures.**Item**( ***Index*** As Variant ) As [FlangeFeature](../FlangeFeature/FlangeFeature.md)

## Property Value

This is a read only property whose value is a [FlangeFeature](../FlangeFeature/FlangeFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the index of the to return. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Edit width extent of an existing flange feature](../../sample-programs/FlangeDefinition_SetEdgeWidthExtent_Sample.md) | This sample demonstrates editing the width extent of an existing flange feature. This expects an existing sheet metal document that contains a flange feature that contains for physical flanges. It changes the type of width extent for each of the physical flanges. The result from the FlangeWidthsCreation sample can be used as the document to run this macro in. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |