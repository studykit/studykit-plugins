# RevisionTableStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The RevisionTableStyle object represents a revision table style in a drawing. The properties and methods listed below are in addition to those supported by the Style object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddColumn](../RevisionTableStyle/RevisionTableStyle_AddColumn.md) | Method that adds a column to the list of default columns in the style. |
| [ConvertToLocal](../RevisionTableStyle/RevisionTableStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../RevisionTableStyle/RevisionTableStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../RevisionTableStyle/RevisionTableStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../RevisionTableStyle/RevisionTableStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [RemoveAllColumns](../RevisionTableStyle/RevisionTableStyle_RemoveAllColumns.md) | Method that removes all columns from the style. |
| [SaveToGlobal](../RevisionTableStyle/RevisionTableStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../RevisionTableStyle/RevisionTableStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllowLandingLineForRevisionTags](../RevisionTableStyle/RevisionTableStyle_AllowLandingLineForRevisionTags.md) | Gets and sets the whether to add landing to revision tags. |
| [Application](../RevisionTableStyle/RevisionTableStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ColumnHeaderTextStyle](../RevisionTableStyle/RevisionTableStyle_ColumnHeaderTextStyle.md) | Gets and sets the text style used for the column titles (headers). |
| [Comments](../RevisionTableStyle/RevisionTableStyle_Comments.md) | Gets and sets comments associated with the style. |
| [DataTextStyle](../RevisionTableStyle/RevisionTableStyle_DataTextStyle.md) | Gets and sets the text style used for the contents of the table. |
| [HeadingGap](../RevisionTableStyle/RevisionTableStyle_HeadingGap.md) | Gets and sets the heading gap in centimeters. |
| [HeadingPlacement](../RevisionTableStyle/RevisionTableStyle_HeadingPlacement.md) | Gets and sets the location of the heading (title). |
| [InsideLineColor](../RevisionTableStyle/RevisionTableStyle_InsideLineColor.md) | Gets and sets the color of the inner lines of the table. |
| [InsideLineWeight](../RevisionTableStyle/RevisionTableStyle_InsideLineWeight.md) | Gets and sets the line weight of the inner lines of the table. |
| [InternalName](../RevisionTableStyle/RevisionTableStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../RevisionTableStyle/RevisionTableStyle_InUse.md) | Property that indicates if this style is in use. |
| [Name](../RevisionTableStyle/RevisionTableStyle_Name.md) | Gets/Sets the name of the Style. |
| [OutsideLineColor](../RevisionTableStyle/RevisionTableStyle_OutsideLineColor.md) | Gets and sets the color of the outer lines of the table. |
| [OutsideLineWeight](../RevisionTableStyle/RevisionTableStyle_OutsideLineWeight.md) | Gets and sets the line weight of the outer lines of the table. |
| [Parent](../RevisionTableStyle/RevisionTableStyle_Parent.md) | Property returning the parent of this object. |
| [RevisionIndexDefaults](../RevisionTableStyle/RevisionTableStyle_RevisionIndexDefaults.md) | Gets the RevisionIndexDefaults object. |
| [RevisionTagLeaderStyle](../RevisionTableStyle/RevisionTableStyle_RevisionTagLeaderStyle.md) | Gets and sets the leader style used for revision tags. |
| [RevisionTagShape](../RevisionTableStyle/RevisionTableStyle_RevisionTagShape.md) | Gets and sets the shape for revision tags. |
| [RevisionTagTextStyle](../RevisionTableStyle/RevisionTableStyle_RevisionTagTextStyle.md) | Gets and sets the text style used for revision tags. |
| [RowGap](../RevisionTableStyle/RevisionTableStyle_RowGap.md) | Gets and sets the row gap in centimeters. |
| [RowLineSpacing](../RevisionTableStyle/RevisionTableStyle_RowLineSpacing.md) | Gets and sets the spacing between the rows. |
| [ShowTitle](../RevisionTableStyle/RevisionTableStyle_ShowTitle.md) | Gets and sets the whether to show the title of the table. |
| [StyleLocation](../RevisionTableStyle/RevisionTableStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../RevisionTableStyle/RevisionTableStyle_StyleType.md) | Gets the type of the style. |
| [TableDirection](../RevisionTableStyle/RevisionTableStyle_TableDirection.md) | Gets and sets the direction of the table. |
| [Title](../RevisionTableStyle/RevisionTableStyle_Title.md) | Gets and sets the title of the table. |
| [TitleTextStyle](../RevisionTableStyle/RevisionTableStyle_TitleTextStyle.md) | Gets and sets the text style used for the title of the table. |
| [Type](../RevisionTableStyle/RevisionTableStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../RevisionTableStyle/RevisionTableStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[ObjectDefaultsStyle.RevisionTableStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_RevisionTableStyle.md), [ObjectDefaultsStyle.RevisionTagStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_RevisionTagStyle.md), [RevisionTable.Style](../RevisionTable/RevisionTable_Style.md), [RevisionTableStylesEnumerator.Item](../RevisionTableStylesEnumerator/RevisionTableStylesEnumerator_Item.md)

## Version

Introduced in version 2011
