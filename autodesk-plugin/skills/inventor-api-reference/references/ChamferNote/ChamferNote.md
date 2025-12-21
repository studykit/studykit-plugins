# ChamferNote Object

Derived from: [LeaderNote](../LeaderNote/LeaderNote.md) Object

## Description

The ChamferNote object represents a chamfer note with an attached leader on a sheet and derives from the LeaderNote object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ChamferNote/ChamferNote_Delete.md) | Method that deletes the DrawingNote. |
| [GetReferenceKey](../ChamferNote/ChamferNote_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ChamferNote/ChamferNote_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ChamferNote/ChamferNote_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BackgroundColor](../ChamferNote/ChamferNote_BackgroundColor.md) | Gets/Sets the BackgroundColor associated with the LeaderNote. |
| [ChamferEdgeOne](../ChamferNote/ChamferNote_ChamferEdgeOne.md) | Property that returns that first chamfer edge. This can either be a linear DrawingCurve object or a SketchLine object from a sheet sketch. |
| [ChamferEdgeTwo](../ChamferNote/ChamferNote_ChamferEdgeTwo.md) | Property that returns that second chamfer edge. This can either be a linear DrawingCurve object or a SketchLine object from a sheet sketch. |
| [Color](../ChamferNote/ChamferNote_Color.md) | Gets/Sets color of the DrawingNote. |
| [DimensionStyle](../ChamferNote/ChamferNote_DimensionStyle.md) | Gets/Sets the DimensionStyle associated with the LeaderNote. |
| [FormattedChamferNote](../ChamferNote/ChamferNote_FormattedChamferNote.md) | Gets and sets the fully formatted string that defines the contents of the chamfer note. |
| [FormattedText](../ChamferNote/ChamferNote_FormattedText.md) | Gets/Sets formatted text of the DrawingNote. |
| [HideValue](../ChamferNote/ChamferNote_HideValue.md) | Gets and sets whether to display the chamfer note value in the note. |
| [HorizontalJustification](../ChamferNote/ChamferNote_HorizontalJustification.md) | Gets/Sets horizontal justification of the DrawingNote. |
| [Layer](../ChamferNote/ChamferNote_Layer.md) | Gets/Sets the layer used by the DrawingNote. |
| [Leader](../ChamferNote/ChamferNote_Leader.md) | Property that returns the Leader object. |
| [LineSpacing](../ChamferNote/ChamferNote_LineSpacing.md) | Gets/Sets the LineSpacing used by the DrawingNote. |
| [LineSpacingType](../ChamferNote/ChamferNote_LineSpacingType.md) | Gets/Sets the LineSpacingType used by the DrawingNote. |
| [Parent](../ChamferNote/ChamferNote_Parent.md) | Property that returns the parent sheet of the object. |
| [Position](../ChamferNote/ChamferNote_Position.md) | Gets/Sets the position of the DrawingNote on the sheet. |
| [RangeBox](../ChamferNote/ChamferNote_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Retrieved](../ChamferNote/ChamferNote_Retrieved.md) | Indicates whether the drawing note was created as a result of retrieving it from the model. |
| [RetrievedFrom](../ChamferNote/ChamferNote_RetrievedFrom.md) | Returns the model annotation this drawing note was retrieved from. |
| [Rotation](../ChamferNote/ChamferNote_Rotation.md) | Gets/Sets the rotation of the LeaderNote. |
| [ShowTextBorder](../ChamferNote/ChamferNote_ShowTextBorder.md) | Gets/Sets whether to show the text border or not. |
| [StackedTextPosition](../ChamferNote/ChamferNote_StackedTextPosition.md) | Gets and sets the position (alignment) of the stacked text with respect to regular text. |
| [Text](../ChamferNote/ChamferNote_Text.md) | Gets/Sets text of the DrawingNote. |
| [Type](../ChamferNote/ChamferNote_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitAttributes](../ChamferNote/ChamferNote_UnitAttributes.md) | Get the unit attributes associated with the LeaderNote. |
| [UseBackgroundColor](../ChamferNote/ChamferNote_UseBackgroundColor.md) | Gets/Sets the UseBackgroundColor associated with the LeaderNote. |
| [VerticalJustification](../ChamferNote/ChamferNote_VerticalJustification.md) | Gets/Sets vertical justification of the DrawingNote. |
| [WidthScale](../ChamferNote/ChamferNote_WidthScale.md) | Gets/Sets the width scale factor of the DrawingNote. |

## Accessed From

[ChamferNotes.Add](../ChamferNotes/ChamferNotes_Add.md), [ChamferNotes.Item](../ChamferNotes/ChamferNotes_Item.md)

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |