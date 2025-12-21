# HoleTable Object

## Description

A hole table contains information for some or all holes in a drawing view. A hole tag is associated with each hole and a corresponding row in the table. If an existing hole is changed, the hole table is updated when the drawing updates.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../HoleTable/HoleTable_Delete.md) | Method that deletes the HoleTable. |
| [Export](../HoleTable/HoleTable_Export.md) | Method that saves the custom table to an external file. |
| [GetReferenceKey](../HoleTable/HoleTable_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [MatchCustomHoles](../HoleTable/HoleTable_MatchCustomHoles.md) | Method that specifies two or more custom holes (designated with center marks) to be the same. |
| [ShowTags](../HoleTable/HoleTable_ShowTags.md) | Property that indicates whether to show or hide all the hole tags associated with this table. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../HoleTable/HoleTable_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArrangeByPosition](../HoleTable/HoleTable_ArrangeByPosition.md) | Gets/Sets whether to tags holes relative to their position on the selected view or by their relative size. |
| [AttributeSets](../HoleTable/HoleTable_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ColumnHeaderTextStyle](../HoleTable/HoleTable_ColumnHeaderTextStyle.md) | Gets/Sets the text style used for the column titles (headers). |
| [DataTextStyle](../HoleTable/HoleTable_DataTextStyle.md) | Gets/Sets the text style used for the contents of the table. |
| [DeleteTagsOnRollup](../HoleTable/HoleTable_DeleteTagsOnRollup.md) | Gets/Sets whether to delete tags except for the first in a series of hole tags when the row merge type is kRollupRowMerge. |
| [GroupHoleTypes](../HoleTable/HoleTable_GroupHoleTypes.md) | Gets/Sets whether to group and tag holes by type. |
| [HeadingPlacement](../HoleTable/HoleTable_HeadingPlacement.md) | Gets/Sets the placement position of the HoleTable heading. |
| [HoleTableColumns](../HoleTable/HoleTable_HoleTableColumns.md) | Property that returns the HoleTableColumns collection object. |
| [HoleTableRows](../HoleTable/HoleTable_HoleTableRows.md) | Property that returns the HoleTableRows collection object. |
| [HoleTableType](../HoleTable/HoleTable_HoleTableType.md) | Property that returns the type of the hole table. |
| [IncludeCentermarks](../HoleTable/HoleTable_IncludeCentermarks.md) | Gets/Sets whether to include center marks. |
| [IncludeCircularCuts](../HoleTable/HoleTable_IncludeCircularCuts.md) | Gets/Sets whether to include extruded cuts. |
| [IncludeCounterBoreHoleFeatures](../HoleTable/HoleTable_IncludeCounterBoreHoleFeatures.md) | Gets/Sets whether to include counterbored hole features. |
| [IncludeCounterSinkHoleFeatures](../HoleTable/HoleTable_IncludeCounterSinkHoleFeatures.md) | Gets/Sets whether to include countersunk hole features. |
| [IncludeDrilledHoleFeatures](../HoleTable/HoleTable_IncludeDrilledHoleFeatures.md) | Gets/Sets whether to include drilled hole features. |
| [IncludeHoleFeatures](../HoleTable/HoleTable_IncludeHoleFeatures.md) | Gets/Sets whether to include hole features. |
| [IncludeRecoveredPunchCenters](../HoleTable/HoleTable_IncludeRecoveredPunchCenters.md) | Gets/Sets whether to include recovered punch center marks. |
| [IncludeThreadedHoleFeatures](../HoleTable/HoleTable_IncludeThreadedHoleFeatures.md) | Gets/Sets whether to include threaded hole features. |
| [Layer](../HoleTable/HoleTable_Layer.md) | Gets and sets the layer used by the HoleTable. |
| [Parent](../HoleTable/HoleTable_Parent.md) | Property that returns the parent object of this HoleTable. |
| [ParentView](../HoleTable/HoleTable_ParentView.md) | Property that returns the drawing view that this table is associated with. |
| [Position](../HoleTable/HoleTable_Position.md) | Gets/Sets the position of the HoleTable on the sheet. |
| [PreserveTagging](../HoleTable/HoleTable_PreserveTagging.md) | Gets/Sets whether to preserve the hole tags assigned when the table is created. |
| [RangeBox](../HoleTable/HoleTable_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [ReformatOnCustomHoleMatch](../HoleTable/HoleTable_ReformatOnCustomHoleMatch.md) | Gets/Sets whether to re-index the hole tags and resort contents when a Match Custom Hole operation is done. |
| [RowMergeType](../HoleTable/HoleTable_RowMergeType.md) | Gets/Sets the row merge option for the hole table. |
| [SecondaryTagModifierOnRollup](../HoleTable/HoleTable_SecondaryTagModifierOnRollup.md) | Gets/Sets whether to include a secondary numeric tag when the row merge type is kRollupRowMerge. |
| [SequentialNumbering](../HoleTable/HoleTable_SequentialNumbering.md) | Gets/Sets whether to replace the alphanumeric hole tags with sequential numbering of the holes in the hole table. |
| [ShowTitle](../HoleTable/HoleTable_ShowTitle.md) | Gets and sets whether to show the title of the hole table. |
| [Style](../HoleTable/HoleTable_Style.md) | Gets/Sets the associated HoleTableStyle object. |
| [Title](../HoleTable/HoleTable_Title.md) | Gets/Sets the title of the HoleTable. |
| [TitleTextStyle](../HoleTable/HoleTable_TitleTextStyle.md) | Gets/Sets the text style used for the title of the table. |
| [Type](../HoleTable/HoleTable_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[HoleTableCell.Parent](../HoleTableCell/HoleTableCell_Parent.md), [HoleTableColumn.Parent](../HoleTableColumn/HoleTableColumn_Parent.md), [HoleTableRow.Parent](../HoleTableRow/HoleTableRow_Parent.md), [HoleTables.Add](../HoleTables/HoleTables_Add.md), [HoleTables.AddByFeatureType](../HoleTables/HoleTables_AddByFeatureType.md), [HoleTables.AddSelected](../HoleTables/HoleTables_AddSelected.md), [HoleTables.Item](../HoleTables/HoleTables_Item.md)

## Version

Introduced in version 10
