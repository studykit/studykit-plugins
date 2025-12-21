# SheetMetalComponentDefinition.SetEndOfPartToTopOrBottom Method

Parent Object: [SheetMetalComponentDefinition](../SheetMetalComponentDefinition/SheetMetalComponentDefinition.md)

## Description

Method that positions the end-of-part marker at the top or bottom of the browser.

## Syntax

SheetMetalComponentDefinition.**SetEndOfPartToTopOrBottom**( ***SetToTop*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SetToTop | Boolean | Input Boolean that specifies whether the end-of-part marker is to be moved to the top or the bottom of the browser. If True, the marker is moved to the top of the browser, just below the Origin folder. If False, it is moved to the bottom of the browser, just below the last item in the browser. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Edit width extent of an existing flange feature](../../sample-programs/FlangeDefinition_SetEdgeWidthExtent_Sample.md) | This sample demonstrates editing the width extent of an existing flange feature. This expects an existing sheet metal document that contains a flange feature that contains for physical flanges. It changes the type of width extent for each of the physical flanges. The result from the FlangeWidthsCreation sample can be used as the document to run this macro in. |

## Version

Introduced in version 7
