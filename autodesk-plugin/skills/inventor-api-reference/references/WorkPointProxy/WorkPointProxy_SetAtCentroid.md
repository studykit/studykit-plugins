# WorkPointProxy.SetAtCentroid Method

Parent Object: [WorkPointProxy](../WorkPointProxy/WorkPointProxy.md)

## Description

Method that redefines a work point to be located at the centroid of the input entities.

## Syntax

WorkPointProxy.**SetAtCentroid**( ***Entities*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entities | Object | Input object that specifies the entities. This can be an Edge, an EdgeLoop object or an EdgeCollection containing one or more edges. If an EdgeCollection is input, the collection must contain connected edges. If isolated edges appear in the collection, the method will fail. |

## Version

Introduced in version 2008
