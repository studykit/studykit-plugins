# WorkPoint.SetAtCentroid Method

Parent Object: [WorkPoint](../WorkPoint/WorkPoint.md)

## Description

Method that redefines a work point to be located at the centroid of the input entities.

## Remarks

This method is not valid when the work point exists in an Assembly component definition.

## Syntax

WorkPoint.**SetAtCentroid**( ***Entities*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entities | Object | Input object that specifies the entities. This can be an Edge, an EdgeLoop object or an EdgeCollection containing one or more edges. If an EdgeCollection is input, the collection must contain connected edges. If isolated edges appear in the collection, the method will fail. |

## Version

Introduced in version 2008
