# ComponentOccurrenceProxy.CreateGeometryProxy Method

Parent Object: [ComponentOccurrenceProxy](../ComponentOccurrenceProxy/ComponentOccurrenceProxy.md)

## Description

Method that creates a proxy object for input object. A proxy object represents another object within the assembly space. Queries made on the proxy object are returned with respect to the assembly space, not the space the real geometry exists in.

## Syntax

ComponentOccurrenceProxy.**CreateGeometryProxy**( ***Geometry*** As Object, ***Result*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Geometry | Object | Input entity to create a proxy for. This entity must exist under the tree of this occurrence. |
| Result | Object | Output proxy object created. |

## Version

Introduced in version 4
