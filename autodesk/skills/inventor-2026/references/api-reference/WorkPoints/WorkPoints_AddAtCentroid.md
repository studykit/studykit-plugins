# WorkPoints.AddAtCentroid Method

Parent Object: [WorkPoints](../WorkPoints/WorkPoints.md)

## Description

Method that creates a new work point at the centroid of the input entities. This method is not currently supported when creating a work point within an assembly.

## Syntax

WorkPoints.**AddAtCentroid**( ***Entities*** As Object, [***Construction***] As Boolean ) As [WorkPoint](../WorkPoint/WorkPoint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entities | Object | Input object that specifies the entities. This can be an Edge, an EdgeLoop object or an EdgeCollection containing one or more edges. If an EdgeCollection is input, the collection must contain connected edges. If isolated edges appear in the collection, the method will fail. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work point as a construction point or not. The default is False, which indicates to create a standard work point. A construction work point is hidden from the user and is not displayed graphically or listed in the browser. |

## Version

Introduced in version 2008
