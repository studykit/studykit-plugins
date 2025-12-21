# PunchNote Object

Derived from: [LeaderNote](../LeaderNote/LeaderNote.md) Object

## Description

The PunchNote object represents a punch note with an attached leader on a sheet and derives from the LeaderNote object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../PunchNote/PunchNote_Delete.md) | Method that deletes the DrawingNote. |
| [GetReferenceKey](../PunchNote/PunchNote_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PunchNote/PunchNote_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../PunchNote/PunchNote_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BackgroundColor](../PunchNote/PunchNote_BackgroundColor.md) | Gets/Sets the BackgroundColor associated with the LeaderNote. |
| [Color](../PunchNote/PunchNote_Color.md) | Gets/Sets color of the DrawingNote. |
| [DimensionStyle](../PunchNote/PunchNote_DimensionStyle.md) | Gets/Sets the DimensionStyle associated with the LeaderNote. |
| [FormattedPunchNote](../PunchNote/PunchNote_FormattedPunchNote.md) | Gets and sets the fully formatted string that defines the contents of the punch note. |
| [FormattedQuantityNote](../PunchNote/PunchNote_FormattedQuantityNote.md) | Gets and sets the fully formatted string that defines the quantity note. |
| [FormattedText](../PunchNote/PunchNote_FormattedText.md) | Gets/Sets formatted text of the DrawingNote. |
| [HideValue](../PunchNote/PunchNote_HideValue.md) | Gets and sets whether to display the punch note value in the note. |
| [HorizontalJustification](../PunchNote/PunchNote_HorizontalJustification.md) | Gets/Sets horizontal justification of the DrawingNote. |
| [Layer](../PunchNote/PunchNote_Layer.md) | Gets/Sets the layer used by the DrawingNote. |
| [Leader](../PunchNote/PunchNote_Leader.md) | Property that returns the Leader object. |
| [LineSpacing](../PunchNote/PunchNote_LineSpacing.md) | Gets/Sets the LineSpacing used by the DrawingNote. |
| [LineSpacingType](../PunchNote/PunchNote_LineSpacingType.md) | Gets/Sets the LineSpacingType used by the DrawingNote. |
| [Parent](../PunchNote/PunchNote_Parent.md) | Property that returns the parent sheet of the object. |
| [Position](../PunchNote/PunchNote_Position.md) | Gets/Sets the position of the DrawingNote on the sheet. |
| [PunchEdge](../PunchNote/PunchNote_PunchEdge.md) | Gets and sets the punch edge associated with the note. |
| [QuantityDefinition](../PunchNote/PunchNote_QuantityDefinition.md) | Gets and sets how the quantity value is set for the note. |
| [RangeBox](../PunchNote/PunchNote_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Retrieved](../PunchNote/PunchNote_Retrieved.md) | Indicates whether the drawing note was created as a result of retrieving it from the model. |
| [RetrievedFrom](../PunchNote/PunchNote_RetrievedFrom.md) | Returns the model annotation this drawing note was retrieved from. |
| [Rotation](../PunchNote/PunchNote_Rotation.md) | Gets/Sets the rotation of the LeaderNote. |
| [ShowTextBorder](../PunchNote/PunchNote_ShowTextBorder.md) | Gets/Sets whether to show the text border or not. |
| [StackedTextPosition](../PunchNote/PunchNote_StackedTextPosition.md) | Gets and sets the position (alignment) of the stacked text with respect to regular text. |
| [Text](../PunchNote/PunchNote_Text.md) | Gets/Sets text of the DrawingNote. |
| [Type](../PunchNote/PunchNote_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitAttributes](../PunchNote/PunchNote_UnitAttributes.md) | Get the unit attributes associated with the LeaderNote. |
| [UseBackgroundColor](../PunchNote/PunchNote_UseBackgroundColor.md) | Gets/Sets the UseBackgroundColor associated with the LeaderNote. |
| [UsePartUnits](../PunchNote/PunchNote_UsePartUnits.md) | Gets and sets whether to use model units or the units specified by dimension style. |
| [VerticalJustification](../PunchNote/PunchNote_VerticalJustification.md) | Gets/Sets vertical justification of the DrawingNote. |
| [WidthScale](../PunchNote/PunchNote_WidthScale.md) | Gets/Sets the width scale factor of the DrawingNote. |

## Accessed From

[PunchNotes.Add](../PunchNotes/PunchNotes_Add.md), [PunchNotes.Item](../PunchNotes/PunchNotes_Item.md)

## Version

Introduced in version 2010
