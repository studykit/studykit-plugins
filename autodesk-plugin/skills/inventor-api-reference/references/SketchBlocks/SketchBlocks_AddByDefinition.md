# SketchBlocks.AddByDefinition Method

Parent Object: [SketchBlocks](../SketchBlocks/SketchBlocks.md)

## Description

Method that creates a sketch block instance based on the \input definition. The newly created SketchBlock object is returned.

## Syntax

SketchBlocks.**AddByDefinition**( ***Definition*** As [SketchBlockDefinition](../SketchBlockDefinition/SketchBlockDefinition.md), ***Position*** As [Point2d](../Point2d/Point2d.md) ) As [SketchBlock](../SketchBlock/SketchBlock.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Definition | [SketchBlockDefinition](../SketchBlockDefinition/SketchBlockDefinition.md) | Input SketchBlockDefinition that specifies the definition to create the instance from. |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the placement point for the block in sketch space. The block is placed such that the insertion point of the sketch block definition coincides with this point. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create and insert a sketch block definition into a part sketch](../../sample-programs/SketchBlockDefinition_Sample.md) | This sample demonstrates inserting a sketch block into a part sketch. |

## Version

Introduced in version 2010
