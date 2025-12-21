# TextBoxes Object

## Description

The TextBoxes collection object provides access to all the existing objects in a drawing document and supports methods to create new TextBox objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddByRectangle](../TextBoxes/TextBoxes_AddByRectangle.md) | Method that creates a text box whose size is defined by the \input points that define opposing diagonals of the text box. |
| [AddFitted](../TextBoxes/TextBoxes_AddFitted.md) | Method that creates a text box positioned at the specified point. The size of the resulting text box is just large enough to contain the input text. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TextBoxes/TextBoxes_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../TextBoxes/TextBoxes_Count.md) | Property that returns the number of items in the collection. |
| [Item](../TextBoxes/TextBoxes_Item.md) | Returns a TextBox from the collection. |
| [Type](../TextBoxes/TextBoxes_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingSketch.TextBoxes](../DrawingSketch/DrawingSketch_TextBoxes.md), [PlanarSketch.TextBoxes](../PlanarSketch/PlanarSketch_TextBoxes.md), [PlanarSketchProxy.TextBoxes](../PlanarSketchProxy/PlanarSketchProxy_TextBoxes.md), [Sketch.TextBoxes](../Sketch/Sketch_TextBoxes.md), [SketchBlockDefinition.TextBoxes](../SketchBlockDefinition/SketchBlockDefinition_TextBoxes.md), [SketchBlockDefinitionProxy.TextBoxes](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_TextBoxes.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Sketch Text Add](../../sample-programs/TextBoxes_Sample.md) | This sample illustrates creating text in a sketch. |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |