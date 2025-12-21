# ReferenceComponent.SetEndOfPart Method

Parent Object: [ReferenceComponent](../ReferenceComponent/ReferenceComponent.md)

## Description

Method that repositions the end-of-part marker relative to the object this method is called from.

## Remarks

The argument defines if the end-of-part marker will be positioned just before or just after the object. If the object is contained within another object and is not in the top level of the browser, the positioning of the marker will be relative to the top-level object the calling object is contained within. An example of this case is a sketch that has not been shared and has been consumed by a feature. Another example is a nested work feature.

## Syntax

ReferenceComponent.**SetEndOfPart**( ***Before*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Before | Boolean | Input Boolean that indicates if the end of part marker should be immediately before or after this reference component. A value of True indicates before and False indicates after. |

## Version

Introduced in version 7
