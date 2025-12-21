# TextBoxProxy Object

Derived from: [TextBox](../TextBox/TextBox.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToGeometry](../TextBoxProxy/TextBoxProxy_ConvertToGeometry.md) | Method that converts the text box to sketch geometries. |
| [Delete](../TextBoxProxy/TextBoxProxy_Delete.md) | Method that deletes the text box. |
| [GetFacetsInfo](../TextBoxProxy/TextBoxProxy_GetFacetsInfo.md) | Returns facets’ coordinates of the text box. |
| [GetReferenceKey](../TextBoxProxy/TextBoxProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TextBoxProxy/TextBoxProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TextBoxProxy/TextBoxProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BackgroundColor](../TextBoxProxy/TextBoxProxy_BackgroundColor.md) | Gets/Sets the BackgroundColor associated with the TextBox. |
| [BoundaryGeometry](../TextBoxProxy/TextBoxProxy_BoundaryGeometry.md) | Property that returns the four construction sketch lines that form the boundary of the text box. |
| [Color](../TextBoxProxy/TextBoxProxy_Color.md) | Gets/Sets the color of the text box. |
| [ContainingOccurrence](../TextBoxProxy/TextBoxProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ContainingSketchBlock](../TextBoxProxy/TextBoxProxy_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [Fitted](../TextBoxProxy/TextBoxProxy_Fitted.md) | Property that returns if the text box remains tightly fitted to the text within the box. True indicates the text box just encloses the text. |
| [FittedTextHeight](../TextBoxProxy/TextBoxProxy_FittedTextHeight.md) | Property that returns the actual height of the text within the text box. This does not necessarily represent the current height of the text box, but only the text within the box. If the Fitted property is True then this value is the same as the height of the text box. |
| [FittedTextWidth](../TextBoxProxy/TextBoxProxy_FittedTextWidth.md) | Property that returns the actual width of the text within the text box. This does not necessarily represent the current width of the text box, but only the text within the box. If the Fitted property is True then this value is the same as the width of the text box. |
| [FormattedText](../TextBoxProxy/TextBoxProxy_FormattedText.md) | Gets and sets the fully formatted string that defines the contents of the text box. |
| [Height](../TextBoxProxy/TextBoxProxy_Height.md) | Gets and sets the height of the text box. |
| [HorizontalJustification](../TextBoxProxy/TextBoxProxy_HorizontalJustification.md) | Gets and sets the horizontal justification override of the text box. |
| [Layer](../TextBoxProxy/TextBoxProxy_Layer.md) | Gets and sets the layer applied to this text box. |
| [LineSpacing](../TextBoxProxy/TextBoxProxy_LineSpacing.md) | Gets and sets the line spacing of the text box. |
| [LineSpacingType](../TextBoxProxy/TextBoxProxy_LineSpacingType.md) | Gets and sets the method used to define the line spacing. |
| [NativeObject](../TextBoxProxy/TextBoxProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Origin](../TextBoxProxy/TextBoxProxy_Origin.md) | Gets and sets the position of upper-left corner of the text box. |
| [OriginSketchPoint](../TextBoxProxy/TextBoxProxy_OriginSketchPoint.md) | Gets the SketchPoint on the origin of this TextBox. This will be Nothing in the case that the boundaries are displayed |
| [Parent](../TextBoxProxy/TextBoxProxy_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../TextBoxProxy/TextBoxProxy_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Rotation](../TextBoxProxy/TextBoxProxy_Rotation.md) | Gets and sets the override rotation of the text box. |
| [ShowBoundaries](../TextBoxProxy/TextBoxProxy_ShowBoundaries.md) | Gets and sets whether boundary geometry is displayed for the text box. |
| [SingleLineText](../TextBoxProxy/TextBoxProxy_SingleLineText.md) | Gets/Sets the single line text option. If True, all line breaks are removed from multi-line text. |
| [SketchBlockPath](../TextBoxProxy/TextBoxProxy_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [StackedTextPosition](../TextBoxProxy/TextBoxProxy_StackedTextPosition.md) | Gets and sets the position (alignment) of the stacked text with respect to regular text. |
| [Style](../TextBoxProxy/TextBoxProxy_Style.md) | Gets/Sets the text style associated with the text box. |
| [Text](../TextBoxProxy/TextBoxProxy_Text.md) | Gets and sets the string that defines the contents of the text box. |
| [Type](../TextBoxProxy/TextBoxProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseBackgroundColor](../TextBoxProxy/TextBoxProxy_UseBackgroundColor.md) | Gets/Sets the UseBackgroundColor associated with the TextBox. |
| [VerticalJustification](../TextBoxProxy/TextBoxProxy_VerticalJustification.md) | Gets and sets the vertical justification override of the text box. |
| [Width](../TextBoxProxy/TextBoxProxy_Width.md) | Gets and sets the width of the text box. |
| [WidthScale](../TextBoxProxy/TextBoxProxy_WidthScale.md) | Gets and sets override stretch factor for the text box. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |