# GeometricConstraints.AddCoincident Method

Parent Object: [GeometricConstraints](../GeometricConstraints/GeometricConstraints.md)

## Description

Method that creates a new coincident constraint between two entities. One of the input entities must be a sketch point. The other entity can be a point or any other type of sketch entity.

## Remarks

Placing a coincident constraint between two points will not cause them to merge into a single point. Use the Merge method on the SketchPoint object to merge two points. This method will fail if the constraint overconstrains the sketch.

## Syntax

GeometricConstraints.**AddCoincident**( ***EntityOne*** As [SketchEntity](../SketchEntity/SketchEntity.md), ***EntityTwo*** As [SketchEntity](../SketchEntity/SketchEntity.md) ) As [CoincidentConstraint](../CoincidentConstraint/CoincidentConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. |
| EntityTwo | [SketchEntity](../SketchEntity/SketchEntity.md) | Input sketch entity. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |

## Version

Introduced in version 5
