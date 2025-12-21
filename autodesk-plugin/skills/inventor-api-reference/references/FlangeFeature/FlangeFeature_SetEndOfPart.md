# FlangeFeature.SetEndOfPart Method

Parent Object: [FlangeFeature](../FlangeFeature/FlangeFeature.md)

## Description

Method that repositions the end-of-part marker relative to the object this method is called from.

## Syntax

FlangeFeature.**SetEndOfPart**( ***Before*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Before | Boolean | Input Boolean that indicates if the end of part marker should be immediately before or after this work feature. A value of True indicates before and False indicates after. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Edit width extent of an existing flange feature](../../sample-programs/FlangeDefinition_SetEdgeWidthExtent_Sample.md) | This sample demonstrates editing the width extent of an existing flange feature. This expects an existing sheet metal document that contains a flange feature that contains for physical flanges. It changes the type of width extent for each of the physical flanges. The result from the FlangeWidthsCreation sample can be used as the document to run this macro in. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |