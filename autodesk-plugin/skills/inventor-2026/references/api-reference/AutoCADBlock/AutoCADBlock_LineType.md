# AutoCADBlock.LineType Property

Parent Object: [AutoCADBlock](../AutoCADBlock/AutoCADBlock.md)

## Description

Read-write property that gets and sets the line type override for the block. Setting the property to kDefaultLineType restores the block to the line type defined by the layer on which this block resides. If the property returns kCustomLineType, the GetCustom.

## Syntax

AutoCADBlock.**LineType**() As [LineTypeEnum](../LineTypeEnum.md)

## Property Value

This is a read/write property whose value is a [LineTypeEnum](../LineTypeEnum.md).

## Version

Introduced in version 2011
