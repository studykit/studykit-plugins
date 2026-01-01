# Sheet.ChangeLayer Method

Parent Object: [Sheet](../Sheet/Sheet.md)

## Description

Method that changes the associated layer for all the input objects.

## Syntax

Sheet.**ChangeLayer**( ***Objects*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Layer*** As [Layer](../Layer/Layer.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Objects | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing the objects to change the layer of. All the objects should belong to the parent Sheet. The collection can contain any drawing object that has a layer associated with it. |
| Layer | [Layer](../Layer/Layer.md) | Input Layer object that specifies the new layer to which the objects should be moved to. |

## Version

Introduced in version 2011
