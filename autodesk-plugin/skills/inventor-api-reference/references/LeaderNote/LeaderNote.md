# LeaderNote Object

Derived from: [DrawingNote](../DrawingNote/DrawingNote.md) Object

## Description

The LeaderNote object represents a note with an attached leader on a sheet and derives from the DrawingNote object. The properties and methods listed below are in addition to those supported by the DrawingNote object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../LeaderNote/LeaderNote_Delete.md) | Method that deletes the DrawingNote. |
| [GetReferenceKey](../LeaderNote/LeaderNote_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../LeaderNote/LeaderNote_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../LeaderNote/LeaderNote_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BackgroundColor](../LeaderNote/LeaderNote_BackgroundColor.md) | Gets/Sets the BackgroundColor associated with the LeaderNote. |
| [Color](../LeaderNote/LeaderNote_Color.md) | Gets/Sets color of the DrawingNote. |
| [DimensionStyle](../LeaderNote/LeaderNote_DimensionStyle.md) | Gets/Sets the DimensionStyle associated with the LeaderNote. |
| [FormattedText](../LeaderNote/LeaderNote_FormattedText.md) | Gets/Sets formatted text of the DrawingNote. |
| [HorizontalJustification](../LeaderNote/LeaderNote_HorizontalJustification.md) | Gets/Sets horizontal justification of the DrawingNote. |
| [Layer](../LeaderNote/LeaderNote_Layer.md) | Gets/Sets the layer used by the DrawingNote. |
| [Leader](../LeaderNote/LeaderNote_Leader.md) | Property that returns the Leader object. |
| [LineSpacing](../LeaderNote/LeaderNote_LineSpacing.md) | Gets/Sets the LineSpacing used by the DrawingNote. |
| [LineSpacingType](../LeaderNote/LeaderNote_LineSpacingType.md) | Gets/Sets the LineSpacingType used by the DrawingNote. |
| [Parent](../LeaderNote/LeaderNote_Parent.md) | Property that returns the parent sheet of the object. |
| [Position](../LeaderNote/LeaderNote_Position.md) | Gets/Sets the position of the DrawingNote on the sheet. |
| [RangeBox](../LeaderNote/LeaderNote_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Retrieved](../LeaderNote/LeaderNote_Retrieved.md) | Indicates whether the drawing note was created as a result of retrieving it from the model. |
| [RetrievedFrom](../LeaderNote/LeaderNote_RetrievedFrom.md) | Returns the model annotation this drawing note was retrieved from. |
| [Rotation](../LeaderNote/LeaderNote_Rotation.md) | Gets/Sets the rotation of the LeaderNote. |
| [ShowTextBorder](../LeaderNote/LeaderNote_ShowTextBorder.md) | Gets/Sets whether to show the text border or not. |
| [StackedTextPosition](../LeaderNote/LeaderNote_StackedTextPosition.md) | Gets and sets the position (alignment) of the stacked text with respect to regular text. |
| [Text](../LeaderNote/LeaderNote_Text.md) | Gets/Sets text of the DrawingNote. |
| [Type](../LeaderNote/LeaderNote_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitAttributes](../LeaderNote/LeaderNote_UnitAttributes.md) | Get the unit attributes associated with the LeaderNote. |
| [UseBackgroundColor](../LeaderNote/LeaderNote_UseBackgroundColor.md) | Gets/Sets the UseBackgroundColor associated with the LeaderNote. |
| [VerticalJustification](../LeaderNote/LeaderNote_VerticalJustification.md) | Gets/Sets vertical justification of the DrawingNote. |
| [WidthScale](../LeaderNote/LeaderNote_WidthScale.md) | Gets/Sets the width scale factor of the DrawingNote. |

## Accessed From

[LeaderNotes.Add](../LeaderNotes/LeaderNotes_Add.md), [LeaderNotes.Item](../LeaderNotes/LeaderNotes_Item.md)

## Derived Classes

[BendNote](../BendNote/BendNote.md), [ChamferNote](../ChamferNote/ChamferNote.md), [PunchNote](../PunchNote/PunchNote.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add new leader note](../../sample-programs/LeaderNode_Sample.md) | This sample illustrates creating leader text on a sheet. |

## Version

Introduced in version 10
