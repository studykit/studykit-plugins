# TextBox Object

## Description

The TextBox object represents text on a sheet or sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToGeometry](../TextBox/TextBox_ConvertToGeometry.md) | Method that converts the text box to sketch geometries. |
| [Delete](../TextBox/TextBox_Delete.md) | Method that deletes the text box. |
| [GetFacetsInfo](../TextBox/TextBox_GetFacetsInfo.md) | Returns facets’ coordinates of the text box. |
| [GetReferenceKey](../TextBox/TextBox_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TextBox/TextBox_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TextBox/TextBox_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BackgroundColor](../TextBox/TextBox_BackgroundColor.md) | Gets/Sets the BackgroundColor associated with the TextBox. |
| [BoundaryGeometry](../TextBox/TextBox_BoundaryGeometry.md) | Property that returns the four construction sketch lines that form the boundary of the text box. |
| [Color](../TextBox/TextBox_Color.md) | Gets/Sets the color of the text box. |
| [ContainingSketchBlock](../TextBox/TextBox_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [Fitted](../TextBox/TextBox_Fitted.md) | Property that returns if the text box remains tightly fitted to the text within the box. True indicates the text box just encloses the text. |
| [FittedTextHeight](../TextBox/TextBox_FittedTextHeight.md) | Property that returns the actual height of the text within the text box. This does not necessarily represent the current height of the text box, but only the text within the box. If the Fitted property is True then this value is the same as the height of the text box. |
| [FittedTextWidth](../TextBox/TextBox_FittedTextWidth.md) | Property that returns the actual width of the text within the text box. This does not necessarily represent the current width of the text box, but only the text within the box. If the Fitted property is True then this value is the same as the width of the text box. |
| [FormattedText](../TextBox/TextBox_FormattedText.md) | Gets and sets the fully formatted string that defines the contents of the text box. |
| [Height](../TextBox/TextBox_Height.md) | Gets and sets the height of the text box. |
| [HorizontalJustification](../TextBox/TextBox_HorizontalJustification.md) | Gets and sets the horizontal justification override of the text box. |
| [Layer](../TextBox/TextBox_Layer.md) | Gets and sets the layer applied to this text box. |
| [LineSpacing](../TextBox/TextBox_LineSpacing.md) | Gets and sets the line spacing of the text box. |
| [LineSpacingType](../TextBox/TextBox_LineSpacingType.md) | Gets and sets the method used to define the line spacing. |
| [Origin](../TextBox/TextBox_Origin.md) | Gets and sets the position of upper-left corner of the text box. |
| [OriginSketchPoint](../TextBox/TextBox_OriginSketchPoint.md) | Gets the SketchPoint on the origin of this TextBox. This will be Nothing in the case that the boundaries are displayed |
| [Parent](../TextBox/TextBox_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../TextBox/TextBox_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Rotation](../TextBox/TextBox_Rotation.md) | Gets and sets the override rotation of the text box. |
| [ShowBoundaries](../TextBox/TextBox_ShowBoundaries.md) | Gets and sets whether boundary geometry is displayed for the text box. |
| [SingleLineText](../TextBox/TextBox_SingleLineText.md) | Gets/Sets the single line text option. If True, all line breaks are removed from multi-line text. |
| [SketchBlockPath](../TextBox/TextBox_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [StackedTextPosition](../TextBox/TextBox_StackedTextPosition.md) | Gets and sets the position (alignment) of the stacked text with respect to regular text. |
| [Style](../TextBox/TextBox_Style.md) | Gets/Sets the text style associated with the text box. |
| [Text](../TextBox/TextBox_Text.md) | Gets and sets the string that defines the contents of the text box. |
| [Type](../TextBox/TextBox_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseBackgroundColor](../TextBox/TextBox_UseBackgroundColor.md) | Gets/Sets the UseBackgroundColor associated with the TextBox. |
| [VerticalJustification](../TextBox/TextBox_VerticalJustification.md) | Gets and sets the vertical justification override of the text box. |
| [Width](../TextBox/TextBox_Width.md) | Gets and sets the width of the text box. |
| [WidthScale](../TextBox/TextBox_WidthScale.md) | Gets and sets override stretch factor for the text box. |

## Accessed From

[ProfilePath.TextBox](../ProfilePath/ProfilePath_TextBox.md), [ProfilePathProxy.TextBox](../ProfilePathProxy/ProfilePathProxy_TextBox.md), [TextBoxConstraint.TextBox](../TextBoxConstraint/TextBoxConstraint_TextBox.md), [TextBoxConstraintProxy.TextBox](../TextBoxConstraintProxy/TextBoxConstraintProxy_TextBox.md), [TextBoxes.AddByRectangle](../TextBoxes/TextBoxes_AddByRectangle.md), [TextBoxes.AddFitted](../TextBoxes/TextBoxes_AddFitted.md), [TextBoxes.Item](../TextBoxes/TextBoxes_Item.md), [TextBoxProxy.NativeObject](../TextBoxProxy/TextBoxProxy_NativeObject.md)

## Derived Classes

[TextBoxProxy](../TextBoxProxy/TextBoxProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Sketch Text Add](../../sample-programs/TextBoxes_Sample.md) | This sample illustrates creating text in a sketch. |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |

## Version

Introduced in version 5.3
