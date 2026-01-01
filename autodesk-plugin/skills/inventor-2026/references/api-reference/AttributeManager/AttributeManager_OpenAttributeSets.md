# AttributeManager.OpenAttributeSets Method

Parent Object: [AttributeManager](../AttributeManager/AttributeManager.md)

## Description

Finds the AttributeSet of the given name for each object in the object collection. If it does not find one, it creates a new AttributeSet. returns the in the same order as the object collection. Using this method is several times faster than accessing AttributeSets for each object individually. OpenAttributeSets works correctly even if the given collection has degenerate objects such as an edge for the apex of a cone. In such a case, OpenAttributeSets succeeds for all the valid objects, and returns NULL objects for the degenerate objects.

## Syntax

AttributeManager.**OpenAttributeSets**( ***Objects*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***AttributeSetName*** As String ) As [AttributeSetsEnumerator](../AttributeSetsEnumerator/AttributeSetsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Objects | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection. |
| AttributeSetName | String | Input String that specifies the name of the attribute set to find or create. |

## Version

Introduced in version 5.3
