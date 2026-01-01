# SketchBlockProxy.SketchBlockPath Property

Parent Object: [SketchBlockProxy](../SketchBlockProxy/SketchBlockProxy.md)

## Description

Property that returns the path of sketch blocks at the leaf of which this sketch block is found. The enumerator returns a count of 0 if the block lives directly under a sketch. The path does not include this sketch block itself.

## Syntax

SketchBlockProxy.**SketchBlockPath**() As [SketchBlocksEnumerator](../SketchBlocksEnumerator/SketchBlocksEnumerator.md)

## Property Value

This is a read only property whose value is a [SketchBlocksEnumerator](../SketchBlocksEnumerator/SketchBlocksEnumerator.md).

## Version

Introduced in version 2010
