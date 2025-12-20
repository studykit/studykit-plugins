# SketchedSymbolDefinition.Sketch Property

Parent Object: [SketchedSymbolDefinition](../SketchedSymbolDefinition/SketchedSymbolDefinition.md)

## Description

Property that returns the sketch associated with the sketched symbol definition. The DrawingSketch returned by the Sketch property supports all query functionality but cannot be edited. To edit the contents of a sketched symbol definition, use the Edit method. This creates a copy of the sketched symbol definition's sketch for edit. The ExitEdit method of the SketchedSymbolDefinition can then be used to save the edited sketch as the sketched symbol definition's sketch.

## Syntax

SketchedSymbolDefinition.**Sketch**() As [DrawingSketch](../DrawingSketch/DrawingSketch.md)

## Property Value

This is a read only property whose value is a [DrawingSketch](../DrawingSketch/DrawingSketch.md).

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |