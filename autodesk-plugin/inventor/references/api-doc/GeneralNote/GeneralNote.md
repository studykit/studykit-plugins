# GeneralNote Object

Derived from: [DrawingNote](../DrawingNote/DrawingNote.md) Object

## Description

The GeneralNote object represents a general note on a sheet and derives from the DrawingNote object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../GeneralNote/GeneralNote_Delete.md) | Method that deletes the DrawingNote. |
| [GetReferenceKey](../GeneralNote/GeneralNote_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../GeneralNote/GeneralNote_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../GeneralNote/GeneralNote_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BackgroundColor](../GeneralNote/GeneralNote_BackgroundColor.md) | Gets/Sets the BackgroundColor associated with the GeneralNote. |
| [Color](../GeneralNote/GeneralNote_Color.md) | Gets/Sets color of the DrawingNote. |
| [Fitted](../GeneralNote/GeneralNote_Fitted.md) | Property that returns whether the note remains tightly fitted to the text within the box. |
| [FittedTextHeight](../GeneralNote/GeneralNote_FittedTextHeight.md) | Property that returns the actual height of the text within the note. This does not necessarily represent the current height of the note, but only the text within the note. If the Fitted property is True then this value is the same as the height of the note. |
| [FittedTextWidth](../GeneralNote/GeneralNote_FittedTextWidth.md) | Property that returns the actual width of the text within the note. This does not necessarily represent the current width of the note, but only the text within the note. If the Fitted property is True then this value is the same as the width of the note. |
| [FormattedText](../GeneralNote/GeneralNote_FormattedText.md) | Gets/Sets formatted text of the DrawingNote. |
| [Height](../GeneralNote/GeneralNote_Height.md) | Gets/Sets the height of the GeneralNote. |
| [HorizontalJustification](../GeneralNote/GeneralNote_HorizontalJustification.md) | Gets/Sets horizontal justification of the DrawingNote. |
| [Layer](../GeneralNote/GeneralNote_Layer.md) | Gets/Sets the layer used by the DrawingNote. |
| [LineSpacing](../GeneralNote/GeneralNote_LineSpacing.md) | Gets/Sets the LineSpacing used by the DrawingNote. |
| [LineSpacingType](../GeneralNote/GeneralNote_LineSpacingType.md) | Gets/Sets the LineSpacingType used by the DrawingNote. |
| [Parent](../GeneralNote/GeneralNote_Parent.md) | Property that returns the parent sheet of the object. |
| [Position](../GeneralNote/GeneralNote_Position.md) | Gets/Sets the position of the DrawingNote on the sheet. |
| [RangeBox](../GeneralNote/GeneralNote_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Retrieved](../GeneralNote/GeneralNote_Retrieved.md) | Indicates whether the drawing note was created as a result of retrieving it from the model. |
| [RetrievedFrom](../GeneralNote/GeneralNote_RetrievedFrom.md) | Returns the model annotation this drawing note was retrieved from. |
| [Rotation](../GeneralNote/GeneralNote_Rotation.md) | Gets/Sets the rotation of the GeneralNote. |
| [ShowTextBorder](../GeneralNote/GeneralNote_ShowTextBorder.md) | Gets/Sets whether to show the text border or not. |
| [StackedTextPosition](../GeneralNote/GeneralNote_StackedTextPosition.md) | Gets and sets the position (alignment) of the stacked text with respect to regular text. |
| [Text](../GeneralNote/GeneralNote_Text.md) | Gets/Sets text of the DrawingNote. |
| [TextStyle](../GeneralNote/GeneralNote_TextStyle.md) | Gets/Sets the TextStyle of the GeneralNote. |
| [Type](../GeneralNote/GeneralNote_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitAttributes](../GeneralNote/GeneralNote_UnitAttributes.md) | Get the unit attributes associated with the GeneralNote. |
| [UseBackgroundColor](../GeneralNote/GeneralNote_UseBackgroundColor.md) | Gets/Sets the UseBackgroundColor associated with the GeneralNote. |
| [VerticalJustification](../GeneralNote/GeneralNote_VerticalJustification.md) | Gets/Sets vertical justification of the DrawingNote. |
| [Width](../GeneralNote/GeneralNote_Width.md) | Gets/Sets the width of the GeneralNote. |
| [WidthScale](../GeneralNote/GeneralNote_WidthScale.md) | Gets/Sets the width scale factor of the DrawingNote. |

## Accessed From

[GeneralNotes.AddByRectangle](../GeneralNotes/GeneralNotes_AddByRectangle.md), [GeneralNotes.AddFitted](../GeneralNotes/GeneralNotes_AddFitted.md), [GeneralNotes.Item](../GeneralNotes/GeneralNotes_Item.md)

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |