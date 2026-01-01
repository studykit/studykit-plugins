# ChainDimensionSet.MergeMembers Method

Parent Object: [ChainDimensionSet](../ChainDimensionSet/ChainDimensionSet.md)

## Description

Method that merges two members of the set by deleting the second member and healing (modifying) the first member to fill the gap. The input members must be contiguous, else the method will fail.

## Syntax

ChainDimensionSet.**MergeMembers**( ***MemberOne*** As [LinearGeneralDimension](../LinearGeneralDimension/LinearGeneralDimension.md), ***MemberTwo*** As [LinearGeneralDimension](../LinearGeneralDimension/LinearGeneralDimension.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MemberOne | [LinearGeneralDimension](../LinearGeneralDimension/LinearGeneralDimension.md) | Input LinearGeneralDimension object that specifies the first member of the set to merge. This member is retained and modified. |
| MemberTwo | [LinearGeneralDimension](../LinearGeneralDimension/LinearGeneralDimension.md) | Input LinearGeneralDimension object that specifies the second member of the set to merge. This member is deleted. |

## Version

Introduced in version 2011
