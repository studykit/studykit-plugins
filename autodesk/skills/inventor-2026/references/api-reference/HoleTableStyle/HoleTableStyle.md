# HoleTableStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The HoleTableStyle object represents a hole table style in a drawing. The properties and methods listed below are in addition to those supported by the Style object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddColumn](../HoleTableStyle/HoleTableStyle_AddColumn.md) | Method that adds a column to the list of default columns in the style. |
| [ConvertToLocal](../HoleTableStyle/HoleTableStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../HoleTableStyle/HoleTableStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../HoleTableStyle/HoleTableStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../HoleTableStyle/HoleTableStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [RemoveAllColumns](../HoleTableStyle/HoleTableStyle_RemoveAllColumns.md) | Method that removes all columns from the style. |
| [SaveToGlobal](../HoleTableStyle/HoleTableStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../HoleTableStyle/HoleTableStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../HoleTableStyle/HoleTableStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArrangeByPosition](../HoleTableStyle/HoleTableStyle_ArrangeByPosition.md) | Gets and sets whether to tags holes relative to their position on the selected view or by their relative size. |
| [ColumnHeaderTextStyle](../HoleTableStyle/HoleTableStyle_ColumnHeaderTextStyle.md) | Gets and sets the text style used for the column titles (headers). |
| [Comments](../HoleTableStyle/HoleTableStyle_Comments.md) | Gets and sets comments associated with the style. |
| [DataTextStyle](../HoleTableStyle/HoleTableStyle_DataTextStyle.md) | Gets and sets the text style used for the contents of the table. |
| [DeleteTagsOnRollup](../HoleTableStyle/HoleTableStyle_DeleteTagsOnRollup.md) | Gets and sets whether to delete tags except for the first in a series of hole tags when the row merge type is kRollupRowMerge. |
| [GroupHoleTypes](../HoleTableStyle/HoleTableStyle_GroupHoleTypes.md) | Gets and sets whether to group and tag holes by type. |
| [HeadingPlacement](../HoleTableStyle/HoleTableStyle_HeadingPlacement.md) | Gets and sets the location of the heading (title). |
| [IncludeCentermarks](../HoleTableStyle/HoleTableStyle_IncludeCentermarks.md) | Gets and sets whether to include center marks. |
| [IncludeCircularCuts](../HoleTableStyle/HoleTableStyle_IncludeCircularCuts.md) | Gets and sets whether to include extruded cuts. |
| [IncludeCounterBoreHoleFeatures](../HoleTableStyle/HoleTableStyle_IncludeCounterBoreHoleFeatures.md) | Gets and sets whether to include counterbored hole features. |
| [IncludeCounterSinkHoleFeatures](../HoleTableStyle/HoleTableStyle_IncludeCounterSinkHoleFeatures.md) | Gets and sets whether to include countersunk hole features. |
| [IncludeDrilledHoleFeatures](../HoleTableStyle/HoleTableStyle_IncludeDrilledHoleFeatures.md) | Gets and sets whether to include drilled hole features. |
| [IncludeHoleFeatures](../HoleTableStyle/HoleTableStyle_IncludeHoleFeatures.md) | Gets and sets whether to include hole features. Applies only to view based hole tables. |
| [IncludeRecoveredPunchCenters](../HoleTableStyle/HoleTableStyle_IncludeRecoveredPunchCenters.md) | Gets and sets whether to include recovered punch center marks. |
| [IncludeThreadedHoleFeatures](../HoleTableStyle/HoleTableStyle_IncludeThreadedHoleFeatures.md) | Gets and sets whether to include threaded hole features. |
| [InsideLineColor](../HoleTableStyle/HoleTableStyle_InsideLineColor.md) | Gets and sets the color of the inner lines of the table. |
| [InsideLineWeight](../HoleTableStyle/HoleTableStyle_InsideLineWeight.md) | Gets and sets the line weight of the inner lines of the table. |
| [InternalName](../HoleTableStyle/HoleTableStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../HoleTableStyle/HoleTableStyle_InUse.md) | Property that indicates if this style is in use. |
| [Name](../HoleTableStyle/HoleTableStyle_Name.md) | Gets/Sets the name of the Style. |
| [OutsideLineColor](../HoleTableStyle/HoleTableStyle_OutsideLineColor.md) | Gets and sets the color of the outer lines of the table. |
| [OutsideLineWeight](../HoleTableStyle/HoleTableStyle_OutsideLineWeight.md) | Gets and sets the line weight of the outer lines of the table. |
| [Parent](../HoleTableStyle/HoleTableStyle_Parent.md) | Property returning the parent of this object. |
| [PreserveTagging](../HoleTableStyle/HoleTableStyle_PreserveTagging.md) | Gets and sets whether to preserve the hole tags assigned when the table is created. |
| [ReformatOnCustomHoleMatch](../HoleTableStyle/HoleTableStyle_ReformatOnCustomHoleMatch.md) | Gets and sets whether to re-index the hole tags and resort contents when a Match Custom Hole operation is done. |
| [RowMergeType](../HoleTableStyle/HoleTableStyle_RowMergeType.md) | Gets and sets the row merge option for the hole table. |
| [SecondaryTagModifierOnRollup](../HoleTableStyle/HoleTableStyle_SecondaryTagModifierOnRollup.md) | Gets and sets whether to include a secondary numeric tag when the row merge type is kRollupRowMerge. |
| [SequentialNumbering](../HoleTableStyle/HoleTableStyle_SequentialNumbering.md) | Gets and sets whether to replace the alphanumeric hole tags with sequential numbering of the holes in the hole table. |
| [StyleLocation](../HoleTableStyle/HoleTableStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../HoleTableStyle/HoleTableStyle_StyleType.md) | Gets the type of the style. |
| [Title](../HoleTableStyle/HoleTableStyle_Title.md) | Gets and sets the title of the HoleTable. |
| [TitleTextStyle](../HoleTableStyle/HoleTableStyle_TitleTextStyle.md) | Gets and sets the text style used for the title of the table. |
| [Type](../HoleTableStyle/HoleTableStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../HoleTableStyle/HoleTableStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |
| [UseLeaderForTags](../HoleTableStyle/HoleTableStyle_UseLeaderForTags.md) | Gets and sets whether to generate a leader for any hole tag dragged away from the hole with which it is associated. |

## Accessed From

[HoleTable.Style](../HoleTable/HoleTable_Style.md), [HoleTableStylesEnumerator.Item](../HoleTableStylesEnumerator/HoleTableStylesEnumerator_Item.md), [ObjectDefaultsStyle.HoleTableStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_HoleTableStyle.md)

## Version

Introduced in version 2009
