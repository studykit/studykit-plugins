# PartsListFilterSettings.Add Method

Parent Object: [PartsListFilterSettings](../PartsListFilterSettings/PartsListFilterSettings.md)

## Description

Method that returns the specified PartsListFilterItem object from the collection.

## Syntax

PartsListFilterSettings.**Add**( ***PartsListFilterItemType*** As [PartsListFilterItemTypeEnum](../PartsListFilterItemTypeEnum.md), [***Options***] As Variant ) As [PartsListFilterItem](../PartsListFilterItem/PartsListFilterItem.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PartsListFilterItemType | [PartsListFilterItemTypeEnum](../PartsListFilterItemTypeEnum.md) | Input PartsListFilterItemTypeEnum value that specifies the PartsListFilterItem to add. If the same type item already exists, this returns an error. |
| Options | Variant | Optional input NameValueMap that specifies the options to set. Below are valid values:  | Options | Applied to | | --- | --- | | Name = “StandardContentOnly”. Value = Boolean value that specifies whether to show only the standard content or not. | kStandardContentFilterItem | | Name = “PurchasedItemsOnly”. Value = Boolean value that specifies whether to show the purchased items only. | kPurchasedItemsFilterItem | | Name = “ItemNumberRange”. Value = String value that specifies the item number range(e.g.:1,3,7-10 ). | kItemNumberRangeFilterItem | | Name = “AssemblyViewRepresentation”. Value = DesignViewRepresentation object that specifies the assembly design view representation. | AssemblyViewRepresentation | | Name = “LimitQTYToVisibleComponentsOnly”. Value = Boolean value that specifies whether limit QTY to visible components only. | AssemblyViewRepresentation | |

## Version

Introduced in version 2024.1

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |