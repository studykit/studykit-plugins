# BorderDefinition.Sketch Property

Parent Object: [BorderDefinition](../BorderDefinition/BorderDefinition.md)

## Description

Property that returns the sketch associated with the border definition. The DrawingSketch returned by the Sketch property supports all query functionality but cannot be edited. To edit the contents of a border definition, use the Edit method. This creates a copy of the border definition's sketch for edit. The ExitEdit method of the BorderDefinition can then be used to save the edited sketch as the border definition's sketch.

## Syntax

BorderDefinition.**Sketch**() As [DrawingSketch](../DrawingSketch/DrawingSketch.md)

## Property Value

This is a read only property whose value is a [DrawingSketch](../DrawingSketch/DrawingSketch.md).

## Version

Introduced in version 5.3
