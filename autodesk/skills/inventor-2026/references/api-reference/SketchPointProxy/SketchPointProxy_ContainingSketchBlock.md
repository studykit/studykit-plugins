# SketchPointProxy.ContainingSketchBlock Property

Parent Object: [SketchPointProxy](../SketchPointProxy/SketchPointProxy.md)

## Description

Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch.

## Syntax

SketchPointProxy.**ContainingSketchBlock**() As [SketchBlock](../SketchBlock/SketchBlock.md)

## Property Value

This is a read only property whose value is a [SketchBlock](../SketchBlock/SketchBlock.md).

## Version

Introduced in version 2010
