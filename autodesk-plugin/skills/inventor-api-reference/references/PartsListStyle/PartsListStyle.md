# PartsListStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The PartsListStyle object represents a parts list style in a drawing. The properties and methods listed below are in addition to those supported by the Style object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddColumn](../PartsListStyle/PartsListStyle_AddColumn.md) | Method that adds a column to the list of default columns in the style. |
| [ConvertToLocal](../PartsListStyle/PartsListStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../PartsListStyle/PartsListStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../PartsListStyle/PartsListStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../PartsListStyle/PartsListStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [RemoveAllColumns](../PartsListStyle/PartsListStyle_RemoveAllColumns.md) | Method that removes all columns from the style. |
| [SaveToGlobal](../PartsListStyle/PartsListStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../PartsListStyle/PartsListStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PartsListStyle/PartsListStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ColumnHeaderTextStyle](../PartsListStyle/PartsListStyle_ColumnHeaderTextStyle.md) | Gets and sets the text style used for the column titles (headers). |
| [Comments](../PartsListStyle/PartsListStyle_Comments.md) | Gets and sets comments associated with the style. |
| [DataTextStyle](../PartsListStyle/PartsListStyle_DataTextStyle.md) | Gets and sets the text style used for the contents of the table. |
| [HeadingGap](../PartsListStyle/PartsListStyle_HeadingGap.md) | Gets and sets the heading gap in centimeters. |
| [HeadingPlacement](../PartsListStyle/PartsListStyle_HeadingPlacement.md) | Gets and sets the location of the heading (title). |
| [InternalName](../PartsListStyle/PartsListStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../PartsListStyle/PartsListStyle_InUse.md) | Property that indicates if this style is in use. |
| [Name](../PartsListStyle/PartsListStyle_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../PartsListStyle/PartsListStyle_Parent.md) | Property returning the parent of this object. |
| [RowGap](../PartsListStyle/PartsListStyle_RowGap.md) | Gets and sets the row gap in centimeters. |
| [RowLineSpacing](../PartsListStyle/PartsListStyle_RowLineSpacing.md) | Gets and sets the spacing between the rows. |
| [ShowTitle](../PartsListStyle/PartsListStyle_ShowTitle.md) | Gets and sets the whether to show the title of the table. |
| [SortSettings](../PartsListStyle/PartsListStyle_SortSettings.md) | Gets the parts list sort settings. |
| [StyleLocation](../PartsListStyle/PartsListStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../PartsListStyle/PartsListStyle_StyleType.md) | Gets the type of the style. |
| [TableDirection](../PartsListStyle/PartsListStyle_TableDirection.md) | Gets and sets the direction of the table based on the Item numbers. |
| [Title](../PartsListStyle/PartsListStyle_Title.md) | Gets and sets the title of the PartListTable. |
| [TitleTextStyle](../PartsListStyle/PartsListStyle_TitleTextStyle.md) | Gets and sets the text style used for the title of the table. |
| [Type](../PartsListStyle/PartsListStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../PartsListStyle/PartsListStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |

## Accessed From

[ObjectDefaultsStyle.PartsListStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_PartsListStyle.md), [PartsList.Style](../PartsList/PartsList_Style.md), [PartsListStylesEnumerator.Item](../PartsListStylesEnumerator/PartsListStylesEnumerator_Item.md)

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |