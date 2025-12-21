# SketchBlocks.Add Method

Parent Object: [SketchBlocks](../SketchBlocks/SketchBlocks.md)

## Description

Method that creates a sketch block instance using existing sketch objects. A sketch block definition is implicitly created. The newly created SketchBlock object is returned.

## Syntax

SketchBlocks.**Add**( ***SketchObjects*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***Name***] As String, [***InsertionPoint***] As Variant ) As [SketchBlock](../SketchBlock/SketchBlock.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchObjects | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that specifies the sketch entities to create the sketch block from. The collection can contain SketchEntity, (other) SketchBlock, SketchImage and TextBox objects. |
| Name | String | Optional input String that specifies a name for the sketch block definition. If not provided, the name is automatically generated. |
| InsertionPoint | Variant | Optional input Point2d object that specifies the insertion point for the sketch block. The insertion sketch point is created in space and no constraints are created on the insertion point. The insertion point can be retrieved using SketchBlockDefinition.InsertionPoint property and constraints can be added to it. If not specified, a default insertion point is chosen.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2010
