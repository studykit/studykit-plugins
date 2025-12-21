# TitleBlockDefinition.Sketch Property

Parent Object: [TitleBlockDefinition](../TitleBlockDefinition/TitleBlockDefinition.md)

## Description

Property that returns the sketch associated with the title block definition. The DrawingSketch returned by the Sketch property supports all query functionality but cannot be edited. To edit the contents of a title block definition, use the Edit method. This creates a copy of the title block definition's sketch for edit. The ExitEdit method of the TitleBlockDefinition can then be used to save the edited sketch as the title block definition's sketch.

## Syntax

TitleBlockDefinition.**Sketch**() As [DrawingSketch](../DrawingSketch/DrawingSketch.md)

## Property Value

This is a read only property whose value is a [DrawingSketch](../DrawingSketch/DrawingSketch.md).

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |