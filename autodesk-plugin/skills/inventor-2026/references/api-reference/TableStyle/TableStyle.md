# TableStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The TableStyle object represents a general (custom) table style in a drawing. The properties and methods listed below are in addition to those supported by the Style object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddColumn](../TableStyle/TableStyle_AddColumn.md) | Method that adds a column to the list of default columns in the style. |
| [ConvertToLocal](../TableStyle/TableStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../TableStyle/TableStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../TableStyle/TableStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../TableStyle/TableStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [RemoveAllColumns](../TableStyle/TableStyle_RemoveAllColumns.md) | Method that removes all columns from the style. |
| [SaveToGlobal](../TableStyle/TableStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../TableStyle/TableStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TableStyle/TableStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ColumnHeaderTextStyle](../TableStyle/TableStyle_ColumnHeaderTextStyle.md) | Gets and sets the text style used for the column titles (headers). |
| [ColumnTitleHorizontalJustification](../TableStyle/TableStyle_ColumnTitleHorizontalJustification.md) | Gets and sets the justification of the column title. |
| [ColumnValueHorizontalJustification](../TableStyle/TableStyle_ColumnValueHorizontalJustification.md) | Gets and sets the justification of the values in the column. |
| [ColumnWidth](../TableStyle/TableStyle_ColumnWidth.md) | Gets and sets the default width of columns in centimeters. |
| [Comments](../TableStyle/TableStyle_Comments.md) | Gets and sets comments associated with the style. |
| [DataTextStyle](../TableStyle/TableStyle_DataTextStyle.md) | Gets and sets the text style used for the contents of the table. |
| [HeadingGap](../TableStyle/TableStyle_HeadingGap.md) | Gets and sets the heading gap in centimeters. |
| [HeadingPlacement](../TableStyle/TableStyle_HeadingPlacement.md) | Gets and sets the location of the heading (title). |
| [InsideLineColor](../TableStyle/TableStyle_InsideLineColor.md) | Gets and sets the color of the inner lines of the table. |
| [InsideLineWeight](../TableStyle/TableStyle_InsideLineWeight.md) | Gets and sets the line weight of the inner lines of the table. |
| [InternalName](../TableStyle/TableStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../TableStyle/TableStyle_InUse.md) | Property that indicates if this style is in use. |
| [Name](../TableStyle/TableStyle_Name.md) | Gets/Sets the name of the Style. |
| [OutsideLineColor](../TableStyle/TableStyle_OutsideLineColor.md) | Gets and sets the color of the outer lines of the table. |
| [OutsideLineWeight](../TableStyle/TableStyle_OutsideLineWeight.md) | Gets and sets the line weight of the outer lines of the table. |
| [Parent](../TableStyle/TableStyle_Parent.md) | Property returning the parent of this object. |
| [RowGap](../TableStyle/TableStyle_RowGap.md) | Gets and sets the row gap in centimeters. |
| [RowLineSpacing](../TableStyle/TableStyle_RowLineSpacing.md) | Gets and sets the spacing between the rows. |
| [ShowTitle](../TableStyle/TableStyle_ShowTitle.md) | Gets and sets the whether to show the title of the table. |
| [StyleLocation](../TableStyle/TableStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../TableStyle/TableStyle_StyleType.md) | Gets the type of the style. |
| [TableDirection](../TableStyle/TableStyle_TableDirection.md) | Gets and sets the direction of the table. |
| [Title](../TableStyle/TableStyle_Title.md) | Gets and sets the title of the table. |
| [TitleTextStyle](../TableStyle/TableStyle_TitleTextStyle.md) | Gets and sets the text style used for the title of the table. |
| [Type](../TableStyle/TableStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../TableStyle/TableStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[CustomTable.Style](../CustomTable/CustomTable_Style.md), [ObjectDefaultsStyle.BendTableStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_BendTableStyle.md), [ObjectDefaultsStyle.ConfigurationTableStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_ConfigurationTableStyle.md), [ObjectDefaultsStyle.TableStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_TableStyle.md), [TableStylesEnumerator.Item](../TableStylesEnumerator/TableStylesEnumerator_Item.md)

## Version

Introduced in version 2011
