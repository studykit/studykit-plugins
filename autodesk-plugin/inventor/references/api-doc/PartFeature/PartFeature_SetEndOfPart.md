# PartFeature.SetEndOfPart Method

Parent Object: [PartFeature](../PartFeature/PartFeature.md)

## Description

Method that repositions the end-of-part marker relative to the object this method is called from.

## Remarks

The argument defines if the end-of-part marker will be positioned just before or just after the object. If the object is contained within another object and is not in the top level of the browser, the positioning of the marker will be relative to the top-level object the calling object is contained within. An example of this case is a sketch that has not been shared and has been consumed by a feature. Another example is a nested work feature.

## Syntax

PartFeature.**SetEndOfPart**( ***Before*** As Boolean )

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
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |