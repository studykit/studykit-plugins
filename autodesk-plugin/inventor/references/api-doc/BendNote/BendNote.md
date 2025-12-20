# BendNote Object

Derived from: [LeaderNote](../LeaderNote/LeaderNote.md) Object

## Description

The BendNote object represents a bend note on a sheet and derives from the LeaderNote object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../BendNote/BendNote_Delete.md) | Method that deletes the DrawingNote. |
| [GetReferenceKey](../BendNote/BendNote_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BendNote/BendNote_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../BendNote/BendNote_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BackgroundColor](../BendNote/BendNote_BackgroundColor.md) | Gets/Sets the BackgroundColor associated with the LeaderNote. |
| [BendEdge](../BendNote/BendNote_BendEdge.md) | Property that returns the bend edge associated with the note. |
| [Color](../BendNote/BendNote_Color.md) | Gets/Sets color of the DrawingNote. |
| [DimensionStyle](../BendNote/BendNote_DimensionStyle.md) | Gets/Sets the DimensionStyle associated with the LeaderNote. |
| [FormattedBendNote](../BendNote/BendNote_FormattedBendNote.md) | Gets and sets the fully formatted string that defines the contents of the bend note. |
| [FormattedText](../BendNote/BendNote_FormattedText.md) | Gets/Sets formatted text of the DrawingNote. |
| [HideValue](../BendNote/BendNote_HideValue.md) | Gets and sets whether to display the bend note value in the note. |
| [HorizontalJustification](../BendNote/BendNote_HorizontalJustification.md) | Gets/Sets horizontal justification of the DrawingNote. |
| [Layer](../BendNote/BendNote_Layer.md) | Gets/Sets the layer used by the DrawingNote. |
| [Leader](../BendNote/BendNote_Leader.md) | Property that returns the Leader object. |
| [LineSpacing](../BendNote/BendNote_LineSpacing.md) | Gets/Sets the LineSpacing used by the DrawingNote. |
| [LineSpacingType](../BendNote/BendNote_LineSpacingType.md) | Gets/Sets the LineSpacingType used by the DrawingNote. |
| [Parent](../BendNote/BendNote_Parent.md) | Property that returns the parent sheet of the object. |
| [Position](../BendNote/BendNote_Position.md) | Gets/Sets the position of the DrawingNote on the sheet. |
| [RangeBox](../BendNote/BendNote_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Retrieved](../BendNote/BendNote_Retrieved.md) | Indicates whether the drawing note was created as a result of retrieving it from the model. |
| [RetrievedFrom](../BendNote/BendNote_RetrievedFrom.md) | Returns the model annotation this drawing note was retrieved from. |
| [Rotation](../BendNote/BendNote_Rotation.md) | Gets/Sets the rotation of the LeaderNote. |
| [ShowTextBorder](../BendNote/BendNote_ShowTextBorder.md) | Gets/Sets whether to show the text border or not. |
| [StackedTextPosition](../BendNote/BendNote_StackedTextPosition.md) | Gets and sets the position (alignment) of the stacked text with respect to regular text. |
| [Text](../BendNote/BendNote_Text.md) | Gets/Sets text of the DrawingNote. |
| [Type](../BendNote/BendNote_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitAttributes](../BendNote/BendNote_UnitAttributes.md) | Get the unit attributes associated with the LeaderNote. |
| [UseBackgroundColor](../BendNote/BendNote_UseBackgroundColor.md) | Gets/Sets the UseBackgroundColor associated with the LeaderNote. |
| [UsePartUnits](../BendNote/BendNote_UsePartUnits.md) | Gets and sets whether to use model units or the units specified by dimension style. |
| [VerticalJustification](../BendNote/BendNote_VerticalJustification.md) | Gets/Sets vertical justification of the DrawingNote. |
| [WidthScale](../BendNote/BendNote_WidthScale.md) | Gets/Sets the width scale factor of the DrawingNote. |

## Accessed From

[BendNotes.Add](../BendNotes/BendNotes_Add.md), [BendNotes.Item](../BendNotes/BendNotes_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create bend note](../../sample-programs/BendNotes_Add_Sample.md) | This sample demonstrates the creation of a bend note on the drawing view of a flat pattern. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |